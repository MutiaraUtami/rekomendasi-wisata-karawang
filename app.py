from flask import Flask, render_template, request
import pandas as pd
from datetime import datetime
from fuzzy import (
    haversine, fuzzy_bintang, fuzzy_harga,
    fuzzy_jam_operasional, fuzzy_distance,
    fuzzy_open_status, hitung_fuzzy_score
)

app = Flask(__name__)

# Default lokasi user (contoh: Karawang Kota)
DEFAULT_LAT = -6.3054
DEFAULT_LON = 107.3065

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/')
def landing():
    df = pd.read_csv('wisatakarawang.csv')
    df[['Latitude', 'Longitude']] = df['Koordinat'].str.split(',', expand=True).astype(float)

    # Ambil 3 data acak
    wisata_random = df[['Nama Tempat Wisata', 'Kecamatan', 'Kategori', 'Bintang',
                        'Harga Tiket', 'Jam Buka', 'Jam Tutup']].sample(3)

    return render_template('landing.html', wisata=wisata_random.to_dict(orient='records'))
  
@app.route('/hasil', methods=['POST'])
def rekomendasi():
    # Ambil data dari form (atau pakai default)
    
    lat = float(request.form.get('lat', DEFAULT_LAT))
    lon = float(request.form.get('lon', DEFAULT_LON))

    # Ambil waktu saat ini (format jam decimal)
    current_time = datetime.now().hour + datetime.now().minute / 60

    # Load data wisata
    df = pd.read_csv('wisatakarawang.csv')
    df[['Latitude', 'Longitude']] = df['Koordinat'].str.split(',', expand=True).astype(float)

    # Hitung skor fuzzy
    df['Skor Fuzzy'] = df.apply(lambda row: hitung_fuzzy_score(row, lat, lon, current_time), axis=1)
    df_sorted = df.sort_values(by='Skor Fuzzy', ascending=False)

    # Ambil 10 rekomendasi teratas
    rekomendasi = df_sorted[['Nama Tempat Wisata', 'Kecamatan', 'Kategori', 'Bintang',
                             'Harga Tiket', 'Jam Buka', 'Jam Tutup', 'Skor Fuzzy']].head(10).to_dict(orient='records')

    return render_template('hasil.html', rekomendasi=rekomendasi)

if __name__ == '__main__':
    app.run(debug=True)

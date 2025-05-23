import math

def fuzzy_bintang(bintang):
    if bintang >= 4.5:
        return 1.0
    elif bintang >= 3.5:
        return 0.7
    elif bintang >= 2.5:
        return 0.5
    else:
        return 0.2

def fuzzy_harga(harga):
    if harga <= 10000:
        return 1.0
    elif harga <= 20000:
        return 0.7
    elif harga <= 40000:
        return 0.5
    else:
        return 0.2

def fuzzy_jam_operasional(buka, tutup):
    try:
        jam_buka = int(tutup.split(":")[0]) - int(buka.split(":")[0])
    except:
        jam_buka = 0
    if jam_buka >= 12:
        return 1.0
    elif jam_buka >= 8:
        return 0.7
    elif jam_buka >= 5:
        return 0.5
    else:
        return 0.2

def fuzzy_distance(jarak):
    if jarak <= 5:
        return 1.0
    elif jarak <= 10:
        return 0.7
    elif jarak <= 20:
        return 0.5
    else:
        return 0.2

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Jari-jari bumi dalam kilometer
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = math.sin(dLat/2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dLon/2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

def fuzzy_open_status(jam_buka, jam_tutup, current_time):
    if jam_buka <= current_time <= jam_tutup:
        return 1.0
    else:
        return 0.0  # Tutup → tidak direkomendasikan
def hitung_fuzzy_score(row, user_lat, user_lon, current_time):
    b = fuzzy_bintang(row['Bintang'])
    h = fuzzy_harga(row['Harga Tiket'])
    j = fuzzy_jam_operasional(row['Jam Buka'], row['Jam Tutup'])

    # Hitung jarak dari lokasi pengguna ke lokasi tempat
    jarak = haversine(user_lat, user_lon, row['Latitude'], row['Longitude'])
    d = fuzzy_distance(jarak)

    # Konversi jam buka dan tutup ke bentuk numerik (misalnya "08:00" -> 8.0)
    buka = int(row['Jam Buka'].split(":")[0])
    tutup = int(row['Jam Tutup'].split(":")[0])
    open_status = fuzzy_open_status(buka, tutup, current_time)

    # Hitung skor total
    total_score = (b + h + j + d + open_status) / 5
    return total_score

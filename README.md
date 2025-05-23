# 🗺️ Rekomendasi Wisata Karawang dengan Metode Fuzzy
Program ini dibuat untuk memberikan rekomendasi tempat wisata di Karawang berdasarkan beberapa kriteria yang dihitung menggunakan metode fuzzy logic. Data yang digunakan berasal dari file wisatakarawang.csv, yang merupakan data sekunder yang dikumpulkan dari Dinas Pariwisata Karawang dan sumber terpercaya lainnya.

## 📌 Fitur Utama
Pengguna dapat memasukkan lokasi saat ini (latitude dan longitude).

Sistem akan menghitung skor fuzzy untuk setiap tempat wisata berdasarkan:

- ⭐ Rating/Bintang

- 💸 Harga Tiket

- 📍 Jarak dari lokasi pengguna

- 🟢 Status buka pada waktu akses

Output berupa daftar rekomendasi wisata yang diurutkan berdasarkan skor tertinggi.

## Algoritma Inti:
Setiap kriteria (bintang, harga, jam, jarak, buka/tutup) difuzzifikasi menjadi nilai numerik.

Jarak dihitung menggunakan rumus Haversine untuk mendapatkan jarak sejauh mungkin secara geografis.

Semua nilai dikombinasikan secara rata-rata untuk menghasilkan skor rekomendasi akhir.

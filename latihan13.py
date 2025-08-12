# Latihan 1: Membuat dan Mengakses
jadwal_senin = ["Matematika", "Bahasa Indonesia", "Olahraga", "Sejarah"]

# Cetak seluruh list
print(jadwal_senin)

# Cetak hanya mata pelajaran pertama
print(jadwal_senin[0])

# Cetak mata pelajaran terakhir menggunakan indeks negatif
print(jadwal_senin[-1])


# Latihan 2: Modifikasi List
# Mengganti "Olahraga" dengan "Kimia"
jadwal_senin[2] = "Kimia"

# Cetak list yang diperbarui
print(jadwal_senin)


# Latihan 3: Traversing dan Modifikasi
nilai_mentah = [55, 63, 72, 81, 90]

for i in range(len(nilai_mentah)):
    nilai_mentah[i] += 5  # Menambahkan nilai bonus 5 poin

print(nilai_mentah)


# Latihan 4: Slicing dan Penggabungan
awal_minggu = ["Senin", "Selasa", "Rabu"]
akhir_minggu = ["Kamis", "Jumat", "Sabtu", "Minggu"]

# Menggabungkan dua list
seminggu = awal_minggu + akhir_minggu

# Mengambil hari kerja (Senin sampai Jumat)
hari_kerja = seminggu[:5]

print(hari_kerja)

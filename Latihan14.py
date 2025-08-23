#1.Menejemen Daftar belanja
# List kosong
belanjaan = []

# Menambahkan item
belanjaan.append("Telur")
belanjaan.append("Susu")
belanjaan.append("Roti")

# Menambahkan di posisi paling awal
belanjaan.insert(0, "Apel")

# Menghapus item
belanjaan.remove("Susu")

# Cetak hasil akhir
print("Daftar belanja:", belanjaan)

#Daftar belanja: ['Apel', 'Telur','susu','Roti']

#2.Mengurutkan tanpa merubah
nilai = [98, 76, 88, 100, 54]

# Mendapatkan list terurut tanpa mengubah aslinya
nilai_terurut = sorted(nilai)

print("Nilai asli:", nilai)
print("Nilai terurut:", nilai_terurut)

#3.Analisit kata
# Meminta input dari pengguna
kalimat = input("Masukkan sebuah kalimat: ")

# Memecah kalimat menjadi list kata
kata_kata = kalimat.split()

# Hitung jumlah kata
print("Jumlah kata:", len(kata_kata))

# Urutkan kata-kata berdasarkan abjad
kata_kata.sort()

print("Kata-kata terurut:", kata_kata)

#4.Memahami Aliasing
a = [1, 2, 3, 4, 5]
b = a          # b dan a menunjuk list yang sama (aliasing)
c = a.copy()   # c adalah salinan list a

b[1] = 20      # Mengubah elemen ke-2 di b (juga mengubah a)
c[1] = 30      # Mengubah elemen ke-2 di c (tidak memengaruhi a)

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

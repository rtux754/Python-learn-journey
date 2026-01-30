# latihan logika dan komparasi
#
# membuat gabungan area rentang dari angka
#
# +++++3----10++++
#

inputUser = float(input("Masukkan angka < 7 atau > 25: "))

# +++++3
# memeriksa angka kurang dari
kurangdari = inputUser < 7
print("Kurang dari:", kurangdari)

# 10++++
# memeriksa angka lebih dari
lebihdari = inputUser > 25
print("Lebih dari:", lebihdari)

# memeriksa hasil input
hasil = kurangdari or lebihdari
print("Hasil yang anda masukkan :", hasil)

# ----3+++++10----
# kasus irisan
# mencari angka rentang tengah tengah
print("\n", 10 * "=", "\n")
inputuser = float(input("Masukkan angka > 9 atau < 36: "))

# memeriksa angka lebih dari
# -----9+++++
lebih = inputuser > 9
print("Lebih dari:", lebih)

# memeriksa angka kurang dari
# +++++39----
kurang = inputuser < 36
print("Kurang dari:", kurang)


# memeriksa hasil input
out = lebih and kurang
print("Hasil:", out)

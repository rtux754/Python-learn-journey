# ----0++++5----8+++++11-----
# ++++0----5++++8-----11+++++

print("----0++++5----8+++++11-----\n")
print("Cara 1")
inputUser = float(input("Masukkan angka : "))

tanda1 = inputUser > 0 and inputUser < 5
print("Hasil pertama:", tanda1)

tanda2 = inputUser > 8 and inputUser < 11
print("Hasil kedua:", tanda2)

hasil = tanda1 or tanda2
print("Hasil akhir:", hasil)

print("\n", 10 * "=", "\n")
print("Cara 2")

Tanda1 = 0 < inputUser < 5 or 8 < inputUser < 11
print("Cara 2:", Tanda1)

print("\n\n++++0----5++++8-----11+++++")
print("Cara 1")
two = float(input("Masukkan angak : "))

sign1 = two < 0
print("Hasil pertama:", sign1)

sign2 = two > 5 and two < 8
print("Hasil kedua:", sign2)

sign3 = two > 11
print("Hasil ketiga:", sign3)

total = sign1 or sign2 or sign3
print("Hasil akhir:", total)

print("\n\nCara 2")

Tada = two < 0 or two > 5 or two < 8 or two > 11
print("Cara 2:", Tada)

# Break

# contoh 1

angka = 0
print("Menghitung angka sampai 3\n")

while angka < 5:
    angka += 1
    print(f"Angka {angka}")

    if angka == 3:
        print("ketemu")
        break
print("Akhir dari program\n")

# contoh 2

data_int = int(input("Hitung angka "))
nomor = 0

while True:
    nomor += 1
    print(nomor)

    if nomor == data_int:
        break
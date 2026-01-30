# Perulangan For

# Dengan list

print("\n==============================")
print("          Dengan list           ")
print("==============================\n")

angka2 = [0,1,2,3,4]
print(angka2)

for i in angka2:
    print(f"i sekarang -> {i}")

'''
    jika seperti itu i setiap perulangannya akan memiliki nilai dari angka2 seiring bertambahnya perulangan
    dan akan berhenti jika variabel sudah memiliki semua nilai dari data
'''
print("\n\nContoh K\n\n")

angka1 = [5,6,7,8,22]
for k in angka1:
    print(f"k sekarang -> {k}")

print("\n\nAkhir dari program\n")

print("\n========================")
print("       Dengan range       ")
print("========================\n")

'''
    jika menggunakan range ada beberapa cara.
    salah satunya
'''

contoh = range(4,8) # menaruh range di variabel data
# jika range(1,8) range akan dimulai dari 1 dan berhenti sebelum 8. bisa digunakan untuk 

for i in contoh:
    # dengan ini selalu dihitung mulai dari 0 sampai satu angka sebelum target
    print(f"i sekarang -> {i}")

print("\nAkhir dari program\n")

print("\n=======================")
print("      Dengan string      ")
print("=======================\n")


# menggunakan str

kata = "Aku sangat menyukai malam yang sunyi"

for huruf in kata:
    print(huruf)

'''
    jika seperti ini for akan print huruf nya satu per-satu hingga selesai. cocok dikombinasikan dengan time
'''
print("\nAkhir dari program\n")
# Latihan Percabangan Kalkulator Sederhana

from sys import stderr

print("\n==============================")
print("     Kalkulator Sederhana     ")
print("==============================\n\n")

angka_1 = float(input("Masukkan angka pertama: "))
operator = input("Operator (+,-,x,/): ")
angka_2 = float(input("Masukkan angka kedua: "))

if operator == "+":
    print(angka_1 + angka_2)
elif operator == "-":
    print(angka_1 - angka_2)
elif operator == "x" or operator == "*":
    print(angka_1 * angka_2)
elif operator == "/":
    print(angka_1 / angka_2)
else:
    print(stderr, "Operation Not Valid\n")

print("\nHasil dari program")
    
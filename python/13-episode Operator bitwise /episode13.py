# operator bitwise
# (operasi masing-masing bit)

a = 7
b = 6

print("\n===== OR =====\n")
# salah satu true maka hasilnya true
c = a | b
print("nilai:", a, "binary:", format(a, "08b"))
print("nilai:", b, "binary:", format(b, "08b"))
print("C = a | b = ", c, "binary:", format(c, "08b"))

print("\n===== AND =====\n")
# salah satu false maka hasilnya false
d = a & b
print("D = a & b = ", d, "binary:", format(d, "08b"))

print("\n===== XOR =====\n")
# salah satunya true maka hasilnya true tapi jika keduanya true atau false maka hasilnya false
e = a ^ b
print("E = a ^ b = ", e, "binary:", format(e, "08b"))

print("\n===== NOT =====\n")
# di mirror kan menjadi mines dan dihitung mulai dari -1
j = ~a
print("~a = ", j, "binary:", format(j, "08b"))  # 7 menjadi -8
# not di flip dengan XOR
print("\nflip")
f = 0b000000111
g = 0b000000110
print("nilai : ", f ^ g, "binary:", format(f ^ g, "08b"))

print("\nShifting\n")

# shift right
print("Shift right")
c = a >> 1
print(
    c, "binary: ", format(c, "08b")
)  # digeser ke kanan 1 kali dan 1 yang di awal 7 menjadi hillang sehingga tersisa 2 angka 1 hasilnya adalah 3

# shift left
# kebalikan dari yang kanan
print("\nShift left")
y = 10
z = y << 2
print(z, "binary: ", format(z, "08b"))  # digeser ke kiri 2 kali

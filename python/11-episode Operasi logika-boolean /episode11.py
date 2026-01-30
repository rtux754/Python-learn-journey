# operasi logika atau boolean
# not, or, and, xor

print("==== NOT ====") # not
# not = kebalikan
# not True = False
# not False = True
a = True
b = not a
print("data a =", a)
print("\n===not===")
print("data b =", b)

print("\n==== OR ====") # or
# or = salah satu bernilai true, maka hasilnya true
a = True
b = True
c = a or b
print(a, "or", b, "=", c)
a = True
b = False
c = a or b
print(a, "or", b, "=", c)
a = False
b = True
c = a or b
print(a, "or", b, "=", c)
a = False
b = False
c = a or b
print(a, "or", b, "=", c)

print("\n==== AND ====") # and
# and = kedua nilai harus true, maka hasilnya true
a = True
b = True
c = a and b
print(a, "and", b, "=", c)
a = True
b = False
c = a and b
print(a, "and", b,'=', c)
a = False
b = True
c = a and b
print(a, "and", b,"=", c)
a = False
b = False
c = a and b
print(a, "and", b, "=", c)

print("\n=== XOR ===") # (^)
# akan true jika salah satunya true, sisanya false
a = True
b = True
c = a ^ b
print(a, "XOR", b, c)
a = True
b = False
c = a ^ b
print(a, "XOR", b, c)
a = False
b = True
c = a ^ b
print(a, "XOR", b, c)
a = False
b = False
c = a ^ b
print(a,"XOR", b, c )
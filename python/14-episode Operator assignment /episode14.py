# operasi yang dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assignment

# operator penugasan memberikan tugas pada variabel. biasanya untuk mengisi nilai
# pengisian nilai (=)
# pengisian dan penambahan (+=)
# pengisian dan pengurangan (-=)
# #pengisian dan perkalian (*=)
# pengisian dan pembagian (/=)
# pengisian dan eksponen (**=)
# pengisian dan sisa bagi (%=)
# pengisian dan floor division (//=)
# pengisian dan AND (&=)
# pengisian dan OR (|=)
# pengisian dan XOR (^=)
# pengisian dan shift right (>>=)
# pengisian dan shift left (<<=)

print("----- Penugasan Dasar -----\n\n")
a = 9  # ini adalah assignment
a += 1  # pengisian dan penambahan
print("a += :", a)

a -= 1  # pengisian dan pengurangan
print("a -= :", a)

a *= 2  # pengisian dan perkalian
print("a *= :", a)

a /= 4  # pengisian dan pembagian
print("a /= :", a)

a = 10
a **= 2  # pengisian dan eksponen
print("a **= :", a)

a %= 2  # pengisian dan sisa bagi
print("a %= :", a)

a = 20
a //= 2  # pengisian dan floor division
print("a //= :", a)

print("\n\n----- Penugasan bitwise -----\n\n")
c = True
print("c = ", c)
c &= False
print("c &= :", c)

b = False
print("b = ", b)
b |= True
print('b |= : ', b)

d = False
print('d = ', d)
d ^= True
print('d ^= : ', d)

# shift
print("\n\n --- Shift --- \n")
print('\n\n --- Right --- \n')
j = 0b0100
print('nilai j : ', j, format(j, '04b'))
j >>= 2
print('nilai j : ', j, format(j, '04b'))

print('\n\n --- Left --- \n')
f = 0b0010
print('nilai f : ', f, format(f, '04b'))
f <<= 2
print('nilai f : ', f, format(f, '04b'))
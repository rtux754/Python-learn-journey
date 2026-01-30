# operasi komparasi

# setiap hasil dari operasi komparasi adalah boolean

# >,<,>=,<=,==,!=,is,is not

print('\nLEBIH BESAR DARI\n')
a = 4
b = 2

# lebih besar dari >
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = a > 5
print(a,'>',5,'=',hasil)
hasil = b > 5
print(b,'>',5,hasil)
hasil = b > 1
print(b,'>',1,hasil)

#a = int(input('Masukkan : ')) # jika ingin seperti ini 
#hasil = a > 5
#print(a,'>',5,'=',hasil)

print('\nLEBIH KECIL DARI\n')
f = 9
p = 4

# lebih kecil dari
hasil = f < 13
print(f,'<',13,hasil)
hasil = f < 8
print(f,'<',8,hasil)
hasil = p < 6
print(p,'<',6,hasil)
hasil = p < 3
print(p,'<',3,hasil)

#a = int(input('masukkan : '))
#hasil = a < 8
#print(a,'<',8,hasil)

print('\nLEBIH BESAR SAMA DENGAN\n')
# lebih besar sama dengan >=
# jika pada lebih besar dari 2 > 2 = false, disini = true karena dia benar benar menghitung dari 2 tidak dari 2 lebih sedikit
i = 4
j = 3

hasil = i >= 4
print(i,'>=',4,hasil)
hasil = i >= 5
print(i,'>=',5,hasil)
hasil = j >= 2
print(j,'>=',2,hasil)
hasil = j >= 4
print(j,'>=',4,hasil)


print('\nLEBIH KECIL SAMA DENGAN\n')
# lebih kecil sama dengan <=

i = 4
j = 3

hasil = i <= 4
print(i,'<=',4,hasil)
hasil = i <= 5
print(i,'<=',5,hasil)
hasil = j <= 2
print(j,'<=',2,hasil)
hasil = j <= 4
print(j,'<=',4,hasil)

print('\nSAMA DENGAN\n')
# sama dengan ==

o = 5
y = 6

hasil = o == 5
print(o,'==',5,hasil)
hasil = o == 6
print(o,'==',6,hasil)
hasil = y == 6
print(y,'==',6,hasil)
hasil = y == 5
print(y,'==',5,hasil)

print('\nTIDAK SAMA DENGAN\n')
# tidak sama dengan !=

o = 5
y = 6

hasil = o != 5
print(o,'!=',5,hasil)
hasil = o != 6
print(o,'!=',6,hasil)
hasil = y != 6
print(y,'!=',6,hasil)
hasil = y != 5
print(y,'!=',5,hasil)

# komparasi 
# >< >= <= == != dapat bekerja pada syntaks literal
# is membandingkan memori objek
# a = 4
# a ada nilainya dan memakan memori
# 4 adalah literal, tidak ada nilainya dan tidak memakan memori

# a is 4 tidak bisa
# is dan is not hanya bisa pada variabel yang ada nilainya
# a = 4
# b = 4
# a is b = true ini bisa
print('\nIS\n')
# is
a = 4
b = 4
hasil = a is b
print('a dengan b',hasil)# true karena nilai a dan b sama sama 4

print('\nIS NOT\n')
# is not
a = 4
b = 4
hasil = a is not b
print('a dengan b',hasil)# false karena nilai a dan b sama sama 4
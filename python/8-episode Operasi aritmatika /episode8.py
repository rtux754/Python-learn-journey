# Operasi Aritmatika

# prioritas operasi
print('\n===PRIORITAS OPERASI===\n')
print('1. () \n 2.eksponen\n 3.perkalian\n   pembagian\n   modulus\n   floor division\n 4.pertambahan dan pengurangan\n')

print('===Operasi Aritmatika===')

a = 8
b = 14
c = 35
d = 12
e = 3

# operasi tambah
print('\n===PENJUMLAHAN===\n')

hasil = a + b + c
print('a b c = ',hasil)

# operasi pengurangan
print('\n===PENGURANGAN===\n')
hasil = a - b - c
print('a b c = ',hasil)

# operasi pembagian
print('\n===PEMBAGIAN===\n')
hasil = a / b / c
print('a / b / c = ',hasil)

# operasi perkalian
print('\n===PERKALIAN===\n')
hasil = a * b * c
print('a * b * c = ',hasil)

# operasi eksponen (pangkat)
print('\n===EKSPONEN===\n')
hasil = a ** b  # tidak bisa lebih dari dua data
print('a ** b = ',hasil) # jika lebih dari dua maka tidak akan ada output apapun

# operasi modulus (sisa pembagian)
print('\n===MODULUS===\n')
hasil =  d % e # walaupun ada tiga data tetapi dia hanya akan mengeluarkan hasil dari dua data awal
print('d e = ',hasil) # jika jumlah pembagiannya pas maka hasil nya akan 0 tapi jika tidak maka angka lain selian 0 yang keluar

# operasi floor division (kebalikan dari modulus) dia adalah hasil pembagian yang dibulatkan atau bisa dibilang hasil float dirubah menjadi integer
print('\n===FLOOR DIVISION===\n')
hasil = b // c # sama halnya dengan modulus hanya dua angka yang keluar walaupun ada tiga data
print('b // c = ',hasil)

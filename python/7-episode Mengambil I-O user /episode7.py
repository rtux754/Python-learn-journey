# Mengambil Input Data Dari User

# output dari input pasti string
print('\n===SRTING===\n')
data = input('Input : ')
print('output = ',data,'type = ',type(data))

# jika ingin mengubahnya menjadi data lain rumusnya seperti ini

print('\n===INTEGER===\n')
data_int = int(input('Masukkan : '))
print('output = ',data_int,'type = ',type(data_int))

# bisa dirubah menjadi data lain

print('\n===FLOAT===\n')
data_float = float(input('FLOAT : '))
print('output = ',data_float,"type = ",type(data_float))

print('\n===BOOLEAN===\n')
bol = bool(int(input('BOOL : ')))  #untuk boolean agar bisa menjadi false harus dirubah dulu ke integer
print('output = ',bol,'type = ',type(bol))# jadi input nya harus variabel agar tidak eror
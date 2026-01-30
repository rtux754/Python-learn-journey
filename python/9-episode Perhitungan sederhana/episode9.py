# konversi satuan suhu
print('\n===KONVERSI SATUAN SUHU===\n')
print('\nRumus Konversi Suhu\n')
print('              celcius       reamur       fahrenheit    kelvin  ')
print('celcius                     4/5C         9/5C+32       C+233   ')
print('reamur        5/4R                       9/4R+32       5/4R+273')
print('fahrenheit    5/9(F-32)     4/5(F-32)                          ')
print('kelvin        K-273         4/5(K-273)                       \n')

# konversi celcius ke satuan lain
print('KELVIN\n')
celcius = float(input('Masukkan suhu dalam celcius : '))
print('suhu adalah ',celcius,'celius')

# reamur
# (5/4)*C
reamur = (5/4)*celcius
print('suhu dalam raemur adalah ',reamur)

# fahrenheit
# ((9/5)* C) + 32
fahrenheit = ((9/5)* celcius) + 32
print('suhu dalam fahrenheit adalah',fahrenheit)

# kelvin
# C + 273
kelvin = celcius + 273
print('suhu dalam kelvin adalah',kelvin)
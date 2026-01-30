# Tugas Konversi Satuan Suhu
print('Tugas Konversi Satuan Suhu\n')
print('Fahrenheit\n')
F = float(input('Masukkan suhu dalam Fahrenheit '))
print('suhu dalam fahrenheit ',F)
C = 5/9 * (F-32)
print('suhu dalam celcius ',C)
K = C + 273
print('suhu dalam kelvin ',K,'\n')

print('Kelvin\n')
Kl = float(input('Masukkan suhu dalam kelvin '))
print('suhu dalam kelvin ',Kl)
Cl =  Kl - 273
print('suhu dalam celcius ',Cl)
Fh = ((9/5) * Cl) + 32
print('suhu dalam fahrenheit ',Fh)

#print('\nVersi Singkat')
#Fh = float(input('Masukkan fahrenheit yang ingi di ubah ke kelvin '))
#Ce = 5/9 * (Fh-32)
#kl = Ce + 273
#print(kl,'kelvin')
#
#print('\nVersi Singkat')
#Kl = float(input('masukkan kelvin yang ingin dirubah dalam fahrenheit '))
#Ce = Kl-273
#Fh = 9/5 * Ce + 32
#print(Fh,'fahrenheit')

kelvin = float(input('masukkan suhu : '))

fahrenheit = ((kelvin - 273) * (9/5) + 32)
print('suhu ',kelvin,'kelvin dalam fahrenheit = ',fahrenheit)
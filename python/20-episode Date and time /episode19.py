# date and time (latihan) library

import datetime as dt

data_hari = dt.date.today()
print(data_hari)
print(f"hari ini berdasarkan tanggal : {data_hari:%A}") # bisa melakukan ini untuk mengetahui hari sesuai tanggal nya

'''
    ada juga cara pengisian secara manual seperti berikut
'''

tanggal = dt.date(2021,10,10)
print(tanggal)
print(f"hari ini berdasarkan tanggal : {tanggal:%A}")

'''
    meminta input tanggal, bulan dan tahun lahir dari user
'''

print("\n" + 5 * "=" + "Meminta input" + "=" * 5)

hari = int(input("Tanggal lahir anda : "))
bulan = int(input("Bulan lahir anda   : "))
tahun = int(input("Tahun lahir anda   : "))

tanggal_lahir = dt.date(tahun,bulan,hari)
print("\nTanggal lahir anda :",tanggal_lahir)
print(f"Harinya adalah     : {tanggal_lahir:%A}")

print("========================")
print("  Menghitung umur anda  ")
print("========================")

# menghitung tanggal lahir user
hari_ini = dt.date.today()
print(f"hari ini tanggal : {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
print(f"Hari ini adalah  : {tanggal_lahir:%A}")
print("Umur anda adalah :",umur_tahun,"tahun",",",umur_bulan_sisa,"bulan")
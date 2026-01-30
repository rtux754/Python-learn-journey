# tugas redirection code
print("konversi satuan suhu")
fahren = float(input("masukkan suhu dalam fahrenheit: "))
kelvin = ((5/9) * (fahren - 32)) + 273
print("suhu dalam kelvin adalah: ", kelvin)

kelvin = float(input("masukkan suhu dalam kelvin: "))
fahren = ((9/5) * (kelvin - 273)) + 32
print("suhu dalam fahrenheit adalah: ", fahren)
# format string


'''
    contoh genreic
'''

'''

nama = "Rozzaq"
contoh = "Hello " + nama
print(contoh)

    ini terlalu panjang, lebih baik seperti ini saja
'''

# string
nama = "ucup"
pertanyaan = ", apa kabar?"
format_str = f"Hello {nama}{pertanyaan} mau mampir kerumah?"
print(format_str)

'''
    yang seperti ini sangat rapih dan efisien.
    cara seperti ini juga bisa digunakan untuk casting tipe data ke str dengan lebih mudah.
'''

# boolean
bole = True
format_str = f"Boolean = {bole}"
print(format_str)

# angka

'''
    contoh awal


angka = 20.16
print("angka = " + str(angka))

'''

'''
    cara ini tidak efisien, lakukan seperti ini
'''

# float
angka = 20.5
format_str = f"angka = {angka}"
print(format_str)

'''
    cara seperti di atas jauh lebih efisien
    untuk bilangan bulat ada caranya tersendiri
'''

# integer
angka = 15
format_str = f"bilangan bulat = {angka:d}" # tambahkan :d untuk memberi tahu jika itu adalah bilangan bulat, tetapi tidak diberi juga tidak masalah

# bilangan ribuan dan jutaan

'''
    ada trick yang mempermudah untuk memberikan koma pada angka ribuan dan jutaan
'''

ribuan = 2000
jutaan = 2000000
format_str = f"ribuan = {ribuan:,}"
print(format_str)
format_str = f"jutaan = {jutaan:,}"
print(format_str)

'''
    trick untuk menampilkan 2 angka dibelakang koma
'''

# desimal
flut = 23.8346
format_str = f"desimal = {flut:.2f}" # . menandakan desimalnya lalu 2 menandakan mengambil 2 angka di belakang . dan f untuk float
print(format_str)

# menampilkan leading zero atau di depan koma ada berapa angka
flut = 23.8346
format_str = f"leading zero = {flut:06.2f}" # 5 menandakan jumlah output angka yang dimiliki
print(format_str)

'''
    jika yang berada di posisi 5 adalah 6 maka di depannya akan diisi "kosong" lalu jika kita menambahkan 0  di depan posisi 6
    maka "kosong" pada 6 akan diisi oleh 0
'''

# menampilkan tanda + atau -

angka_minus = -21
angka_plus = 21
format_minus = f"minus = {angka_minus:+d}" # tambahkan + untuk menampilkan tandanya d disesuaikan dengan tipedanya
format_plus = f"plus = {angka_plus:+d}" # (:+.2f)
print(format_minus)
print(format_plus)

# format persen
persen = 0.045
format_persen = f"persen = {persen:.2%}" # bisa ditambahkan (:.2%) untuk menampilkan 2 angka dibelakang koma saja
print(format_persen)

'''
    didalam placeholder juga bisa dilakukan operasi penjumlahan
'''

##

harga = 15000
jumlah = 5
formater = f"harga = Rp{harga * jumlah:,}"
print(formater)

# angka lain (binary, octal, hexadecimal)

angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"
print(format_binary)
print(format_octal)
print(format_hex)
# operasi dan manipulasi string

# 1. menyambung string (conctenate)

'''
    Part 1
'''


nama_awal = "Alif"
nama_tengah = "Khotibul"
nama_akhir = "Umam"

nama_lengkap = nama_awal+ " " + nama_tengah + " " + nama_akhir
print("Nama : ",nama_lengkap)

# 2. menghitung panja
# ng string
panjang = len(nama_lengkap)
print("Panjang nama: ",panjang)
print("Panjang nama " + nama_lengkap + " = " + str(panjang))

# 3. mengecek apakah ada komponen string atau char di string
i = "l"
status = i in nama_lengkap
print(i + " ada di " + nama_lengkap + " = " + str(status))

k = "L"
status = k not in nama_lengkap
print(k + " tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string

print("GG " * 10)
print(15 * "wk")

# indexing
print("index ke-5 : " + nama_lengkap[5])
print("index ke-(-1) : " + nama_lengkap[-1]) # mengambil dari belakang
print("indedx ke-[0:3] : " + nama_lengkap[0:3]) # 0 sampai sebelum 4
print("index ke-[0,2,4,6,8,10] : " + nama_lengkap[0:11:2]) # 0 sampai sebelum 11 dengan diloncati 2

# item paling kecil
print("paling kecil : " + min(nama_lengkap) + " < (yang kosong ini adalah spasi)")

# item paling besar
print("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("ASCII code untuk 117 adalah " + chr(data))

# 4. operator dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o pada " + data + " = " + str(jumlah))

'''
    batas part 1
'''

print("=======================")
print("        Part 2         ")
print("=======================")

'''
    Part 2
'''

## merubah case dari string

# merubah semua ke upper case

salam = "bro!"
nama = "Miftahur Rozzaq"
print("normal = " + salam + nama)

salam = salam.upper()
nama = nama.upper()
print("upper = " + salam + nama)

# merubah semua ke lower case

aku = "roZZaq"
print("normal = " + aku)

aku = aku.lower()
print("lower = " + aku)

## pengecekan dengan isX method

# pengecekan lower case
salam = "halo"
apakah_lower = salam.islower() # hasilnya bool
print("apakah " + salam + " is lower = " + str(apakah_lower))

# pengecekan upper case
salam = "HALO"
apakah_upper = salam.isupper()
print("apakah " + salam + " is upper = " + str(apakah_upper))

# mengecek semuanya huruf

alpa = "nama1"
apakah_alpha = alpa.isalpha()
print(alpa + " is alpha = " + str(apakah_alpha))

# mengecek huruf dan angka
apakah_alnum = alpa.isalnum()
print(alpa + " is alnum = " + str(apakah_alnum))

# mengecek angka saja
angka = "123"
apakah_desimal = angka.isdecimal()
print(angka + " is decimal = " + str(apakah_desimal))

# mengecek apakah spasi, tab, newline \n
spasi = " "
apakah_spasi = spasi.isspace()
print("apakah data spasi isspace = " + str(apakah_spasi))

# mengecek semua kalimat dimulai dengan huruf besar
titl = "Aku Sangat Jago"
apakah_title = titl.istitle()
print(titl + " is title = " + str(apakah_title))

## mengecek komponen

# komponen awal
cek = "Aku Kamu".startswith("Aku") # operasi bisa dilakukan seperti ini agar lebih mudah
print("start = " + str(cek))

# komponen akhir
cek_akhir = "Aku Kamu".endswith("Kamu")
print("end = " + str(cek_akhir))

# penggabungan komponen

list = ["Aku", "Sayang", "Kamu"]
print("normal = ", list, type(list))
gabungan = " ".join(list)
print(gabungan)

gabungan = "Aku Sayang Kamu"
print(gabungan, type(gabungan))

print(gabungan.split(" ")) # kembali menjadi list

## alokasi karakter
'''
contoh singkatnya:
    print(18 *"=" + "Data" + "=" * 18)
bisa membuat si "Data" berada di sebuah posisi tampa harus menggunakan cara seperti itu
'''

# rjust()
kanan = "kanan".rjust(19)
print("'" + kanan + "'") # tanda '' untuk menunjukkan batas karakter

# ljust
kiri = "kiri".ljust(19)
print("'" + kiri + "'")

'''
    kita bisa menambahkan argumen dibelakang angka, agar karakter spasi dapat digantikan
'''

# center()
tengah = "tengah".center(23,"-")
print("'" + tengah + "'")

'''
    strip(), ini adalah kebalikan dari ketiga command di atas. strip() berguna untuk menghilangkan karakter yang ditambahkan
'''

# strip()
tengah = tengah.strip("-")
print("'" + tengah + "'")

'''
    untuk spasi argumennya tidak perlu diisi
'''
kanan = kanan.strip()
print("'" + kanan + "'")

kiri = kiri.strip()
print("'" + kiri + "'")

'''
    Batas part 2
'''

'''   Masih banyak method yang ada dan aku menemukan beberapa di kolom komentar   '''

'''

Contoh metode lain :


1) capitalize() <-- Membuat karakter pertama di string menjadi uppercase

tes_capitalize = "ayam goreng enak"

cek_hasil = tes_capitalize.capitalize()

print(cek_hasil)


tes_capitalize = "AYAM GORENG ENAK"

cek_hasil = tes_capitalize.capitalize()

print(cek_hasil)

------> Hasil keduanya : Ayam goreng enak


2) casefold() <-- sama dengan lower()

bedanya, casefold() mengkonversi karakter tidak umum menjadi lowercase karakter umum

Contoh  : 'ß' (german) = menjadi 'ss'


tes_casefold = "außen IS AN GERMAN WORD"

cek_hasil = tes_casefold.casefold()

print(cek_hasil)

------> Hasil : aussen is an german word



3) swapcase() <-- Uppercase jadi lowercase dan kebalikannya

tes_swapcase = "Ayam Goreng Suharti"

cek_hasil = tes_swapcase.swapcase()

print(cek_hasil)

------> Hasil : aYAM gORENG sUHARTI



4) expandtabs () <-- Mengatur lebar tab (\t)

tes_expandtabs = "Ayam\tGoreng\tSuharti"

cek_hasil = tes_expandtabs.expandtabs(10)

print(cek_hasil)

------> Hasil : Ayam      Goreng    Suharti

'''

'''

Metode (Method) in  Pyhton
count() | Mengembalikan jumlah kemunculan nilai tertentu dalam string
encode() | Mengembalikan versi encoded dari string
find() | Mencari nilai tertentu dalam string dan mengembalikan posisi kemunculannya
format() | Memformat nilai-nilai ke dalam string
format_map() | Memformat nilai-nilai yang ditentukan ke dalam string
index() | Mencari nilai dalam string dan mengembalikan posisi kemunculannya
isdigit() | Mengembalikan True jika semua karakter dalam string adalah digit
isidentifier() | Mengembalikan True jika string merupakan identifier yang valid
isnumeric() | Mengembalikan True jika semua karakter dalam string adalah angka
isprintable() | Mengembalikan True jika semua karakter dalam string dapat dicetak

'''
# Continue and pass

# Pass. berfungsi sebagai dummy, tidak akan dieksekusi

angka = 0

while angka < 5:
    angka += 1
    if angka == 3:
        pass
    print(angka)

# contoh lain
def fungsi():
    pass

class Hero():
    pass

'''
    pass sering digunakan pada fungsi atau class.
    pass membuat mereka tidak akan dihiraukan.
    mereka ada tapi tidak diimplementasikan.
'''

# Continue

nomor = 0

while nomor < 5:
    nomor += 1
    print(f"Nomor saat ini {nomor}") # aksi 1

    if nomor == 3:
        print("ini if")
        continue # memubuat program akan loncat kembali ke awal
    # aksi dua akan diloncatin
    print("Halo") # aksi 2

print("Akhir dari program")

'''
    penjelasan singkat:
    apapun yang berada di bawah continue akan dilewati
    sering di temukan pada while. ini seperti looping kecil yang berada di dalam looping
    tapi bukan nestedloop
'''

data = "ini adalah string"
print(data)
print(type(data))


# 1. cara membuat string


'''
    1. Dengan single quote
'''

data = "dibuat dengan single quote"
print(data)
print(type(data))

'''
    2. Dengan double quote
'''

data = "dibuat dengan double quote"
print(data)
print(type(data))

# bisa juga seperti ini
print('"Ini akan terus berlanjut", ujar si lelaki') # kalimat langsung dalam pelajaran bahasa Indonesia
print("'Ini akan terus berlanjut', ujar si lelaki")

'''
    3. Dengan \
'''

# membuat tanda ' menjadi string
print('ini hari jum\'at')
print('g\'day, isn\'it?')

# backslash
print("Home\\fenrir\\Downloads")

# tab
print("ucup \totong, jauhan")

# backspace
print("ucup \botong, deketan")

# newline
print("Baris pertama. \n baris kedua.") # LF -> line feed -> unix, macos, linux
print("Baris pertama. \r baris kedua.") # CR -> carriage return -> commodore, acorn, lips
print("Baris pertama.\r\nbaris kedua.") # CRLF -> line feed carriage return -> windows

'''
    4. String literal atau raw
'''

''' Warning!!! '''
print("Home\new folder") # akan salah

'''
    jika punya banyak \\ pada path yang dimiliki bisa menggunakan cara dibawah biar lebih mudah
'''

# menggunakan string raw
print(r'Home\fenrir\Downloads') # dengan menggunakan ini (r) semua yang ada didalam dianggap string

# multiline literal string
print("""
Nama : Yanto
Kelas": 5 SD
""")

# multiline literal string dan raw
print(r"""
Home\fenrir\Downloads
Home\fenrir\Documents
""")
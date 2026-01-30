## width and multiline


# data
nama = "Rozzaq"
umur = 17
kelas = "IX-4"

print("\n" + 5 * "=" + "Multiline enter" + "=" * 5)
# string multiline dengan \n
data_string = f"nama = {nama}\numur = {umur}\nkelas = {kelas}"
print(data_string)

# string multiline dengan triplets
print("\n" + 5 * "=" + "Multiline triplets" + "=" * 5)
data_string = f"""
nama  = {nama:>6}
umur  = {umur:>6}
kelas = {kelas:>6}
"""
print(data_string)

'''
    bisa ditambahkan :>{ukuran data yang dimiliki} agar outputnya rata ke kanan semua biar rapih
'''


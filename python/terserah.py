def tambah(a,b):
    return a + b

def kurang(a,b):
    return a - b

def kali(a,b):
    return a * b

def bagi(a,b):
    return a / b

def sisa_bagi(a,b):
    return a % b

def kalkulator():
    print("== kalkulator sederhana ==\n")
    print("Pilih Operasi:")
    print("1. Tambah(+)")
    print("2. Kurang(-)")
    print("3. Kali(*)")
    print("4. Bagi(/)")
    print("5. Sisa bagi(%)")

    pilihan = input("\nMasukkan pilihan anda(1/2/3/4/5): ")

    if pilihan in('1','2','3','4','5'):
        try:
            num1 = float(input("Masukkan angka pertama: "))
            num2 = float(input("Masukkan angka kedua: "))
        except ValueError:
            print("Input harus berupa angka!")
            return
        
        if pilihan == '1':
            print(f"Hasil: {num1} + {num2} = {tambah(num1, num2)}")
        elif pilihan == '2':
            print(f"Hasil: {num1} - {num2} = {kurang(num1, num2)}")
        elif pilihan == '3':
            print(f"Hasil: {num1} * {num2} = {kali(num1, num2)}")
        elif pilihan == '4':
            print(f"Hasil: {num1} / {num2} = {bagi(num1, num2)}")
        elif pilihan == '5':
            print(f"Hasil: {num1} % {num2} = {sisa_bagi(num1, num2)}")
    else:
        print("Pilihan tidak valid.")
        
    
# menjalankan kalkulator
if __name__ == "__main__":
    kalkulator()
            
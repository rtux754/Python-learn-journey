import time
import sys

def tulis(teks):
    for karakter in teks:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(0.2)
    print()

tulis("\n\tDesember")
time.sleep(2)
tulis("\nAku Kalah Dari Hujan Di Bulan Desember.")
time.sleep(1.5)
tulis("Januari!")
time.sleep(1)
tulis("Kau Menang....\n")
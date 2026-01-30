import sys
import time

def efek_ngetik(teks):
    for karakter in teks:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

efek_ngetik("\n\tJanuari\n")
time.sleep(1)
efek_ngetik("Januari!")
time.sleep(2)
efek_ngetik("Ini Yang Terakhir,,")
time.sleep(2)
efek_ngetik("Bulan Itu Indah, Bukan?\n")
time.sleep(3)
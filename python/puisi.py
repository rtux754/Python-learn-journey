#import time
#
#print("\n\tGarnet\n")
#time.sleep(2)
#print("Kalian menang.")
#time.sleep(1.5)
#print("Aku pecundang!")

import time 
import sys

def efek_ngetik(teks):
    for karakter in teks:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

# efek_ngetik("\n\tGarnet")
# time.sleep(1)
# efek_ngetik("\nJanuari?")
# time.sleep(2)
# efek_ngetik("Nama-mu Sangat Indah,")
# time.sleep(1.6)
# efek_ngetik("Senyum-mu, Tawa-mu...")
# time.sleep(2)
# efek_ngetik("Sangat Benar-benar Indah.")
# time.sleep(1.2)
# efek_ngetik("Kumohon.....")
# time.sleep(1.4)
# efek_ngetik("Genggam Erat Tangan-ku!")
# time.sleep(0.5)
# efek_ngetik("\nBulannya Indah, Kan, Januari?\n")

# efek_ngetik("Kangen Genshin Woilah")
# time.sleep(1)
# efek_ngetik("........")
# time.sleep(0.05)
# efek_ngetik("Bajing")

efek_ngetik("Admin mau mandi dulu")
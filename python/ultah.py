import sys
import time
import os

def clear_screen():
    # Membersihkan layar
    os.system('cls' if os.name == 'nt' else "clear")

def typewriter_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def birthday_gift():
    clear_screen()

    # Animasi pembuka
    typewriter_effect(">> Menginisialisasi modul kebahagian...", 0.03)
    typewriter_effect(">> Memuat memori tahun lalu...", 0.03)
    typewriter_effect(">> Menyiapkan kejutan untukmu...", 0.03)
    time.sleep(1)

    # ASCII Art Kue Ulang Tahun
    cake = """
           * * * *     * * * *
          | |   | |   | |   | |
        |~~~~~~~~~~~~~~~~~~~~~~~|
        |      HAPPY BIRTHDAY   |
      |~~~~~~~~~~~~~~~~~~~~~~~~~~~|
      |          12-01-2026       |
      |         -----------       |
      |~~~~~~~~~~~~~~~~~~~~~~~~~~~|
    """    
    print(cake)

    # Pesan Spesial
    typewriter_effect("Halo Teman! 👋", 0.1)
    print("-" * 30)
    typewriter_effect("Selamat ulang tahun yang ke-sekian!", 0.07)
    typewriter_effect("Semoga kode-kodemu selalu bebas bug,", 0.06)
    typewriter_effect("Logikamu selalu tajam seiring bertambahnya usia,", 0.06)
    typewriter_effect("Dan semoga impian-impian besarmu segera ter-compile dengan sukses!", 0.06)
    print("-" * 30)

    # Interaksi sederhana
    input("\nTekan [ENTER] untuk meniup lilin...")

    print("\n*FIUUUUUUUU~* 🕯️💨")
    time.sleep(1)
    print("\nSelamat! Semoga harimu menyenangkan hari ini! 🎉✨")

if __name__ == "__main__":
    birthday_gift()
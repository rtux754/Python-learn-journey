#!/usr/bin/env python3
import subprocess
import datetime
import os

# Nama file log
LOG_FILE = "acchan_debug_log.txt"

# Kata kunci yang akan memicu notifikasi desktop
KEYWORDS_TO_NOTIFY = ["Error", "Warning", "Failed", "mismatched tag", "Not Responding"]

def send_notification(message):
    """Mengirim notifikasi ke desktop Linux menggunakan notify-send"""
    try:
        # Menjalankan perintah notify-send
        subprocess.run(["notify-send", "Nyarch Monitor Alert", message])
    except Exception as e:
        print(f"Gagal mengirim notifikasi: {e}")

def run_and_log():
    print(f"--- Memulai Monitoring Acchan dengan Notifikasi ---")
    print(f"Log disimpan di: {os.path.abspath(LOG_FILE)}")
    
    # Perintah untuk menjalankan Nyarch Assistant
    cmd = ["flatpak", "run", "moe.nyarchlinux.assistant"]

    try:
        with open(LOG_FILE, "a") as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"\n\n--- SESI BARU: {timestamp} ---\n")
            
            # Menjalankan proses Nyarch Assistant
            process = subprocess.Popen(
                cmd, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT, 
                text=True
            )

            # Membaca output baris demi baris
            for line in process.stdout:
                print(line, end="") # Tampilkan di terminal
                f.write(line)      # Tulis ke file log
                f.flush()

                # Cek apakah ada kata kunci error di baris ini
                for word in KEYWORDS_TO_NOTIFY:
                    if word.lower() in line.lower():
                        # Kirim notifikasi jika ditemukan
                        send_notification(f"Terdeteksi: {word}")
                        break # Stop cek kata kunci lain di baris yang sama

            process.wait()
    except KeyboardInterrupt:
        print("\nMonitoring dihentikan oleh user.")
    except Exception as e:
        print(f"Terjadi kesalahan pada skrip: {e}")

if __name__ == "__main__":
    run_and_log()
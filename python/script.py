import os
import datetime
import subprocess

# Nama file log
LOG_FILE = "debug_log.txt"

# Kata kunci yang akan memimcu notifikasi
KEYWORD_TO_NOTIFY = ["Error", "Warning", "Failed", "mismatched tag", "Not Responding"]

def send_notification(message):
    """Mengirim notifikasi ke desktop"""
    try:
        # Menjalankan perintah send
        subprocess.run(["notify-send", message])
    except Exception as e:
        print(f"Gagal mengirim notifikasi: {e}")

def run_and_log():
    print(f"--- Memulai Monitoring Acchan dengan Notifikasi ---")
    print(f"Log disimpan di: {os.path.abspath(LOG_FILE)}")

    # Perintah menjalankan 
    cmd = ["flatpak", "run", "moe.nyarchlinux.assistant"]

    try:
        with open(LOG_FILE, "a") as f:
            timestamp = datetime.datetime.now("%Y-%m-%d %H:%M:%S")
            f.write(f"\n\n--- SESI BARU: {timestamp} ---\n")

            # Menjalankan proses
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )

            # Membaca output baris demi baris
            for line in process.stdout:
                print(line,end="")
                f.write(line)
                f.flush()

                # Cek apakah ada kata kunci error
                for word in KEYWORD_TO_NOTIFY:
                    if word.lower() in line.lower():
                        send_notification(f"Terdeteksi: {word}")
                        break

            process.wait()
    except KeyboardInterrupt:
        print("\nMonitoring dihentikan oleh user.")
    except Exception as e:
        print(f"Terjadi kesalahan pada skrip: {e}")

if __name__ == "__main__":
    run_and_log()
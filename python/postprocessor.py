import yt_dlp

def download_mp3(url):
    # konfigurasi opsi untuk yt_dlp
    ydlp_opts = {
        'format': 'bestaudio/best',
        # lokasi penyimpanan dan template nama file
        'outtmpl': '%(title)s.%(ext)s',
        # mengubah file ke mp3
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192' # kualitas bitrate [192, 256, 320]
        }],
    }

    with yt_dlp.YoutubeDL(yt_dlp) as ydl:
        ydl.download([url])

# eksekutor file
if __name__ == "__main__":
    video_url = input("Enter Youtube URL: ")
    download_mp3(video_url)
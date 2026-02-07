import yt_dlp
# from tqdm import tqdm 
# import time

def download_yt_video(url):
    # pencari
    ydl_opts = {
        'format': 'bestvideo[height<=1000]',
        'noplaylist': True
    }

    # pengunduh
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# eksekutor
if __name__ == "__main__":
    # meminta input saat dijalankan
    video_url = input("Enter the Youtube Video URL: ")
    download_yt_video(video_url)

# for i in tqdm(range(100)):
    # time.sleep(0.02)

"""
    yang ku komen coba sendiri library nya tapi jangan dijadikan satu sama yang disini
    karena sia-sia
"""
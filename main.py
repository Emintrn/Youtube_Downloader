import yt_dlp

url = input("enter video url: ").strip()

yt_dlp.YoutubeDL().download([url])

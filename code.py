from pytube import YouTube
import os

url = "https://www.youtube.com/watch?v=xCe9wnBjIcs"
yt = YouTube(url)

### Download formato .mp4 (Vídeo) do YouTube ###
video = yt.streams.get_highest_resolution()
video.download()

print(yt.title + " has been successfully downloaded.")

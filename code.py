from pytube import YouTube
import os

url = "https://www.youtube.com/watch?v=xCe9wnBjIcs"


yt = YouTube(url)



### Download formato .mp4 (Vídeo) do YouTube ###
video = yt.streams.get_highest_resolution()
video.download()



### Download formato .mp3 (música) do YouTube ###
audio = yt.streams.filter(only_audio=True).first()
out_file = audio.download()
# Salvando arquivo formato .mp3
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
# Retorno para confirmação
print(yt.title + " has been successfully downloaded.")

from pytube import YouTube

link = input("Inserisci link di YouTube: ")
yt = YouTube(link)

ys = yt.streams.get_highest_resolution()
ys.download()
print("Download Completato!")
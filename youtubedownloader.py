from pytube import YouTube
URL = input("Enter the Video you want to download: ")
video = YouTube(URL)

video_Streams = video.streams.filter(file_extension='mp4').get_by_itag(18)
video_Streams.download(filename= "first youtube download", output_path=".")


import pytube  
from pytube import YouTube  
video_url = ''   
Video = YouTube(video_url)
youtube = pytube.YouTube(video_url) 
video = youtube.streams.filter(res="1080p").first()  
video.download('C:/Users/user/Downloads/')

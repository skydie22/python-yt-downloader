from pytube import YouTube
from datetime import datetime

download_start_time = datetime.now()

    
def download(url):
    global download_start_time
    youtubeObject = YouTube(url)
    video = youtubeObject.streams.get_highest_resolution()
    print(f"Fetching {video.title}\"..")
    print(f"Fetching successful\n")
    print(f"Information: \n"
              f"File size: {round(video.filesize * 0.000001, 2)} MegaBytes\n"
              f"Highest Resolution: {video.resolution}\n"
              f"Author: {youtubeObject.author}")
    print("Views: {:,}\n".format(youtubeObject.views))
    print(f"Downloading \"{video.title}\"..")   
    if video != 0:
        download_start_time
        video.download()
    else:
        print("error cant download video")
        
    print("Download is completed successfully")
    

def main():
    url = input("enter youtube url: ")
    download(url)
    
    
main()
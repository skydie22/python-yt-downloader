from pytube import YouTube
from datetime import datetime
import os

download_start_time = datetime.now()

    
def download_video(url, directory):
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
        video.download(output_path=directory)
    else:
        print("error cant download video")
        
    print("Download is completed successfully")
    
def download_music(url, directory):
    youtubeObject = YouTube(url)
    video = youtubeObject.streams.filter(only_audio=True).first()
    mp3 = video.download(output_path=directory)
    base, ext = os.path.splitext(mp3)
    new_file = base + '.mp3'
    os.rename(mp3, new_file)

    print(f"Fetching {video.title}\"..")
    print(f"Fetching successful\n")
    print(f"Information: \n"
              f"File size: {round(video.filesize * 0.000001, 2)} MegaBytes\n"
              f"Author: {youtubeObject.author}")
    print("Views: {:,}\n".format(youtubeObject.views))
    print(f"Downloading \"{video.title}\"..")   
    if video != 0:
        download_start_time
        mp3
    else:
        print("error cant download video")
        
    print("Download is completed successfully")
    
    
    

def main():
    # url = input("enter youtube url: ")
    # directory = input("enter the destination folder or leave blank for current directory : >> ")
    # download(url, directory)
    print("welcome to youtube converter")
    print("2 options available:")
    print("video")
    print("audio")
    print("")
    
    options = input("")
    if options.lower() == "video":
        url = input("enter youtube url: ")
        directory = input("enter the destination folder or leave blank for current directory : >> ")
        download_video(url, directory)
    elif options.lower() == "audio":
        url = input("enter youtube url: ")
        directory = input("enter the destination folder or leave blank for current directory : >> ")
        download_music(url, directory)
    else:
        print("option not valid. please input video or audio")
        print(f"{options}")
        
    
    
main()
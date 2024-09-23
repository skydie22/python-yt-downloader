from pytube import YouTube, Playlist, Search
from datetime import datetime
import os

download_start_time = datetime.now()

def search(query):
    global download_start_time
    s = Search(query)
    videos = s.results
    for index,i in enumerate(videos[:50]):
        print(f"{index}.{i.title}")
        # print(type(videos))
    # for i in s.results:
    #     print(f"{i.title}")
    
    choise = int(input("select number from list: "))
    
    if 0 <= choise <= len(videos[:50]):
        selected_video = videos[choise]
        print(f"downloading video... {selected_video.title}")
        stream = selected_video.streams.get_highest_resolution()
        if stream != 0 :
            download_start_time
            stream.download()
            print("Download is completed successfully")
        else:
            print("error cant download video")
        

        
    # get object keys
    # keys = "\n".join([k for k in s.results[0].__dict__])
    # print(keys)

#download single video
def download_video(url, directory):
    global download_start_time
    youtubeObject = YouTube(url)
    video = youtubeObject.streams.get_highest_resoluton()
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

#download only audio file
def download_music(url, directory):
    youtubeObject = YouTube(url)
    video = youtubeObject.streams.filter(only_audio=True).first()
    mp4a = video.download(output_path=directory)
    base, ext = os.path.splitext(mp4a)
    new_file = base + '.mp4a'
    os.rename(mp4a, new_file)

    print(f"Fetching {video.title}\"..")
    print(f"Fetching successful\n")
    print(f"Information: \n"
              f"File size: {round(video.filesize * 0.000001, 2)} MegaBytes\n"
              f"Author: {youtubeObject.author}")
    print("Views: {:,}\n".format(youtubeObject.views))
    print(f"Downloading \"{video.title}\"..")   
    if video != 0:
        download_start_time
        mp4a
    else:
        print("error cant download video")
        
    print("Download is completed successfully")
    
    
def main():
    # url = input("enter youtube url: ")
    # directory = input("enter the destination folder or leave blank for current directory : >> ")
    # download(url, directory)
    
    print("welcome to youtube converter")
    print("2 options available:")
    print(f"video\naudio\nsearch")
    
    options = input("select option: ")
  
    
    if options.lower() == "video":
        url = input("enter youtube url: ")
        directory = input("enter the destination folder or leave blank for current directory : >> ")
        download_video(url, directory)
    elif options.lower() == "audio":
        url = input("enter youtube url: ")
        directory = input("enter the destination folder or leave blank for current directory : >> ")
        download_music(url, directory)
    elif options.lower() == "search":
        query = input("search: ")
        search(query)
    else:
        print("option not valid. please input video or audio")
        print(f"{options}")
        
    
    
main()
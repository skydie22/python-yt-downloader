from pytubefix import YouTube, Search
from tqdm import tqdm
from datetime import datetime
import ffmpeg
import os

download_start_time = datetime.now()
progress_bar = None

def progress_bar(video, chunk, byte_remaining):
    total_size = video.filesize
    bytes_downloaded = total_size - byte_remaining
    if progress_bar:
        progress_bar.update(len(chunk))



#download single video
# def download_video(url, directory):
#     global download_start_time
#     youtubeObject = YouTube(url)
#     video = youtubeObject.streams.get_highest_resoluton()
#     print(f"Fetching {video.title}\"..")
#     print(f"Fetching successful\n")
#     print(f"Information: \n"
#               f"File size: {round(video.filesize * 0.000001, 2)} MegaBytes\n"
#               f"Highest Resolution: {video.resolution}\n"
#               f"Author: {youtubeObject.author}")
#     print("Views: {:,}\n".format(youtubeObject.views))
#     print(f"Downloading \"{video.title}\"..")   
#     if video != 0:
#         download_start_time
#         video.download(output_path=directory)
#     else:
#         print("error cant download video")
        
#     print("Download is completed successfully")

def download_video(url,directory):
    global progress_bar
    yt = YouTube(url, on_progress_callback=progress_bar)
    title = yt.title.replace(" ", "_").replace("|", "")

    #download video 
    video_stream = yt.streams.filter(only_video=True, adaptive=True, file_extension="mp4").order_by('resolution').desc().first()
    video_path = os.path.join(directory, f"{title}_video.mp4")
    print(f"Downloading video: {yt.title} ({video_stream.resolution})")
    progress_bar = tqdm(total=video_stream.filesize, unit='B', unit_scale=True, desc="Video")
    video_stream.download(output_path=directory, filename=f"{title}_video.mp4")
    progress_bar.close()
    
    #download audio
    audio_stream = yt.streams.filter(only_audio=True, adaptive=True, file_extension="mp4").order_by('abr').desc().first()
    audio_path = os.path.join(directory, f"{title}_audio.mp4")
    print(f"Downloading audio: {yt.title} ({audio_stream.resolution})")
    progress_bar = tqdm(total=audio_stream.filesize, unit='B', unit_scale=True, desc="Audio")
    audio_stream.download(filename=audio_path)
    progress_bar.close()
    
    #merge audio and video
    output_path = os.path.join(directory, f"{title}_final.mp4")
    print("Check file:", os.path.exists(video_path), "|", video_path)
    print("Check file:", os.path.exists(audio_path), "|", audio_path)

    print("merge audio and video file....")
  
    try:
        (
            ffmpeg
            .input(video_path)
            .output(
                output_path,
                i=audio_path,
                vcodec='copy',
                acodec='aac',
                strict='experimental',
                shortest=None
            )
            .run(overwrite_output=True)
        )
    except ffmpeg.Error as e:
        print(" Failed when merge audio and video:", e)
        return
    

    os.remove(video_path)
    os.remove(audio_path)
    print(f"Final file save as: {output_path}\n")
   




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


def search_and_download(url, directory=""):
    global download_start_time
    s = Search(url)
    videos = s.results
    for index,i in enumerate(videos[:50]):
        print(f"{index}.{i.title}")
        # print(type(videos))
    # for i in s.results:
    #     print(f"{i.title}")
    
    
    try:
        choice = int(input("select number from list: "))
        if 0 <= choice <= len(videos[:50]):
            selected_video = videos[choice]
            print(f"downloading video... {selected_video.title}")
            download_video(selected_video.watch_url, directory  )
        else:
            print("invalid choice")
            
    except ValueError:
        print("invalid choice, must number")
        
        
    
    # if 0 <= choise <= len(videos[:50]):
    #     selected_video = videos[choise]
    #     print(f"downloading video... {selected_video.title}")
    #     stream = selected_video.streams.get_highest_resolution()
    #     if stream != 0 :
    #         download_start_time
    #         stream.download()
    #         print("Download is completed successfully")
    #     else:
    #         print("error cant download video")
        

        
    # get object keys
    # keys = "\n".join([k for k in s.results[0].__dict__])
    # print(keys)
    
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
        url = input("search: ")
        search_and_download(url)
    else:
        print("option not valid. please input video or audio")
        print(f"{options}")
        
    
    
main()
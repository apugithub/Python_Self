from pytube import YouTube
import datetime

timestamp = datetime.datetime.now().strftime("%d-%m-%Y, %I-%M-%S %p")  # This is to create the timestamp

local_path = 'C:/Users/Blue Bird/Desktop'
final_path = local_path+'/VID_{stamp}'.format(stamp=timestamp)  # This will create a folder with current timestamp

link = 'https://www.youtube.com/watch?v=5HdB8V09gJU'  # ***** Just enter the link... thats all


def downloadYouTube(videourl, path):
    yt = YouTube(videourl)
    print ('Processing Video...')
    print('These are the details -- \n Title: {title} \n Author: {author} \n Views: {views}\n'.format(title=yt.title,
                                            author=yt.author, views=yt.views))
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().last() # lowest resolution
    #yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first() #highest resolution
    print('Downloading Video...')
    yt.download(path)


downloadYouTube(link, final_path)
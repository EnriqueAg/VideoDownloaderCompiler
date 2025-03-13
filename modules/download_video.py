import os # To get folder path
import yt_dlp # To get username and download video

class Get_Video():
    def __init__(self, url, output_dir, video_name):
        # Initialize the class
        self.url = url
        self.output_dir = output_dir
        self.video_name = video_name
    def download_video(self):
        # Download the video
        ydl_opts = {
            'outtmpl': os.path.join(self.output_dir, f'{self.video_name}.%(ext)s'),
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])

if __name__ == '__main__':
    url = input('Enter the video URL: ')
    output_dir = input('Enter the output directory: ')
    video_name = input('Enter the new video name')
    video = Get_Video(url, output_dir, video_name)
    try:
        video.download_video()
    except:
        print('Error downloading video, please try again')
    else:
        print('Video downloaded successfully')
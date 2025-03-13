import os # To get folder path
from moviepy.video.io.VideoFileClip import VideoFileClip # To combine videos
from moviepy import concatenate_videoclips # To combine videos

class Compile_Videos():
    def __init__(self, folder_videos, output_directory, compilation_name, custom_limit, minutes, secs):
        # Initialize the Compile_Videos class
        self.folder_videos = folder_videos
        self.output_directory = output_directory
        self.compilation_name = compilation_name
        self.custom_limit = custom_limit
        self.minutes = minutes
        self.secs = secs
    
    def folder_videos_content(self):
        # Get the list of video files in the folder, or return an error message if no videos are found
        video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.flv']
        files = [f for f in os.listdir(self.folder_videos) if os.path.isfile(os.path.join(self.folder_videos, f))]
        video_files = [f for f in files if os.path.splitext(f)[1].lower() in video_extensions]
        return video_files if video_files else 'No videos found in the folder'

    def verify_output_folder(self):
        # Check if the output directory exists, otherwise create using the current app directory
        if not os.path.exists(self.output_directory):
            return os.path.dirname(os.path.abspath(__file__))
        return self.output_directory
    
    def total_time(self):
        # Calculate the total duration in seconds based on minutes and seconds
        return self.minutes * 60 + self.secs
    
    def create_compilation(self):
        # Create a compilation of video clips with an optional time limit
        compilation = []
        total_duration = 0  # Track the total duration of the video clips
        time_limit = self.total_time() if self.custom_limit else float('inf')

        # Fetch video files
        video_files = self.folder_videos_content()
        if video_files == 'No videos found in the folder':
            return [] # Return an empty list if no valid videos are found
        for video in video_files:
            video_path = os.path.join(self.folder_videos, video)
            video_clip = VideoFileClip(video_path)
            # Check if adding this clip exceeds the time limit
            if total_duration + video_clip.duration <= time_limit:
                compilation.append(video_clip)
                total_duration += video_clip.duration
            else:
                # Stop adding clips once the time limit is reached
                break
        return compilation # Return the list of video clips

    def combine_videos(self):
        # Combine the video clips into a single compilation
        compilation = self.create_compilation()
        if not compilation:
            print("No video clips to compile.")
            return None
        try:
            final_clip = concatenate_videoclips(compilation)
            compilation_path_name = os.path.join(self.output_directory, self.compilation_name)
            # Ensure output directory exists
            os.makedirs(os.path.dirname(compilation_path_name), exist_ok=True)
            # Write the final video
            final_clip.write_videofile(compilation_path_name, codec="libx264")
            return compilation_path_name
        except Exception as e:
            print(f"Error during video compilation: {e}")
            return None


if __name__ == '__main__':
    folder_videos = input('Enter the folder where the videos are located: ')
    output_directory = input('Enter the output directory: ')
    compilation_name = input('Enter the compilation name: ')
    compilation_name += '.mp4'
    custom_limit = input('Do you want to set a time limit? (True/False): ').strip().lower() == 'true'
    minutes = int(input('Enter the number of minutes: '))
    secs = int(input('Enter the number of seconds: '))

    # Initialize the Compile_Videos class
    compilation = Compile_Videos(folder_videos, output_directory, compilation_name, custom_limit, minutes, secs)

    # Perform folder and file validation
    video_files = compilation.folder_videos_content()
    if video_files == 'No videos found in the folder':
        print(video_files) # Print the 'No videos found in the folder' message
    else:
        # output_directory = compilation.verify_output_folder()
        # Combine videos
        compilation.combine_videos()
import customtkinter as ct
import os # To get folder path
import sys # To get folder path
import threading # To start a new thread, i.e. a new process and not blocking the main UI thread
from modules.cttk_spinbox import FloatSpinbox # cttk_spinbox.py is a custom widget
from modules.get_info import Get_Info # get_info.py is to get video information
from modules.download_video import Get_Video # download_video is to download video
from modules.compile_videos import Compile_Videos # compile_videos is to compile videos

class App(ct.CTk):
    def __init__(self):
        super().__init__()
        self.state('zoomed')
        self.geometry("800x500") # Set initial windows size
        self.minsize(800,500) # Set minimum windows size
        self.resizable(True, True) # Enable resize
        self.title('Video Downloader & Compiler') # Windows name
        current_file_path = os.path.abspath(__file__)  # Absolute path of the current file
        current_directory = os.path.dirname(current_file_path)
        self.iconbitmap(rf"{current_directory}\assets\vdc.ico")  # Icon
        ct.set_appearance_mode('dark') # UI Color
        ct.set_default_color_theme('dark-blue') # Theme for elements


        # base_path : Determine base path based on execution mode
        if getattr(sys, 'frozen', False):  # Running as a PyInstaller bundle
           self.base_path = os.path.dirname(sys.executable)  # Directory of the .exe (dist folder)
        else:  # Running as a regular Python script
            self.base_path = os.path.dirname(os.path.abspath(__file__))  # Directory of the script

    ### DOWNLOAD / SAVE VIDEO ELEMENTS
        #DOWNLOAD FRAME
        self.d_frame = ct.CTkFrame(self, fg_color='#1a1a1a')
        self.d_frame.place(relx=0.1, rely=0.025, relwidth=0.8, relheight=0.4)

        # DOWNLOAD TITLE
        self.title_download =  ct.CTkLabel(self.d_frame, text='Download video', font=ct.CTkFont(size=15, weight="bold"))
        self.title_download.place(relx=0.5, rely=0.1, anchor=ct.CENTER)

        # ENTRY LINK
        self.entry_link = ct.CTkEntry(self.d_frame, placeholder_text='Paste the link of your video here')
        self.entry_link.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.15)

        # BUTTON GET VIDEO INFORMATION
        self.button_get_info = ct.CTkButton(self.d_frame, text='Get video info', command=self.get_info_callback)
        self.button_get_info.place(relx=0.05, rely=0.45, relwidth=0.3, relheight=0.15)

        # ENTRY VIDEO NAME
        self.entry_video_name = ct.CTkEntry(self.d_frame, placeholder_text='Type your new video name here')
        self.entry_video_name.place(relx=0.4, rely=0.45, relwidth=0.55, relheight=0.15)

        # BUTTON DOWNLOAD/SAVE VIDEO
        self.button_download_save = ct.CTkButton(self.d_frame, text='Download/save video', command=self.download_video_callback)
        self.button_download_save.place(relx=0.05, rely=0.7, relwidth=0.3, relheight=0.15)

        # ENTRY PATH
        self.entry_path = ct.CTkEntry(self.d_frame, placeholder_text=self.base_path)
        self.entry_path.place(relx=0.4, rely=0.7, relwidth=0.55, relheight=0.15)

    ### COMPILE VIDEOS ELEMENTS
        ### COMPILER FRAME
        self.c_frame = ct.CTkFrame(self, fg_color='#1a1a1a')
        self.c_frame.place(relx=0.1, rely=0.45, relwidth=0.8, relheight=0.46)

        # COMPILER TITLE
        self.title_compiler =  ct.CTkLabel(self.c_frame, text='Compile video', font=ct.CTkFont(size=15, weight="bold"))
        self.title_compiler.place(relx=0.5, rely=0.1, anchor=ct.CENTER)

        # ENTRY FOLDER PATH OF VIDEOS
        self.entry_path_folder = ct.CTkEntry(self.c_frame, placeholder_text='Paste the folder path that contains your videos here (.MP4, .AVI, .MOV, .MKV, .FLV)')
        self.entry_path_folder.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.14)

        # ENTRY VIDEO COMPILATION NAME
        self.entry_compilation_name = ct.CTkEntry(self.c_frame, placeholder_text='Compilation video name')
        self.entry_compilation_name.place(relx=0.05, rely=0.42, relwidth=0.3,relheight=0.14)

        # ENTRY DESTINATION FOLDER
        self.entry_destination_folder = ct.CTkEntry(self.c_frame, placeholder_text=self.base_path)
        self.entry_destination_folder.place(relx=0.4, rely=0.42, relwidth=0.55,relheight=0.14)

        # SWITCH LIMIT VIDEO DURATION
        self.switch_limit_duration = ct.CTkSwitch(self.c_frame, text='Limit video duration (Minutes:Seconds)', command=self.limit_duration_callback)
        self.switch_limit_duration.place(relx=0.05, rely=0.6, relwidth=0.55, relheight=0.17)

        # SPINBOX MINUTES
        self.spinbox_minutes = FloatSpinbox(self.c_frame, step_size=1, low_limit=0, high_limit=30, command=self.spinbox_minutes_callback)
        #self.spinbox_minutes.place(relx=0.5, rely=0.65, relwidth=0.15, relheight=0.2)

        # LABEL COLON
        self.label_colon = ct.CTkLabel(self.c_frame, text=':', font=ct.CTkFont(size=15, weight="bold"))
        #self.label_colon.place(relx=0.65, rely=0.65, relwidth=0.05, relheight=0.2)  

        # SPINBOX SECONDS
        self.spinbox_seconds = FloatSpinbox(self.c_frame, step_size=1, low_limit=0, high_limit=59, default_value=30, command=self.spinbox_seconds_callback)
        #self.spinbox_seconds.place(relx=0.7, rely=0.65, relwidth=0.15, relheight=0.2)

        # BUTTON COMPILE VIDEOS
        self.button_compile = ct.CTkButton(self.c_frame, text='Compile videos', command=self.compile_videos_callback)
        self.button_compile.place(relx=0.35, rely=0.8, relwidth=0.3, relheight=0.15)

    ### LABEL STATUS ELEMENT
        self.label_status = ct.CTkLabel(self, text='Waiting for user input', font=ct.CTkFont(size=10), fg_color='#1a1a1a', text_color='yellow', anchor=ct.CENTER, justify=ct.LEFT, width=200, height=20, corner_radius=5)
        self.label_status.place(relx=0.5, rely=0.96, anchor=ct.CENTER, relwidth=0.8, relheight=0.05)
    
    def download_video_callback(self):
        # Get the user input
        url = self.entry_link.get()
        if url == '' or not 'https://' in url:
            self.label_status.configure(text='Invalid URL, please try again')
        else:
            output_dir = self.entry_path.get()
            if output_dir == '':
                media_directory = os.path.join(self.base_path, "Media")
                # Create the "Media" folder if it doesn't exist
                if not os.path.exists(media_directory):
                    os.makedirs(media_directory)
                # Set the output directory to the "Media" folder
                output_dir = media_directory
                self.entry_path.insert(0, output_dir)  
            else:
                output_dir = self.entry_path.get()
            video_name = self.entry_video_name.get()
            if video_name == '':
                video_name = 'VDC video'
            self.label_status.configure(text='Downloading video...')
            # Start a new thread for the heavy operation
            threading.Thread(target=self.process_download_video, args=(url, output_dir, video_name), daemon=True).start()
    
    def process_download_video(self, url, output_dir, video_name):
        # Download the video
        video = Get_Video(url, output_dir, video_name)
        try:
            video.download_video()
        except:
            self.label_status.configure(text='Error downloading video, please try again')
        else:
            self.label_status.configure(text='Video downloaded successfully')

    def get_info_callback(self):
        # Get the user input
        url = self.entry_link.get()
        if url == '' or not 'https://' in url:
            self.label_status.configure(text='Invalid URL, please try again')
        else:
            self.label_status.configure(text='Getting video information...')
            # Start a new thread for the heavy operation
            threading.Thread(target=self.process_get_info, args=(url,), daemon=True).start()
    
    def process_get_info(self, url):
        # Get the video information
        info = Get_Info(url)
        try:
            description = info.get_information()
            # Update the GUI on the main thread
            self.entry_video_name.delete(0, ct.END)
            self.entry_video_name.insert(0, description)
            self.label_status.configure(text='Video information was obtained')
        except:
            self.label_status.configure(text='Error getting information, please try again')
    
    def compile_videos_callback(self):
        # Folder videos path
        folder_path = self.entry_path_folder.get()
        if not folder_path or not os.path.exists(folder_path):
            self.label_status.configure(text="Invalid folder or no folder selected. Please select a valid folder.")
            return    
        # Compilation name
        compilation_name = self.entry_compilation_name.get()
        if not compilation_name:
            compilation_name = 'VDC compilation'
            self.entry_compilation_name.insert(0, compilation_name)
        # Destination folder
        output_dir = self.entry_destination_folder.get()
        if not output_dir:
            media_directory = os.path.join(self.base_path, "Media")
            # Create the "Media" folder if it doesn't exist
            if not os.path.exists(media_directory):
                os.makedirs(media_directory)
            # Set the output directory to the "Media" folder
            output_dir = media_directory
            self.entry_destination_folder.insert(0, output_dir)  # Update the entry with the default path
        else:
            output_dir = self.entry_destination_folder.get()
        # Limit duration
        limit_duration_element = self.switch_limit_duration.get()
        if limit_duration_element:
            try:
                custom_limit = True
                minutes = int(self.spinbox_minutes.get())
                seconds = int(self.spinbox_seconds.get())
            except ValueError:
                self.label_status.configure(text='Invalid duration entered. Please correct it.')
                return
        else:
            custom_limit = False
            minutes = 0
            seconds = 0

        self.label_status.configure(text='Compiling videos...')
        # Start a new thread for the heavy operation
        threading.Thread(target=self.process_compile_videos, args=(folder_path, output_dir, compilation_name, custom_limit, minutes, seconds),daemon=True).start()
    
    def process_compile_videos(self, folder_path, output_dir, compilation_name, custom_limit, minutes, seconds):
        # Compile the videos
        compilation_name += '.mp4'
        compilation = Compile_Videos(folder_path, output_dir, compilation_name, custom_limit, minutes, seconds)
        video_files = compilation.folder_videos_content()
        if video_files == 'No videos found in the folder':
            self.label_status.configure(text=video_files)
            return
            #output_directory = compilation.verify_output_folder()
            # Combine videos
        try:
            compilation.combine_videos()
        except Exception as e:
            error_message = f"Error compiling videos: {e}"
            print(error_message)  # Log the error to the console
            self.after(0, lambda: self.label_status.configure(text=error_message)) # 'Error compiling videos, please try again'
        else:
            self.after(0, lambda: self.label_status.configure(text='Videos compiled successfully'))


    def limit_duration_callback(self):
        # Get the switch state and update the GUI
        if self.switch_limit_duration.get():  # Check if the switch is enabled
            # Show spinboxes and label
            print('activado')
            self.spinbox_minutes.place(relx=0.5, rely=0.6, relwidth=0.15, relheight=0.14)
            self.label_colon.place(relx=0.65, rely=0.56, relwidth=0.05, relheight=0.2)
            self.spinbox_seconds.place(relx=0.7, rely=0.6, relwidth=0.15, relheight=0.14)
        else:
            print('desactivado')
            # Hide spinboxes and label
            self.spinbox_minutes.place_forget()
            self.label_colon.place_forget()
            self.spinbox_seconds.place_forget()
    
    def spinbox_minutes_callback(self):
        pass
        #print('Minutes: ', self.spinbox_minutes.get())
    
    def spinbox_seconds_callback(self):
        pass
        #print('Seconds: ', self.spinbox_seconds.get())
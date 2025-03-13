Video Downloader & Compiler (VDC)


Overview
    The Video Downloader & Compiler (VDC) is a graphical user interface (GUI) application that helps users download videos and compile multiple videos into a single file. Designed for simplicity and functionality, the app makes downloading TikTok videos and creating compilations effortless.

    The interface is user-friendly, featuring separate sections for downloading and compiling videos, with clear prompts for input fields, buttons, and status messages.


Features
    1. Video Downloading
        Input a video URL (e.g., TikTok link).
        Retrieve the video author's name and most popular hashtag automatically.
        Set a custom video name or save using a default name.
        Specify a custom save path or use the default path.
        Download the video with the click of a button.

    2. Video Compilation
        Input the folder path containing videos.
        Provide a custom name for the compiled output video.
        Specify a destination folder for the compiled video.
        Optionally limit the duration of the compilation by toggling the duration switch.
        Set the limit using separate fields for minutes and seconds.
        Compile videos into a single video file with the click of a button.

    3. Message Box
        Displays status updates and app information to help users track progress and identify errors.


Getting Started
    Prerequisites
        Python 3.8+ must be installed on your computer.
        Install the required Python dependencies using:
            bash
            pip install -r requirements.txt
    How to Run the Application
        Clone the repository or download the project folder.
        Navigate to the project directory:
            bash
            cd VideoDownloaderCompiler
        Run the application:
            bash
            python


Dependencies
    Install the following libraries using the requirements.txt file:
        beautifulsoup4==4.13.3
        customtkinter==5.2.2
        moviepy==2.1.2
        requests==2.32.3
        yt-dlp==2025.2.19


Usage
    Download Videos:
        Enter the video link in the text field.
        Click "Get Info" to retrieve the author's name and hashtags.
        Provide a custom name (or leave blank for the default name).
        Specify the save path (or leave blank for the default path).
        Click "Download" to save the video.
    Compile Videos:
        Enter the path to the folder containing videos.
        Provide a name for the compiled output file.
        Specify a destination folder for the compiled video.
        Toggle the duration switch if you'd like to limit the compilation time.
        Input the desired time limit in minutes and seconds.
        Click "Compile" to create a single output video.
    App Information:
        View status messages and progress updates in the message box.


Future Enhancements
    Support for more video platforms (e.g., YouTube, Instagram).
    Enhanced error handling for unsupported formats or invalid links.
    Multi-threaded compilation for faster video processing.
    A modernized design with improved themes and responsiveness.


License
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


Created by Enrique Aguirre
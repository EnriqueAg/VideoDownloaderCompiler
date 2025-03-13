from ui_vdc import App

if __name__ == '__main__':
    app = App()
    app.mainloop()


# Generate executable using pyinstaller, launch CMD in the same directory as the main_vdc.py file:
    # C:\Users\recon\AppData\Local\Programs\Python\Python313\Scripts\pyinstaller.exe --onefile --windowed --noconsole --add-data "assets\vdc.ico;assets" --icon "assets\vdc.ico" --name "Video Downloader & Compiler" --clean main_vdc.py
# After installation, the executable is located at "dist\Video Downloader & Compiler.exe" create a Windows Defender Exception for this file:
    # Open Windows Security.
    # Go to Virus & threat protection.
    # Click Manage settings under Virus & threat protection settings.
    # Scroll down to Exclusions and click Add or remove exclusions.
    # Add the dist/ folder or the specific .exe file.
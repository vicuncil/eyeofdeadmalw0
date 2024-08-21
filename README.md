# eyeofdead
"Eye of Dead" is a malware designed to simulate a disruptive behavior on a computer. When executed, it displays a fullscreen message box asking if the user wants to open something. If the user interacts with the application, it performs several actions including:

Playing an Audio Clip: The application plays an audio clip fetched from the web.
Blocking Keyboard Input: It attempts to block keyboard input (though this part is incomplete as keyboard.block_key is not defined).
Displaying Moving Windows: It creates multiple moving windows with a message, which can be overwhelming and disruptive.
Opening a Web Image: It opens a specific image in the web browser.
Setting a Scary Wallpaper: It downloads an image from the web and sets it as the desktop wallpaper.
Warning: This script is designed for malware simulate purposes and might cause frustration or disruption. It should be used responsibly and only on systems where you have permission.
-----------------------------------------------------------------------------------
To make Program file executable
open cmd
pip install pyinstaller
go do direcory Program.py
python -m PyInstaller --onefile --windowed Program.py  

https://github.com/user-attachments/assets/36040d4a-0bc2-4f8e-9bc6-9670ce1bf2d8

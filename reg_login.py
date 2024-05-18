from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import pygame

root = Tk()

root.title('Test001')
root.geometry("400x400")

pygame.init()
pygame.mixer.init()

btn = Button(root, text="play", width= 15,height=2, bg= "blue", fg= "white", command=lambda:filing())
btn.place(x = 100, y = 5)
btn.config(font=(2))

os.chdir("C:/Users/David/Music")
# Fetching Songs
songtracks = os.listdir()

playlist = Listbox(root, width=50, height=16)
playlist.place(x= 45, y=80)
playlist.config(font=("Bahnschrift", 8))


for i in songtracks:
    playlist.insert(END,i) 

def filing():
   
    current_song = playlist.get(playlist.curselection())
    pygame.mixer.music.load(current_song)
    pygame.mixer.music.play()
    

 
root.mainloop()
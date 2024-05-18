from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import pygame

root = Tk()

root.title('Test001')
root.geometry("400x400")

pygame.init()
pygame.mixer.init()

btn = Button(root, text="Open Image", width= 15,height=2, bg= "blue", fg= "white", command=lambda:filing())
btn.place(x = 100, y = 5)
btn.config(font=(2))

lbl = Label(root, text="Playing Music", width=25, height=8)
lbl.place(x= 45, y=80 )
lbl.config(font=(1))

def filing():
    f_types = [('Audio Files', '*.mp3')]
    file = filedialog.askopenfilename(filetypes=f_types)
    
    current_song = file
    pygame.mixer.music.load(current_song)
    pygame.mixer.music.play()



root.mainloop()
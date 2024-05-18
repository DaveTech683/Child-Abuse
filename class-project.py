from tkinter import *
from random import *

root=Tk()
root.geometry("500x300")

lbl1 = Label(root, text=("Enter Your Guessed Number"), font=("Time New Romans", 12))
lbl1.place(x = 30, y =  50)

ent_user = Entry(root, font=("Time New Romans", 20), bg="blue", foreground="white")
ent_user.place(x = 30, y = 80, width=200, height=50)

lbl2 = Label(root, text=("Computer Guessed Number"), font=("Time New Romans",12))
lbl2.place(x = 250, y =  50)

ent_com = Entry(root, font=("Time New Romans", 20), bg="red", foreground="white")
ent_com.place(x = 250, y = 80, width=200, height=50)

def guess():
    Computer = randint(0,10)


    user = ent_user.get()  
    try:
        if int(user) == Computer:
            ent_com.insert(END, Computer)
            lbl3 = Label(root, text="WOW!!! You Did It",font=("Time New Romans", 15) )
            lbl3.place(x = 180, y = 250)  
        elif int(user) != Computer:
            ent_com.insert(END, Computer)
            lbl3 = Label(root, text="E REmain SMall", font=("Time New Romans", 15))
            lbl3.place(x = 180, y = 250)
    except Exception:
        lbl3 = Label(root, text="WHy NAw... Na Rubbish YOu do!!!", font=("Time New Romans", 15))
        lbl3.place(x = 180, y = 250)
        

btn=Button(root,text="Guess", width=20, height=2, font=(2), bg="blue", fg="white", command=guess)
btn.place(x= 110, y =170 )










root.mainloop()  
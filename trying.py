from tkinter import *
import customtkinter as ctk
import mysql.connector
from datetime import datetime
from tkinter import messagebox, ttk
from io import *
from PIL import ImageTk, Image

def view():
    popup = Tk()
    popup.wm_title("!")

    try:
        # windows only (remove the minimize/maximize button)
        popup.attributes('-toolwindow', True)
    except TclError:
        pass

    frame1 = Frame(popup, width=120, height=150)
    frame1.grid(row=0, column=0)

    frame2 = Frame(popup, width=550, height=260)
    frame2.grid(row=0, column=1)

    btn = ctk.CTkButton(frame2, text="OKAY")
    btn.place(x = 200, y = 225)

    mydb = mysql.connector.connect(
            host = "localhost",
            user= "root",
            password = "",
            port= 3306,
            database="childdb"
            )
    cursor = mydb.cursor() 
    view_rec = """ SELECT * FROM abuse_reg"""
    cursor.execute(view_rec)
    results = cursor.fetchall()
    if results == "":
        pass
    else:
        for r in results:
            reporter_name = r[17]
            station_name = r[9]
            officer = r[11]
            status = r[24]
            

    mydb = mysql.connector.connect(
            host = "localhost",
            user= "root",
            password = "",
            port= 3306,
            database="childdb"
            )
    cursor = mydb.cursor() 
    view_rec = """ SELECT * FROM child_reg"""
    cursor.execute(view_rec)
    results = cursor.fetchall()
    if results == "":
        pass
    else:
        for j in results:
            names = j[1]
            name = j[2]
            c_state = j[3]
            c_country = j[4]
            FATHER = j[6]
            MOTHER = j[13]
            f_country = j[11]
            m_country = j[18]
            ABUSE_TYPE = j[20]
            pic = j[22]
            
            message = """
    A case was reported  of whose the victim name is {} {} 
    from {} state in {}.
    He is the child of Mr. {}  and Mrs. {} both citizens of {}.\n
    The victim has been subjected to {}.
    The case which was reported by {}, has been 
    reported to {} station in which 
    Officer {} has been assigned to the case. 
    The status of the case is currently {}""".format(names, name, c_state, c_country, FATHER, MOTHER,
                                                            f_country, ABUSE_TYPE, reporter_name, station_name, 
                                                            officer, status)
        
    imaging = Image.open(BytesIO(pic))
    print(imaging)
    image1= imaging.resize((120,150))
    img2 = ImageTk.PhotoImage(image1)
    print(img2)
    lbl = Label(frame1, image = img2)
    lbl.place(x = 0, y = 0)
    

    lbl = Label(frame2, text=message)
    lbl.place(x = 5, y = 20)
    lbl.config(font=("Bahnschrift", 11))


            



    popup.mainloop()
view()
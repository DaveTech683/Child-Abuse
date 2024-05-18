from tkinter import *
from tkinter import messagebox
import mysql.connector
import customtkinter as ctk
from datetime import datetime


def Auth():
    root = Tk()
    root.title("Child Abuse System")
    # height = root.winfo_screenheight()//2
    # width = (root.winfo_screenwidth())//2
    # root.geometry("{}x{}".format(width, height))
    # this  brings the window to the top
    # root.attributes('-topmost',True)
    # root.eval('tk::PlaceWindow . right')

    try:
        # windows only (remove the minimize/maximize button)
        root.attributes('-toolwindow', True)
    except TclError:
        pass

    ######################This is the database section ################################################
########################################################################################

    frame_auth= Frame(root)
    frame_auth.grid(row=0, column=0)

    lbl_title= ctk.CTkLabel(frame_auth, text="Authorization Page",)
    lbl_title.grid(row=1, column=0, padx=15, pady = 15)
    lbl_title.configure(font=("Bahnschrift", 20))

    lbl_name= ctk.CTkLabel(frame_auth, text="Full Name:")
    lbl_name.grid(row=2, column=0, padx=15, sticky= 'W')
    lbl_name.configure(font=("Bahnschrift", 15))

    entry_name = ctk.CTkEntry(frame_auth, )
    entry_name.grid(row=3, column=0, padx=15, sticky= 'W', ipadx = 150, ipady = 8)

    lbl= ctk.CTkLabel(frame_auth, text="Email Address:")
    lbl.grid(row=4, column=0, padx=15, sticky= 'W')
    lbl.configure(font=("Bahnschrift", 15))

    entry_mail = ctk.CTkEntry(frame_auth, )
    entry_mail.grid(row=5, column=0, padx=15, sticky= 'W', ipadx = 150, ipady = 8)

    lbl= ctk.CTkLabel(frame_auth, text="Phone Number:")
    lbl.grid(row=6, column=0, padx=15, sticky= 'W')
    lbl.configure(font=("Bahnschrift", 15))

    entry_phone = ctk.CTkEntry(frame_auth, )
    entry_phone.grid(row=7, column=0, padx=15, sticky= 'W', ipadx = 150, ipady = 8)

    lbl= ctk.CTkLabel(frame_auth, text="Username:")
    lbl.grid(row=8, column=0, padx=15, sticky= 'W')
    lbl.configure(font=("Bahnschrift", 15))

    entry_username = ctk.CTkEntry(frame_auth, )
    entry_username.grid(row=9, column=0, padx=15, sticky= 'W', ipadx = 150, ipady = 8)

    lbl= ctk.CTkLabel(frame_auth, text="Password:")
    lbl.grid(row=10, column=0, padx=15, sticky= 'W')
    lbl.configure(font=("Bahnschrift", 15))

    entry_pass = ctk.CTkEntry(frame_auth, )
    entry_pass.grid(row=11, column=0, padx=15, sticky= 'W', ipadx = 150, ipady = 8)

    lbl_addr= ctk.CTkLabel(frame_auth, text="Address:")
    lbl_addr.grid(row=12, column=0, padx=15, sticky= 'W')
    lbl_addr.configure(font=("Bahnschrift", 15))

    entry_addr = ctk.CTkEntry(frame_auth, )
    entry_addr.grid(row=13, column=0, padx=15, sticky= 'W', ipadx = 150, ipady = 8)

    lbl= ctk.CTkLabel(frame_auth, text="State:")
    lbl.grid(row=14, column=0, padx=15, sticky= 'W')
    lbl.configure(font=("Bahnschrift", 15))

    entry_state = ctk.CTkEntry(frame_auth, )
    entry_state.grid(row=15, column=0, padx=15, sticky= 'W', ipadx = 150, ipady = 8)

    lbl= ctk.CTkLabel(frame_auth, text="Country:")
    lbl.grid(row=16, column=0, padx=15, sticky= 'W')
    lbl.configure(font=("Bahnschrift", 15))

    entry_country = ctk.CTkEntry(frame_auth, )
    entry_country.grid(row=17, column=0, padx=15, sticky= 'W', ipadx = 150, ipady = 8)

    btn_reg = ctk.CTkButton(frame_auth, text="Submit", command=lambda:auth_reg())
    btn_reg.grid(row=18, column=0, padx=15, sticky= 'W', ipadx = 150, ipady = 8, pady=20)

    def auth_reg():
        name = entry_name.get()
        mail = entry_mail.get()
        phone = entry_phone.get()
        u_name = entry_username.get()
        p_word = entry_pass.get()
        addr  = entry_addr.get()
        state = entry_state.get()
        country = entry_country.get()

        current_date = datetime.now()
        now_date =current_date.date()

        try: 
            if name != "" or mail != "" or phone != "" or u_name  != "" or p_word != "":
                mydb = mysql.connector.connect(
                        host = "localhost",
                        user= "root",
                        password = "",
                        port= 3306,
                        database="childdb"
                        )
                cursor = mydb.cursor() 
                reg = """CREATE TABLE if not exists auth_reg (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(100),
                        email_address VARCHAR(50),
                        phone VARCHAR(30) NOT NULL,
                        username VARCHAR(50),
                        password VARCHAR(15),
                        address VARCHAR(100),
                        state VARCHAR(30) NOT NULL,
                        country VARCHAR(30) NOT NULL,
                        date VARCHAR(11) NOT NULL                         
                        )"""
                cursor.execute(reg)
                
                mydb.commit()
                insert_table = """INSERT INTO auth_reg(
                            name, email_address, phone, username, password, address, state, country, date)
                            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                vals = (name, mail, phone, u_name, p_word, addr, state, country, now_date )
                cursor.execute(insert_table, vals)
                mydb.commit()
                messagebox.showinfo("SUCCESS", "USER REGISTERED SUCCESSFULLY")
                mydb.close()
            else:
                messagebox.showwarning("Alert", "Incomplete Details")
        except Exception as e:
            messagebox.showerror("Error", e)


    root.mainloop()


def Auth_edit():
    root = Tk()
    root.title("Child Abuse System")
    # height = root.winfo_screenheight()//2
    # width = (root.winfo_screenwidth())//2
    # root.geometry("{}x{}".format(width, height))
    # this  brings the window to the top
    # root.attributes('-topmost',True)
    # root.eval('tk::PlaceWindow . right')

    try:
        # windows only (remove the minimize/maximize button)
        root.attributes('-toolwindow', True)
    except TclError:
        pass

    ######################This is the database section fo collection ################################################
########################################################################################

    frame_auth= Frame(root)
    frame_auth.grid(row=0, column=0)

    lbl_title= ctk.CTkLabel(frame_auth, text="Edit Profile",)
    lbl_title.grid(row=1, column=0, padx=15, pady = 15)
    lbl_title.configure(font=("Bahnschrift", 20))

    lbl_name= ctk.CTkLabel(frame_auth, text="Full Name:")
    lbl_name.grid(row=2, column=0, padx=15, sticky= 'W')
    lbl_name.configure(font=("Bahnschrift", 15))

    global entry_name
    entry_name = ctk.CTkEntry(frame_auth, )
    entry_name.grid(row=3, column=0, padx=15, sticky= 'W', ipadx = 150, ipady = 8)

    lbl= ctk.CTkLabel(frame_auth, text="Email Address:")
    lbl.grid(row=4, column=0, padx=15, sticky= 'W')
    lbl.configure(font=("Bahnschrift", 15))

    global entry_mail
    entry_mail = ctk.CTkEntry(frame_auth, )
    entry_mail.grid(row=5, column=0, padx=15, sticky= 'W', ipadx = 150, ipady = 8)

    lbl= ctk.CTkLabel(frame_auth, text="Phone Number:")
    lbl.grid(row=6, column=0, padx=15, sticky= 'W')
    lbl.configure(font=("Bahnschrift", 15))

    global entry_phone
    entry_phone = ctk.CTkEntry(frame_auth, )
    entry_phone.grid(row=7, column=0, padx=15, sticky= 'W', ipadx = 150, ipady = 8)

    lbl= ctk.CTkLabel(frame_auth, text="Username:")
    lbl.grid(row=8, column=0, padx=15, sticky= 'W')
    lbl.configure(font=("Bahnschrift", 15))

    global entry_username
    entry_username = ctk.CTkEntry(frame_auth, )
    entry_username.grid(row=9, column=0, padx=15, sticky= 'W', ipadx = 150, ipady = 8)

    lbl= ctk.CTkLabel(frame_auth, text="Password:")
    lbl.grid(row=10, column=0, padx=15, sticky= 'W')
    lbl.configure(font=("Bahnschrift", 15))

    global entry_pass
    entry_pass = ctk.CTkEntry(frame_auth, )
    entry_pass.grid(row=11, column=0, padx=15, sticky= 'W', ipadx = 150, ipady = 8)

    lbl_addr= ctk.CTkLabel(frame_auth, text="Address:")
    lbl_addr.grid(row=12, column=0, padx=15, sticky= 'W')
    lbl_addr.configure(font=("Bahnschrift", 15))

    global entry_addr
    entry_addr = ctk.CTkEntry(frame_auth, )
    entry_addr.grid(row=13, column=0, padx=15, sticky= 'W', ipadx = 150, ipady = 8)

    lbl= ctk.CTkLabel(frame_auth, text="State:")
    lbl.grid(row=14, column=0, padx=15, sticky= 'W')
    lbl.configure(font=("Bahnschrift", 15))

    global entry_state
    entry_state = ctk.CTkEntry(frame_auth, )
    entry_state.grid(row=15, column=0, padx=15, sticky= 'W', ipadx = 150, ipady = 8)

    lbl= ctk.CTkLabel(frame_auth, text="Country:")
    lbl.grid(row=16, column=0, padx=15, sticky= 'W')
    lbl.configure(font=("Bahnschrift", 15))

    global entry_country
    entry_country = ctk.CTkEntry(frame_auth, )
    entry_country.grid(row=17, column=0, padx=15, sticky= 'W', ipadx = 150, ipady = 8)

    btn_reg = ctk.CTkButton(frame_auth, text="Submit")
    btn_reg.grid(row=18, column=0, padx=15, sticky= 'W', ipadx = 150, ipady = 8, pady=20)

    def get_auth():

        mydb = mysql.connector.connect(
                host = "localhost",
                user= "root",
                password = "",
                port= 3306,
                database="childdb"
                )
        cursor = mydb.cursor() 
        frame_one_rec = """ SELECT * FROM auth_reg;"""
        cursor.execute(frame_one_rec)
        results_one = cursor.fetchall()
       
        for i in results_one:
            entry_name.insert(0, i[1])
            entry_mail.insert(0, i[2])
            entry_phone.insert(0, i[3])
            entry_username.insert(0, i[4])
            entry_pass.insert(0, i[5])
            entry_addr.insert(0, i[6])
            entry_state.insert(0, i[7])
            entry_country.insert(0, i[8])
        mydb.commit()
        mydb.close()
        
    get_auth()



    root.mainloop()

from tkinter import *
import customtkinter as ctk
import mysql.connector
from datetime import datetime
from tkinter import messagebox, ttk



def popupmsg_abuse():
    popup = Tk()
    popup.wm_title("!")

    try:
        # windows only (remove the minimize/maximize button)
        popup.attributes('-toolwindow', True)
    except TclError:
        pass

    label1 = ctk.CTkLabel(popup, text="Abuse ID")
    label1.grid(row=0, column=0)

    abuse_id_1 = ctk.CTkEntry(popup, placeholder_text= "Abuse ID")
    abuse_id_1.grid(row=1, column=0, ipadx=5, ipady=5, padx=10)

    label2 = ctk.CTkLabel(popup, text="Type of Abuse")
    label2.grid(row=0, column=1, ipadx=5, ipady=5, padx=10, pady=0)

    global type_abuse 
    clicked = StringVar()
    options = ["Bullying and cyberbullying", "Child sexual exploitation","Child trafficking"," Domestic abuse",
                "Emotional abuse"," Grooming", "Neglect", "Online Abuse", "Physical Abuse", "Sexual Abuse"]
    global type_abuse 
    type_abuse = ttk.Combobox (popup, values =options, textvariable = clicked)
    type_abuse.grid(row=1, column=1, ipadx=5, ipady=5, padx=10)

    label3 = ctk.CTkLabel(popup, text="Abused Name(Child)")
    label3.grid(row=0, column=2, ipadx=5, ipady=5, padx=10, pady=0)

    abused_n = ctk.CTkEntry(popup)
    abused_n.grid(row=1, column= 2, ipadx=5, ipady=5, padx=10, pady=10)

    label4 = ctk.CTkLabel(popup, text="Abused Phone(If Any)")
    label4.grid(row=0, column=3, ipadx=5, ipady=5, padx=10, pady=5)

    abused_p = ctk.CTkEntry(popup)
    abused_p.grid(row=1, column= 3, ipadx=5, ipady=5, padx=10, pady=5)

    label5 = ctk.CTkLabel(popup, text="Abused Address")
    label5.grid(row=0, column=4, ipadx=5, ipady=5, padx=10, pady=5)

    abused_addr = ctk.CTkEntry(popup)
    abused_addr.grid(row=1, column= 4, ipadx=5, ipady=5, padx=10, pady=5)

    label6 = ctk.CTkLabel(popup, text="Abused Email")
    label6.grid(row=2, column=0, ipadx=5, ipady=5, padx=10, pady=5)

    abused_mail = ctk.CTkEntry(popup)
    abused_mail.grid(row=3, column=0, ipadx=5, ipady=5, padx=10, pady=5)

    label7 = ctk.CTkLabel(popup, text="Abused State")
    label7.grid(row=2, column=1, ipadx=5, ipady=5, padx=10, pady=5)

    a_state = ctk.CTkEntry(popup)
    a_state.grid(row=3, column=1, ipadx=5, ipady=5, padx=10, pady=5)

    label8 = ctk.CTkLabel(popup, text="Abused Country")
    label8.grid(row=2, column=2, ipadx=5, ipady=5, padx=10, pady=5)

    global a_country 
    clicked = StringVar()
    options = ["U.S.A", "Nigeria", "Canada"]
    global a_country 
    a_country = ttk.Combobox (popup, values =options, textvariable = clicked)
    a_country.grid(row=3, column=2, ipadx=5, ipady=5, padx=10, pady=5)

    label9 = ctk.CTkLabel(popup, text="Station Reported")
    label9.grid(row=2, column=3, ipadx=5, ipady=5, padx=10, pady=5)

    station_n = ctk.CTkEntry(popup)
    station_n.grid(row=3, column=3, ipadx=5, ipady=5, padx=10, pady=5)

    label10 = ctk.CTkLabel(popup, text="Station Address")
    label10.grid(row=2, column=4, ipadx=5, ipady=5, padx=10, pady=5)

    station_addr = ctk.CTkEntry(popup)
    station_addr.grid(row=3, column=4, ipadx=5, ipady=5, padx=10, pady=5)

    label11 = ctk.CTkLabel(popup, text="Officer Incharge")
    label11.grid(row=4, column=0, ipadx=5, ipady=5, padx=10, pady=5)

    p_ic = ctk.CTkEntry(popup)
    p_ic.grid(row=5, column=0, ipadx=5, ipady=5, padx=10, pady=5)

    label12 = ctk.CTkLabel(popup, text="Officer Phone")
    label12.grid(row=4, column=1, ipadx=5, ipady=5, padx=10, pady=5)

    officer_phone = ctk.CTkEntry(popup)
    officer_phone.grid(row=5, column=1, ipadx=5, ipady=5, padx=10, pady=5)

    label13 = ctk.CTkLabel(popup, text="Officer Email")
    label13.grid(row=4, column=2, ipadx=5, ipady=5, padx=10, pady=5)

    Officer_email = ctk.CTkEntry(popup)
    Officer_email.grid(row=5, column=2, ipadx=5, ipady=5, padx=10, pady=5)

    label14= ctk.CTkLabel(popup, text="Officer Address")
    label14.grid(row=4, column=3, ipadx=5, ipady=5, padx=10, pady=5)

    officer_address = ctk.CTkEntry(popup)
    officer_address.grid(row=5, column=3, ipadx=5, ipady=5, padx=10, pady=5)

    label15 = ctk.CTkLabel(popup, text="Officer's State")
    label15.grid(row=4, column=4, ipadx=5, ipady=5, padx=10, pady=5)

    officer_state = ctk.CTkEntry(popup)
    officer_state.grid(row=5, column=4, ipadx=5, ipady=5, padx=10, pady=5)

    label15 = ctk.CTkLabel(popup, text="Officer's Country")
    label15.grid(row=6, column=0, ipadx=5, ipady=5, padx=10, pady=5)

    global officer_country 
    clicked = StringVar()
    options = ["U.S.A", "Nigeria", "Canada"]
    global officer_country 
    officer_country = ttk.Combobox (popup, values =options, textvariable = clicked)
    officer_country.grid(row=7, column=0, ipadx=5, ipady=5, padx=10, pady=5)

    label15 = ctk.CTkLabel(popup, text="Reporter's Name")
    label15.grid(row=6, column=1, ipadx=5, ipady=5, padx=10, pady=5)

    r_name = ctk.CTkEntry(popup)
    r_name.grid(row=7, column=1, ipadx=5, ipady=5, padx=10, pady=5)

    label15 = ctk.CTkLabel(popup, text="Reporter's Phone")
    label15.grid(row=6, column=2, ipadx=5, ipady=5, padx=10, pady=5)

    r_phone = ctk.CTkEntry(popup)
    r_phone.grid(row=7, column=2, ipadx=5, ipady=5, padx=10, pady=5)

    label15 = ctk.CTkLabel(popup, text="Reporter's Email")
    label15.grid(row=6, column=3, ipadx=5, ipady=5, padx=10, pady=5)

    r_email = ctk.CTkEntry(popup)
    r_email.grid(row=7, column=3, ipadx=5, ipady=5, padx=10, pady=5)

    label15 = ctk.CTkLabel(popup, text="Reporter's Address")
    label15.grid(row=6, column=4, ipadx=5, ipady=5, padx=10, pady=5)

    r_addr = ctk.CTkEntry(popup)
    r_addr.grid(row=7, column=4, ipadx=5, ipady=5, padx=10, pady=5)

    label15 = ctk.CTkLabel(popup, text="Reporter's State")
    label15.grid(row=8, column=0, ipadx=5, ipady=5, padx=10, pady=5)

    r_state = ctk.CTkEntry(popup)
    r_state.grid(row=9, column=0, ipadx=5, ipady=5, padx=10, pady=5)

    label15 = ctk.CTkLabel(popup, text="Reporter's Country")
    label15.grid(row=8, column=1, ipadx=5, ipady=5, padx=10, pady=5)

    global r_country 
    clicked = StringVar()
    options = ["U.S.A", "Nigeria", "Canada"]
    global r_country 
    r_country = ttk.Combobox (popup, values =options, textvariable = clicked)
    r_country.grid(row=9, column=1, ipadx=5, ipady=5, padx=10, pady=5)

    label15 = ctk.CTkLabel(popup, text="Status")
    label15.grid(row=8, column=2, ipadx=5, ipady=5, padx=10, pady=5)

    global status_1 
    clicked = StringVar()
    options = ["Pending", "Solved", "Unsolved"]
    global status_1 
    status_1 = ttk.Combobox (popup, values =options, textvariable = clicked)
    status_1.grid(row=9, column=2, ipadx=5, ipady=5, padx=10, pady=5)

    btn_submit = ctk.CTkButton(popup, text="Submit", command=lambda:abuse_admin_popup_query())
    btn_submit.grid(row=9,rowspan=3, column=3, ipadx=5, ipady=5, padx=10, pady=5)

    def abuse_admin_popup_query():
        abuse_id = abuse_id_1.get().upper()
        type = type_abuse.get().upper()
        cname = abused_n.get().upper()
        cphone = abused_p.get()
        caddr = abused_addr.get().upper()
        cemail = abused_mail.get()
        cstate = a_state.get().upper()
        ccountry = a_country.get().upper()
        station = station_n.get().upper()
        saddr = station_addr.get().upper()
        pname = p_ic.get().upper()
        pphone = officer_phone.get()
        pemail = Officer_email.get()
        paddr = officer_address.get().upper()
        pstate = officer_state.get().upper()
        pcountry = officer_country.get().upper()
        rname = r_name.get().upper()
        rphone = r_phone.get()
        remail = r_email.get()
        raddr = r_addr.get().upper()
        rstate = r_state.get().upper()
        rcountry = r_country.get().upper()
        status = status_1.get().upper()

        current_date = datetime.now()
        now_date =current_date.date()


        try:

            mydb = mysql.connector.connect(
                    host = "localhost",
                    user= "root",
                    password = "",
                    port= 3306,
                    database="childdb"
                    )
            cursor = mydb.cursor() 
            insert_rec =  """INSERT INTO abuse_reg(
                            abuse_id, type_abuse, abused_name, abused_phone, abused_address, abused_email, abused_state, abused_country,
                            station_reported, station_address, person_incharge, person_phone, person_email, person_address, person_state,
                            person_country, reporter_name, reporter_phone, reporter_email, reporter_address, reporter_state, 
                            reporter_country, date, status )
                            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            print("Got Here?")
            vals = (abuse_id, type, cname, cphone, caddr, cemail, cstate, ccountry,station, saddr, pname, 
                    pphone, pemail, paddr, pstate, pcountry, rname, rphone, remail, raddr, rstate, rcountry, now_date, status)
            cursor.execute(insert_rec, vals)            
            mydb.commit()
            mydb.close()
            messagebox.showinfo("SUCCESS", "RECORD INSERTED")
        except Exception as e:
            messagebox.showerror("Error", e)

    popup.mainloop()
popupmsg_abuse()

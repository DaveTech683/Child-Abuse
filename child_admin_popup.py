from tkinter import *
import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
import mysql.connector
from tkinter import ttk

def popupmsg_child():
    popup = Tk()
    popup.wm_title("!")

    try:
        # windows only (remove the minimize/maximize button)
        popup.attributes('-toolwindow', True)
    except TclError:
        pass

    label1 = ctk.CTkLabel(popup, text="First Name")
    label1.grid(row=0, column=0)

    first_name = ctk.CTkEntry(popup)
    first_name.grid(row=1, column=0, ipadx=5, ipady=5, padx=10, pady=5)

    label2 = ctk.CTkLabel(popup, text="Last Name")
    label2.grid(row=0, column=1, ipadx=5, ipady=5, padx=10, pady=5)

    last_name = ctk.CTkEntry(popup)
    last_name.grid(row=1, column=1, ipadx=5, ipady=5, padx=10, pady=5)

    label3 = ctk.CTkLabel(popup, text="Address")
    label3.grid(row=0, column=2, ipadx=5, ipady=5, padx=10, pady=5)

    address = ctk.CTkEntry(popup)
    address.grid(row=1, column= 2, ipadx=5, ipady=5, padx=10, pady=5)

    label4 = ctk.CTkLabel(popup, text="State")
    label4.grid(row=2, column=0, ipadx=5, ipady=5, padx=10, pady=5)

    state = ctk.CTkEntry(popup)
    state.grid(row=3, column= 0, ipadx=5, ipady=5, padx=10, pady=5)


    label5 = ctk.CTkLabel(popup, text="Country")
    label5.grid(row=2, column=1, ipadx=5, ipady=5, padx=10, pady=5)

    global country 
    clicked = StringVar()
    options = ["U.S.A", "Nigeria", "Canada"]
    global country 
    country = ttk.Combobox (popup, values =options, textvariable = clicked)
    country.grid(row=3, column= 1, ipadx=5, ipady=5, padx=10, pady=5)

    label6 = ctk.CTkLabel(popup, text="Father Last Name")
    label6.grid(row=2, column=2, ipadx=5, ipady=5, padx=10, pady=5)

    father_name = ctk.CTkEntry(popup)
    father_name.grid(row=3, column=2, ipadx=5, ipady=5, padx=10, pady=5)

    label7 = ctk.CTkLabel(popup, text="Father's Contact")
    label7.grid(row=4, column=0, ipadx=5, ipady=5, padx=10, pady=5)

    father_phone = ctk.CTkEntry(popup)
    father_phone.grid(row=5, column=0, ipadx=5, ipady=5, padx=10, pady=5)

    label8 = ctk.CTkLabel(popup, text="Father's Email")
    label8.grid(row=4, column=1, ipadx=5, ipady=5, padx=10, pady=5)

    father_email = ctk.CTkEntry(popup)
    father_email.grid(row=5, column=1, ipadx=5, ipady=5, padx=10, pady=5)

    label9 = ctk.CTkLabel(popup, text="Father's Address")
    label9.grid(row=4, column=2, ipadx=5, ipady=5, padx=10, pady=5)

    father_address = ctk.CTkEntry(popup)
    father_address.grid(row=5, column=2, ipadx=5, ipady=5, padx=10, pady=5)

    label10 = ctk.CTkLabel(popup, text="Father's State")
    label10.grid(row=6, column=0, ipadx=5, ipady=5, padx=10, pady=5)

    father_state = ctk.CTkEntry(popup)
    father_state.grid(row=7, column=0, ipadx=5, ipady=5, padx=10, pady=5)

    label10 = ctk.CTkLabel(popup, text="Father's Country")
    label10.grid(row=6, column=1, ipadx=5, ipady=5, padx=10, pady=5)

    global father_country 
    clicked = StringVar()
    options = ["U.S.A", "Nigeria", "Canada"]
    global father_country 
    father_country = ttk.Combobox (popup, values =options, textvariable = clicked)
    father_country.grid(row=7, column=1, ipadx=5, ipady=5, padx=10, pady=5)

    label11 = ctk.CTkLabel(popup, text="Mother Last Name")
    label11.grid(row=6, column=2, ipadx=5, ipady=5, padx=10, pady=5)

    mother_name = ctk.CTkEntry(popup)
    mother_name.grid(row=7, column=2, ipadx=5, ipady=5, padx=10, pady=5)

    label12 = ctk.CTkLabel(popup, text="Mother's Contact")
    label12.grid(row=8, column=0, ipadx=5, ipady=5, padx=10, pady=5)

    mother_phone = ctk.CTkEntry(popup)
    mother_phone.grid(row=9, column=0, ipadx=5, ipady=5, padx=10, pady=5)

    label13 = ctk.CTkLabel(popup, text="Mother's Email")
    label13.grid(row=8, column=1, ipadx=5, ipady=5, padx=10, pady=5)

    mother_email = ctk.CTkEntry(popup)
    mother_email.grid(row=9, column=1, ipadx=5, ipady=5, padx=10, pady=5)

    label14= ctk.CTkLabel(popup, text="Mother's Address")
    label14.grid(row=8, column=2, ipadx=5, ipady=5, padx=10, pady=5)

    mother_address = ctk.CTkEntry(popup)
    mother_address.grid(row=9, column=2, ipadx=5, ipady=5, padx=10, pady=5)

    label15 = ctk.CTkLabel(popup, text="Mother's State")
    label15.grid(row=10, column=0, ipadx=5, ipady=5, padx=10, pady=5)

    mother_state = ctk.CTkEntry(popup)
    mother_state.grid(row=11, column=0, ipadx=5, ipady=5, padx=10, pady=5)

    label15 = ctk.CTkLabel(popup, text="Mother's Country")
    label15.grid(row=10, column=1, ipadx=5, ipady=5, padx=10, pady=5)

    global mother_country 
    clicked = StringVar()
    options = ["U.S.A", "Nigeria", "Canada"]
    global mother_country 
    mother_country = ttk.Combobox (popup, values =options, textvariable = clicked)
    mother_country.grid(row=11, column=1, ipadx=5, ipady=5, padx=10, pady=5)

    label15 = ctk.CTkLabel(popup, text="Abuse ID")
    label15.grid(row=10, column=2, ipadx=5, ipady=5, padx=10, pady=5)

    abuse_id = ctk.CTkEntry(popup)
    abuse_id.grid(row=11, column=2, ipadx=5, ipady=5, padx=10, pady=5)

    btn_submit = ctk.CTkButton(popup, text="Submit", command=lambda:abuse_popup_query())
    btn_submit.grid(row=14,rowspan=2, column=1, ipadx=5, ipady=5, padx=10, pady=5)

    def abuse_popup_query():

        child_f_name = first_name.get().upper()
        child_l_name = last_name.get().upper()
        child_state = state.get().upper()
        child_country = country.get().upper()
        child_add = address.get().upper()
        f_f_name = father_name.get().upper()
        f_phone = father_phone.get()
        f_email = father_email.get()
        f_country = father_country.get().upper()
        f_state = father_state.get().upper()
        f_add = father_address.get().upper()
        m_f_name = mother_name.get().upper()
        m_phone = mother_phone.get()
        m_email = mother_email.get()
        m_state = mother_state.get().upper()
        m_country = mother_country.get().upper()
        m_add = mother_address.get().upper()
        id_child = abuse_id.get().upper()

        current_date = datetime.now()
        now_date =current_date.date()

        if child_f_name == "" or child_l_name == "" or child_state == "" or child_country == "" or child_add == "" or f_f_name == "" or f_phone == "" or f_email == "" or f_state == "" or f_country == "" or f_add == "" or m_f_name == "" or m_phone == "" or m_email == "" or m_state == "" or m_country == "" or m_add == "" or id_child == "" or now_date:
            messagebox.showerror("ERROR", "EMPTY/INVALID INPUT")
        else:
            try:

                mydb = mysql.connector.connect(
                        host = "localhost",
                        user= "root",
                        password = "",
                        port= 3306,
                        database="childdb"
                        )
                cursor = mydb.cursor() 
                insert_table = """INSERT INTO child_reg (
                                        child_first_name, child_last_name,child_state, child_country, child_address,
                                        father_last_name, father_phone, father_email, father_state, father_country, father_Address,
                                        mother_last_name, mother_phone, mother_email, mother_state, mother_country,mother_address,
                                        abuse_id,date)
                                        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                vals = (child_f_name, child_l_name,child_state, child_country, child_add, f_f_name,f_phone, f_email,
                        f_state, f_country, f_add,m_f_name, m_phone, m_email, m_state, m_country, m_add,id_child, now_date)
                cursor.execute(insert_table, vals)      
                mydb.commit()
                mydb.close()
                messagebox.showinfo("SUCCESS", "RECORD INSERTED")
            except Exception as e:
                messagebox.showerror("Error", e)

    popup.mainloop()
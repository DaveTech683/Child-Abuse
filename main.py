from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image, ImageTk, ImageFile
from tkinter import ttk
from child_admin_popup import popupmsg_child
from abuse_admin_popup import popupmsg_abuse
import mysql.connector
from datetime import datetime
from login_reg import Auth, Auth_edit
from tkinter import filedialog
from io import *

ImageFile.LOAD_TRUNCATED_IMAGES = True




root = Tk()
root.title("Child Abuse Cases")
height = root.winfo_screenheight()
width = root.winfo_screenwidth()
root.geometry("{}x{}".format(width, height))

# rootck = ctk.CTk()
# ctk.set_appearance_mode("System")

# # windows only (remove the minimize/maximize button)
# root.attributes('-toolwindow', True)

############################################ Top Bar ##############################################################
########################################
###################################
def topbar():
    frame_header = Frame(root, width=width,height=height//12, bg='black')
    frame_header.grid(row=0)
   

    label1 = Label(frame_header, text="Child Abuse", fg='white', bg='black')
    label1.place(x= 100, y=16)
    label1.config(font=("Bahnschrift", 15))

    # global btn_descript
    # clicked = StringVar()
    # options = ['Registeration', 'Admin Page']
    # btn_descript = ttk.Combobox (frame_header, values = options,font=('san-serif', 13), textvariable = clicked)
    # btn_descript.place(x = 1300, y = 15, width=150, height=50)
    # btn_descript.config(font=("Bahnschrift", 13))

    global mbtn
    mbtn = Menubutton(frame_header, text="> Choose Page <", relief=RAISED, bg='black', fg='white')
    mbtn.place(x = 1350, y = 13, width=150, height=50)
    mbtn.config(font=("Bahnschrift", 13))
    mbtn.menu = Menu(mbtn, tearoff = 0)
    mbtn.menu.config(font=("Bahnschrift", 13))
    mbtn["menu"] = mbtn.menu
    
    mbtn.menu.add_command(label="Case Report", command=lambda:bodybar())
    mbtn.menu.add_command(label="Admin Page", command=lambda:login())

    def front_page():
        frame1 = Frame(root, width=700, height=500)
        frame1.place(x = 50, y = 100)

        front_text = """    Welcome To The Child Abuse System Where You Keep Record 
        Of Children
        And Information About Their Abuse!!!

        NOTE: All Information Entered Here Has To Be Correct... 

        
        Click On A Button To Continue Further
        """

        lbl = Label(frame1, text=front_text)
        lbl.place(x = 10, y = 125)
        lbl.config(font=("Bahnschrift",18))

        frame2 = Frame(root, width=700, height=500)
        frame2.place(x = 780, y = 120)

        img= (Image.open("child.png"))
        image= img.resize((580,400))

        global new_image
        new_image= ImageTk.PhotoImage(image)

        lbl2 = Label(frame2, image=new_image)
        lbl2.place(x = 0, y = 30)

        btn1 = ctk.CTkButton(root, text='Case Report Page',height=50,font=("Bahnschrift",18), width=200, command=lambda:bodybar())
        btn1.place(x = 500, y = 650)
        
        

        btn2 = ctk.CTkButton(root, text='Admin Page', height=50,font=("Bahnschrift",18), width=200, command=lambda:login())
        btn2.place(x = 800, y = 650)
    
        
    

    ############################################ Body Bar ##############################################################
    ########################################
    ###################################
    def bodybar():
        frame_body = Frame(root, width=width,height=height, bg='black')
        frame_body.grid(row=1, column = 0)

        frame_sidebar = Frame(frame_body, width=width//5,height=height, bg='black', relief=RAISED)
        frame_sidebar.place(x = 50, y = 0)
        

        btn_dash2 = Button(frame_sidebar, text='Children >>', background='black', fg='white', command=lambda:reg_children())
        btn_dash2.pack(side='top', ipadx=40, ipady=15, pady=10)
        btn_dash2.config(font=("Bahnschrift", 15))

        btn_dash3 = Button(frame_sidebar, text='Abuse >>>>', bg='black', fg='white', command=lambda:reg_abuse())
        btn_dash3.pack(side='top', ipadx=40, ipady=15, pady=10)
        btn_dash3.config(font=("Bahnschrift", 15))

        
        # btn_dash = Button(frame_sidebar, text='Reports >>', bg='black', fg='white', command=lambda:report())
        # btn_dash.pack(side='top', ipadx=40, ipady=15, pady=10)
        # btn_dash.config(font=("Bahnschrift", 15))

        ##################################### BODY PAGE ##############################################
        ##################################
        ###############################
        ###########################
        
        def reg_children():
            frame_childbar = Frame(frame_body,width=width, height=height, bg='white')
            frame_childbar.place(x=306, y=0)

            lbl1 = ctk.CTkLabel(frame_childbar, text='Record New Children')
            lbl1.place(x = 23, y = 30)
            lbl1.configure(font=("Bahnschrift", 18))

            lbl1 = ctk.CTkLabel(frame_childbar, text='First Name:')
            lbl1.place(x = 23, y = 100)
            lbl1.configure(font=("Bahnschrift", 18))

            f_nameEntry = ctk.CTkEntry(frame_childbar, placeholder_text="first Name", width=200, height= 50)
            f_nameEntry.place(x=23, y=130)

            lbl1 = ctk.CTkLabel(frame_childbar, text='Last Name:')
            lbl1.place(x = 250, y = 100)
            lbl1.configure(font=("Bahnschrift", 18))

            l_nameEntry = ctk.CTkEntry(frame_childbar, placeholder_text="Last Name", width=200, height= 50)
            l_nameEntry.place(x=250, y=130)

            lbl1 = ctk.CTkLabel(frame_childbar, text='State:')
            lbl1.place(x = 480, y = 100)
            lbl1.configure(font=("Bahnschrift", 18))

            s_nameEntry = ctk.CTkEntry(frame_childbar, placeholder_text="Child's State", width=200, height= 50)
            s_nameEntry.place(x=480, y=130)

            lbl1 = ctk.CTkLabel(frame_childbar, text="Child's Country:")
            lbl1.place(x = 710, y = 100)
            lbl1.configure(font=("Bahnschrift", 18))

            global c_nameEntry 
            clicked = StringVar()
            options = ["U.S.A", "Nigeria", "Canada"]
            global c_nameEntry 
            c_nameEntry  =ttk.Combobox (frame_childbar, values =options, textvariable = clicked)
            c_nameEntry .place(x=710, y=130, width=200, height= 50)


            lblr = ctk.CTkLabel(frame_childbar, text="Abuse_ID:")
            lblr.place(x = 940, y = 100)
            lblr.configure(font=("Bahnschrift", 18))

            abuse_id = ctk.CTkEntry(frame_childbar, width=200, height= 50)
            abuse_id.place(x=940, y=130)

            lbl1 = ctk.CTkLabel(frame_childbar, text='Address:')
            lbl1.place(x = 23, y = 200)
            lbl1.configure(font=("Bahnschrift", 18))

            ads_nameEntry = ctk.CTkEntry(frame_childbar, placeholder_text="Child's Address",  width=435, height= 50)
            ads_nameEntry.place(x=23, y=230)

            ################################## Father's Registeration page ###############################################
            ##################################

            lbl1 = ctk.CTkLabel(frame_childbar, text="Father's First Name:")
            lbl1.place(x = 480, y = 200)
            lbl1.configure(font=("Bahnschrift", 18))

            father_nameEntry = ctk.CTkEntry(frame_childbar, placeholder_text="Father's First Name", width=200, height= 50)
            father_nameEntry.place(x=480, y=230)

            lbl1 = ctk.CTkLabel(frame_childbar, text= "Father's Last Name:")
            lbl1.place(x = 710, y = 200)
            lbl1.configure(font=("Bahnschrift", 18))

            father_last_nameEntry = ctk.CTkEntry(frame_childbar, placeholder_text="Father's Last Name", width=200, height= 50)
            father_last_nameEntry.place(x=710, y=230)

            lbl1 = ctk.CTkLabel(frame_childbar, text="Father's State:")
            lbl1.place(x = 940, y = 200)
            lbl1.configure(font=("Bahnschrift", 18))

            f_s_nameEntry = ctk.CTkEntry(frame_childbar, placeholder_text="Father's State", width=200, height= 50)
            f_s_nameEntry.place(x=940, y=230)

            lbl1 = ctk.CTkLabel(frame_childbar, text="Father's Country:")
            lbl1.place(x = 23, y = 300)
            lbl1.configure(font=("Bahnschrift", 18))

            global f_c_nameEntry 
            clicked = StringVar()
            options = ["U.S.A", "Nigeria", "Canada"]
            global f_c_nameEntry 
            f_c_nameEntry  =ttk.Combobox (frame_childbar, values =options, textvariable = clicked)
            f_c_nameEntry .place(x=23, y=330, width=200, height= 50)

            # f_c_nameEntry = ctk.CTkEntry(frame_childbar, placeholder_text="Father's Country", width=200, height= 50)
            # f_c_nameEntry.place(x=710, y=330)

            lbl1 = ctk.CTkLabel(frame_childbar, text="Father's Phone:")
            lbl1.place(x = 250, y = 300)
            lbl1.configure(font=("Bahnschrift", 18))

            father_phone = ctk.CTkEntry(frame_childbar, placeholder_text="Father's Phone", width=200, height= 50)
            father_phone.place(x=250, y=330)

            lbl1 = ctk.CTkLabel(frame_childbar, text= "Father's Email:")
            lbl1.place(x = 480, y = 300)
            lbl1.configure(font=("Bahnschrift", 18))

            father_email = ctk.CTkEntry(frame_childbar, placeholder_text="Father's Email", width=200, height= 50)
            father_email.place(x=480, y=330)

            lbl1 = ctk.CTkLabel(frame_childbar, text= "Father's Address:")
            lbl1.place(x = 710, y = 300)
            lbl1.configure(font=("Bahnschrift", 18))

            f_ads_nameEntry = ctk.CTkEntry(frame_childbar, placeholder_text="Father's Address",  width=450, height= 50)
            f_ads_nameEntry.place(x=710, y=330)
            
            ###################################### Mother Detail Taking ##############################################
            #####################################

            lbl1 = ctk.CTkLabel(frame_childbar, text="Mother's First Name:")
            lbl1.place(x = 23, y = 400)
            lbl1.configure(font=("Bahnschrift", 18))

            mother_nameEntry = ctk.CTkEntry(frame_childbar, placeholder_text="Mother's First Name", width=200, height= 50)
            mother_nameEntry.place(x=23, y=430)

            lbl1 = ctk.CTkLabel(frame_childbar, text= "Mother's Last Name:")
            lbl1.place(x = 250, y = 400)
            lbl1.configure(font=("Bahnschrift", 18))

            mother_last_nameEntry = ctk.CTkEntry(frame_childbar, placeholder_text="Mother's Last Name", width=200, height= 50)
            mother_last_nameEntry.place(x=250, y=430)

            lbl1 = ctk.CTkLabel(frame_childbar, text="Mother's State:")
            lbl1.place(x = 480, y = 400)
            lbl1.configure(font=("Bahnschrift", 18))

            m_s_nameEntry = ctk.CTkEntry(frame_childbar, placeholder_text="Mother's State", width=200, height= 50)
            m_s_nameEntry.place(x=480, y=430)

            lbl1 = ctk.CTkLabel(frame_childbar, text="Mother's Country:")
            lbl1.place(x = 710, y = 400)
            lbl1.configure(font=("Bahnschrift", 18))

            global m_c_nameEntry 
            clicked = StringVar()
            options = ["U.S.A", "Nigeria", "Canada"]
            global m_c_nameEntry 
            m_c_nameEntry  =ttk.Combobox (frame_childbar, values =options, textvariable = clicked)
            m_c_nameEntry .place(x=710, y=430, width=200, height= 50)

            # m_c_nameEntry = ctk.CTkEntry(frame_childbar, placeholder_text="Mother's Country", width=200, height= 50)
            # m_c_nameEntry.place(x=710, y=530)

            lbl1 = ctk.CTkLabel(frame_childbar, text="Mother's Phone:")
            lbl1.place(x = 940, y = 400)
            lbl1.configure(font=("Bahnschrift", 18))

            mother_phone = ctk.CTkEntry(frame_childbar, placeholder_text="Mother's Phone", width=200, height= 50)
            mother_phone.place(x=940, y=430)

            lbl1 = ctk.CTkLabel(frame_childbar, text= "Mother's Email:")
            lbl1.place(x = 23, y = 500)
            lbl1.configure(font=("Bahnschrift", 18))

            mother_email = ctk.CTkEntry(frame_childbar, placeholder_text="Last Name", width=200, height= 50)
            mother_email.place(x=23, y=530)

            lbl1 = ctk.CTkLabel(frame_childbar, text= "Mother's Address:")
            lbl1.place(x = 250, y = 500)
            lbl1.configure(font=("Bahnschrift", 18))

            m_ads_nameEntry = ctk.CTkEntry(frame_childbar, placeholder_text="Mother's Address",  width=450, height= 50)
            m_ads_nameEntry.place(x=250, y=530)

            btn_child_register = ctk.CTkButton(frame_childbar, text='Click To Register Child', width=1150, height=50, command=lambda:child_reg_query())
            btn_child_register.place(x = 23, y = 620)
            btn_child_register.configure(font=("Bahnschrift", 18))

            # def child_picture():
                
            #     global img_child 
            #     f_types = [('Jpg Files', '*.jpg'), ('Png Files', '*.png')]
            #     filename = filedialog.askopenfilename(filetypes=f_types)
            #     with open(filename, 'rb') as file:
            #         img_child= file.read()

                # image= img_child.resize((508,575))
                # img = ImageTk.PhotoImage(image)
                

            def child_reg_query():
                child_f_name = f_nameEntry.get().upper()
                child_l_name = l_nameEntry.get().upper()
                child_state = s_nameEntry.get().upper()
                child_country = c_nameEntry.get().upper()
                id_child = abuse_id.get().upper()
                child_add = ads_nameEntry.get().upper()
                f_f_name = father_nameEntry.get().upper()
                f_l_name = father_last_nameEntry.get().upper()
                f_phone = father_phone.get()
                f_email = father_email.get()
                f_country = f_c_nameEntry.get().upper()
                f_state = f_s_nameEntry.get().upper()
                f_add = f_ads_nameEntry.get().upper()
                m_f_name = mother_nameEntry.get().upper()
                m_l_name = mother_last_nameEntry.get().upper()
                m_phone = mother_phone.get()
                m_email = mother_email.get()
                m_state = m_s_nameEntry.get().upper()
                m_country = m_c_nameEntry.get().upper()
                m_add = m_ads_nameEntry.get().upper()                    

                current_date = datetime.now()
                now_date =current_date.date()

                if child_f_name == '' or child_l_name  == '' or child_state  == '' or child_country  == '' or child_add == '' or f_f_name  == '' or f_l_name  == '' or f_phone  == '' or f_email  == '' or f_state  == '' or f_country  == '' or f_add  == '' or m_f_name  == '' or m_l_name  == '' or m_phone  == '' or m_email  == '' or m_state  == '' or m_country  == '' or m_add  == '' or id_child  == '' or now_date  == '':
                    messagebox.showerror("Error", "Incomplete Details")
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
                        query_child = """CREATE TABLE if not exists child_reg (
                                        id INT AUTO_INCREMENT PRIMARY KEY,
                                        child_first_name VARCHAR(50),
                                        child_last_name VARCHAR(50),
                                        child_state VARCHAR(50) NOT NULL,
                                        child_country VARCHAR(30) NOT NULL,
                                        child_address VARCHAR(1000),
                                        father_first_name VARCHAR(50),
                                        father_last_name VARCHAR(50),
                                        father_phone VARCHAR(15) NOT NULL,
                                        father_email VARCHAR(50) NOT NULL,
                                        father_state VARCHAR(50) NOT NULL,
                                        father_country VARCHAR(20) NOT NULL,
                                        father_address text(500),
                                        mother_first_name VARCHAR(50),
                                        mother_last_name VARCHAR(50),
                                        mother_phone VARCHAR(15) NOT NULL,
                                        mother_email VARCHAR(50) NOT NULL,
                                        mother_state VARCHAR(50) NOT NULL,
                                        mother_country VARCHAR(30) NOT NULL,
                                        mother_address text(500),
                                        abuse_id VARCHAR(200), 
                                        date VARCHAR(11) NOT NULL,
                                        )"""
                        cursor.execute(query_child)
                        mydb.commit()
                        insert_table = """INSERT INTO child_reg(
                                        child_first_name, child_last_name,child_state, child_country, child_address,
                                        father_first_name, father_last_name, father_phone, father_email, father_state, father_country, father_Address,
                                        mother_first_name, mother_last_name, mother_phone, mother_email, mother_state, mother_country,mother_address,
                                        abuse_id,date)
                                        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                        vals = (child_f_name, child_l_name,child_state, child_country, child_add, f_f_name, f_l_name,f_phone, f_email,
                                f_state, f_country, f_add,m_f_name, m_l_name, m_phone, m_email, m_state, m_country, m_add,id_child, now_date)
                        cursor.execute(insert_table, vals)
                        mydb.commit()
                        mydb.close()
                        messagebox.showinfo("REGISTERED", "CHILD HAS BEEN REGISTERED SUCCESSFULLY")
                    except Exception as e:
                        messagebox.showerror("Error", e)
                        # "An Unexpected Error Occured, Contact Developer"
            
        reg_children()
        def reg_abuse():
            frame_abusebar = Frame(frame_body,width=width, height=height, bg='white')
            frame_abusebar.place(x=306, y=0)

            lblr = Label(frame_abusebar, text='Record New Abuse', bg='white')
            lblr.place(x = 23, y = 30)
            lblr.config(font=("Bahnschrift", 15))

            lblr = ctk.CTkLabel(frame_abusebar, text="Abuse_ID:")
            lblr.place(x = 23, y = 80)
            lblr.configure(font=("Bahnschrift", 18))

            abuse_list = []
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
                    abuse_list.append(j[20])


            global abuse_reg_id
            clicked = StringVar()
            global abuse_reg_id
            abuse_reg_id =ttk.Combobox (frame_abusebar, values = abuse_list, textvariable = clicked)
            abuse_reg_id.place(x=23, y=110, width=200, height= 50)

            lblr = ctk.CTkLabel(frame_abusebar, text= "Type Of Abuse:")
            lblr.place(x = 250, y = 80)
            lblr.configure(font=("Bahnschrift", 18))

            global type_abuse
            clicked = StringVar()
            options = ["Bullying and cyberbullying", "Child sexual exploitation","Child trafficking"," Domestic abuse",
                        "Emotional abuse"," Grooming", "Neglect", "Online Abuse", "Physical Abuse", "Sexual Abuse"]
            global type_abuse
            type_abuse =ttk.Combobox (frame_abusebar, values =options, textvariable = clicked)
            type_abuse.place(x=250, y=110, width=200, height= 50)

            # type_abuse = ctk.CTkEntry(frame_abusebar, width=200, height= 50)
            # type_abuse.place(x=250, y=110)

            lblr = ctk.CTkLabel(frame_abusebar, text="Abused Name(Child):")
            lblr.place(x = 480, y = 80)
            lblr.configure(font=("Bahnschrift", 18))

            child_name = ctk.CTkEntry(frame_abusebar, width=200, height= 50)
            child_name.place(x=480, y=110)

            lblr = ctk.CTkLabel(frame_abusebar, text="Abused Phone:")
            lblr.place(x = 710, y = 80)
            lblr.configure(font=("Bahnschrift", 18))

            abused_phone = ctk.CTkEntry(frame_abusebar, width=200, height= 50)
            abused_phone.place(x=710, y=110)

            lblr = ctk.CTkLabel(frame_abusebar, text= "Abused's Address:")
            lblr.place(x = 940, y = 80)
            lblr.configure(font=("Bahnschrift", 18))

            abused_adr = ctk.CTkEntry(frame_abusebar, width=200, height= 50)
            abused_adr.place(x=940, y=110)

            ###########################################################################################################

            lblr = ctk.CTkLabel(frame_abusebar, text="Abused Email:")
            lblr.place(x = 23, y = 180)
            lblr.configure(font=("Bahnschrift", 18))

            abuse_email = ctk.CTkEntry(frame_abusebar, width=200, height= 50)
            abuse_email.place(x=23, y=210)

            lblr = ctk.CTkLabel(frame_abusebar, text= "Abused State:")
            lblr.place(x = 250, y = 180)
            lblr.configure(font=("Bahnschrift", 18))

            abuse_state = ctk.CTkEntry(frame_abusebar, width=200, height= 50)
            abuse_state.place(x=250, y=210)

            lblr = ctk.CTkLabel(frame_abusebar, text="Abused Country:")
            lblr.place(x = 480, y = 180)
            lblr.configure(font=("Bahnschrift", 18))

            global abuse_country 
            clicked = StringVar()
            options = ["U.S.A", "Nigeria", "Canada"]
            global abuse_country 
            abuse_country  =ttk.Combobox (frame_abusebar, values =options, textvariable = clicked)
            abuse_country .place(x=480, y=210, width=200, height= 50)

            # abuse_country = ctk.CTkEntry(frame_abusebar, width=200, height= 50)
            # abuse_country.place(x=480, y=210)

            lblr = ctk.CTkLabel(frame_abusebar, text="Station Reported:")
            lblr.place(x = 710, y = 180)
            lblr.configure(font=("Bahnschrift", 18))

            report_station = ctk.CTkEntry(frame_abusebar, width=200, height= 50)
            report_station.place(x=710, y=210)

            lblr = ctk.CTkLabel(frame_abusebar, text= "Station Address:")
            lblr.place(x = 940, y = 180)
            lblr.configure(font=("Bahnschrift", 18))

            station_adr = ctk.CTkEntry(frame_abusebar, width=200, height= 50)
            station_adr.place(x=940, y=210)

            #################################################################################################################

            lblr = ctk.CTkLabel(frame_abusebar, text="Person Incharge:")
            lblr.place(x = 23, y = 270)
            lblr.configure(font=("Bahnschrift", 18))

            per_ic = ctk.CTkEntry(frame_abusebar, width=200, height= 50)
            per_ic.place(x=23, y=300)

            lblr = ctk.CTkLabel(frame_abusebar, text= "Person Incharge Phone:")
            lblr.place(x = 250, y = 270)
            lblr.configure(font=("Bahnschrift", 18))

            per_ic_phone = ctk.CTkEntry(frame_abusebar, width=200, height= 50)
            per_ic_phone.place(x=250, y=300)

            lblr = ctk.CTkLabel(frame_abusebar, text="Person Incharge Email:")
            lblr.place(x = 480, y = 270)
            lblr.configure(font=("Bahnschrift", 18))

            per_ic_email = ctk.CTkEntry(frame_abusebar, width=200, height= 50)
            per_ic_email.place(x=480, y=300)

            lblr = ctk.CTkLabel(frame_abusebar, text="Per_Incharge Address:")
            lblr.place(x = 710, y = 270)
            lblr.configure(font=("Bahnschrift", 18))

            per_ic_adr = ctk.CTkEntry(frame_abusebar, width=200, height= 50)
            per_ic_adr.place(x=710, y=300)

            lblr = ctk.CTkLabel(frame_abusebar, text= "Person Incharge State:")
            lblr.place(x = 940, y = 270)
            lblr.configure(font=("Bahnschrift", 18))

            per_ic_state = ctk.CTkEntry(frame_abusebar, width=200, height= 50)
            per_ic_state.place(x=940, y=300)

            ##########################################################################################################

            lblr = ctk.CTkLabel(frame_abusebar, text="Person Incharge Country:")
            lblr.place(x = 23, y = 360)
            lblr.configure(font=("Bahnschrift", 18))

            global per_ic_country 
            clicked = StringVar()
            options = ["U.S.A", "Nigeria", "Canada"]
            global per_ic_country 
            per_ic_country  =ttk.Combobox (frame_abusebar, values =options, textvariable = clicked)
            per_ic_country .place(x = 23, y = 390, width=200, height= 50)

            # per_ic_country = ctk.CTkEntry(frame_abusebar, width=200, height= 50)
            # per_ic_country.place(x=23, y=390)

            lblr = ctk.CTkLabel(frame_abusebar, text= "Reporter's Name:")
            lblr.place(x = 250, y = 360)
            lblr.configure(font=("Bahnschrift", 18))

            reporter = ctk.CTkEntry(frame_abusebar, width=200, height= 50)
            reporter.place(x=250, y=390)

            lblr = ctk.CTkLabel(frame_abusebar, text="Reporter's Phone:")
            lblr.place(x = 480, y = 360)
            lblr.configure(font=("Bahnschrift", 18))

            reporter_phone = ctk.CTkEntry(frame_abusebar, width=200, height= 50)
            reporter_phone.place(x=480, y=390)

            lblr = ctk.CTkLabel(frame_abusebar, text="Reporter's Email:")
            lblr.place(x = 710, y = 360)
            lblr.configure(font=("Bahnschrift", 18))

            reporter_email = ctk.CTkEntry(frame_abusebar, width=200, height= 50)
            reporter_email.place(x=710, y=390)

            lblr = ctk.CTkLabel(frame_abusebar, text= "Reporter's Address:")
            lblr.place(x = 940, y = 360)
            lblr.configure(font=("Bahnschrift", 18))

            reporter_adr = ctk.CTkEntry(frame_abusebar, width=200, height= 50)
            reporter_adr.place(x=940, y=390)

            #################################################################################################################3

            lblr = ctk.CTkLabel(frame_abusebar, text="Reporter's State:")
            lblr.place(x = 23, y = 460)
            lblr.configure(font=("Bahnschrift", 18))

            reporter_state = ctk.CTkEntry(frame_abusebar, width=200, height= 50)
            reporter_state.place(x=23, y=490)

            lblr = ctk.CTkLabel(frame_abusebar, text="Reporter's Country:")
            lblr.place(x = 250, y = 460)
            lblr.configure(font=("Bahnschrift", 18))

            reporter_country = ctk.CTkEntry(frame_abusebar, width=200, height= 50)
            reporter_country.place(x=250, y=490)

            lblr = ctk.CTkLabel(frame_abusebar, text= "Case Status:")
            lblr.place(x = 480, y = 460)
            lblr.configure(font=("Bahnschrift", 18))
            
            clicked = StringVar()
            options = ["Pending", "Solved", "Unsolved"]
            global abuse_status
            abuse_status =ttk.Combobox (frame_abusebar, values =options, textvariable = clicked)
            abuse_status.place(x=480, y=490, width=200, height= 50)
            
            # abuse_status = ctk.CTkEntry(frame_abusebar, width=200, height= 50)
            # abuse_status.place(x=480, y=490)

            btn_abuse_register = ctk.CTkButton(frame_abusebar, text='SUBMIT', width=1120, height=50, command=lambda:abuse_reg_query())
            btn_abuse_register.place(x = 23, y = 560)
            btn_abuse_register.configure(font=("Bahnschrift", 20))

            def abuse_reg_query():
                
                abuse_id = abuse_reg_id.get().upper()
                type = type_abuse.get().upper()
                cname = child_name.get().upper()
                cphone = abused_phone.get()
                caddr = abused_adr.get().upper()
                cemail = abuse_email.get()
                cstate = abuse_state.get().upper()
                ccountry = abuse_country.get().upper()
                station = report_station.get().upper()
                saddr = station_adr.get().upper()
                pname = per_ic.get().upper()
                pphone = per_ic_phone.get()
                pemail = per_ic_email.get()
                paddr = per_ic_adr.get().upper()
                pstate = per_ic_state.get().upper()
                pcountry = per_ic_country.get().upper()
                rname = reporter.get().upper()
                rphone = reporter_phone.get()
                remail = reporter_email.get()
                raddr = reporter_adr.get().upper()
                rstate =reporter_state.get().upper()
                rcountry = reporter_country.get().upper()
                status = abuse_status.get().upper()

                current_date = datetime.now()
                now_date =current_date.date()

                if abuse_id == '' or type  == '' or cname  == '' or cphone  == '' or caddr  == '' or cemail  == '' or cstate  == '' or ccountry  == '' or station  == '' or saddr  == '' or pname  == '' or pphone  == '' or pemail  == '' or paddr  == '' or pstate  == '' or pcountry  == '' or rname  == '' or rphone  == '' or remail  == '' or raddr  == '' or rstate  == '' or rcountry  == '' or now_date  == '' or status  == '':
                    messagebox.showerror("Error", "Incomplete Details")
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
                        query_abuse = """CREATE TABLE if not exists abuse_reg (
                                        id INT AUTO_INCREMENT PRIMARY KEY,
                                        abuse_id VARCHAR(50),
                                        type_abuse VARCHAR(50),
                                        abused_name VARCHAR(50) NOT NULL,
                                        abused_phone VARCHAR(30) NOT NULL,
                                        abused_address VARCHAR(1000),
                                        abused_email VARCHAR(50),
                                        abused_state VARCHAR(50),
                                        abused_country VARCHAR(30) NOT NULL,
                                        station_reported VARCHAR(100) NOT NULL,
                                        station_address VARCHAR(50) NOT NULL,
                                        person_incharge VARCHAR(50) NOT NULL,
                                        person_phone text(500),
                                        person_email VARCHAR(50),
                                        person_address TEXT(500),
                                        person_state VARCHAR(50) NOT NULL,
                                        person_country VARCHAR(30) NOT NULL,
                                        reporter_name VARCHAR(80) NOT NULL,
                                        reporter_phone VARCHAR(15) NOT NULL,
                                        reporter_email text(50),
                                        reporter_address VARCHAR(500), 
                                        reporter_state text(50),
                                        reporter_country text(30),
                                        date VARCHAR(11) NOT NULL,
                                        status text(15)
                                        
                                        )"""
                        cursor.execute(query_abuse)
                    
                        mydb.commit()
                        insert_table = """INSERT INTO abuse_reg(
                                        abuse_id, type_abuse, abused_name, abused_phone, abused_address, abused_email, abused_state, abused_country,
                                        station_reported, station_address, person_incharge, person_phone, person_email, person_address, person_state,
                                        person_country, reporter_name, reporter_phone, reporter_email, reporter_address, reporter_state, 
                                        reporter_country, date, status )
                                        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                        vals = (abuse_id, type, cname, cphone, caddr, cemail, cstate, ccountry,station, saddr, pname, 
                                pphone, pemail, paddr, pstate, pcountry, rname, rphone, remail, raddr, rstate, rcountry, now_date, status)
                        cursor.execute(insert_table, vals)
                        mydb.commit()
                        messagebox.showinfo("SUCCESS", "ABUSE REGISTERED SUCCESSFULLY")
                        mydb.close()
                    except Exception as e:
                        messagebox.showerror("Error", "An Unexpected Error Occured, Contact Developer")


    ############################################                   ###########################################################
    ####################################                                ##################################################
    ##################################            LOGIN SECTION         ###############################################

    global login
    def login():
        frame_log = Frame(root,width=width, height=height, bg='black')
        frame_log.grid(row=1, column = 0)

        frame_log1 = Frame(frame_log,width=width//3, height=height//1.5, bg='black')
        frame_log1.place(x=220, y= 50)

        img= (Image.open("l_img.png"))
        image= img.resize((508,575))

        global new_image
        new_image= ImageTk.PhotoImage(image)
        
        label1 = Label(frame_log1, image=new_image, bg='black')
        label1.place(x=0, y= 0)


        ##################################### THis is the login section for input ###########################################
        ##################################
        
        frame_log2 = Frame(frame_log,width=width//3, height=height//1.5, bg='#ADD8E6')
        frame_log2.place(x=780, y = 50)

        lbl_title= ctk.CTkLabel(frame_log2, text="Login Page")
        lbl_title.place(x= 170, y= 30)
        lbl_title.configure(font=('calibre',25,'normal'))

        lbl_name= ctk.CTkLabel(frame_log2, text="Email")
        lbl_name.place(x=25, y= 100)
        lbl_name.configure(font=("Bahnschrift", 18))

        entry_mail = ctk.CTkEntry(frame_log2, height=45, width=350)
        entry_mail.place(x =25, y = 140)
        entry_mail.configure(font=('calibre',12,'normal'))

        lbl_user= ctk.CTkLabel(frame_log2, text="Username")
        lbl_user.place(x=25, y=200)
        lbl_user.configure(font=("Bahnschrift", 18))

        global entry_user
        entry_user = ctk.CTkEntry(frame_log2, height=45, width=350)
        entry_user.place(x =25, y = 240)
        entry_user.configure(font=('calibre',12,'normal'))

        lbl_pass= ctk.CTkLabel(frame_log2, text="Password")
        lbl_pass.place(x=25, y=300)
        lbl_pass.configure(font=("Bahnschrift", 18))

        global entry_pass
        entry_pass = ctk.CTkEntry(frame_log2, height=45, width=350)
        entry_pass.place(x =25, y = 340)
        entry_pass.configure(font=('calibre',12,'normal'))

        btn_login = ctk.CTkButton(frame_log2, text='Login', height=45, width=350, command=lambda:log_fuction())
        btn_login.place(x=25, y= 450)
        btn_login.configure(font=('calibre',12,'normal'))

        def log_fuction():
                email = entry_mail.get()
                user = entry_user.get()
                password = entry_pass.get()

                mydb = mysql.connector.connect(
                        host = "localhost",
                        user= "root",
                        password = "",
                        port= 3306,
                        database="childdb"
                        )
                cursor = mydb.cursor() 
                log_rec = """ SELECT * FROM auth_reg"""
                cursor.execute(log_rec)
                results_one = cursor.fetchall()
                for result in results_one:
                    email_reg = result[2]
                    user_reg = result[4]
                    pass_reg = result[5]                       
                    if email != email_reg and user != user_reg and password != pass_reg:
                        ask = messagebox.askyesno("Error Login in", "You Are Not Registered...\nDO You Want to Register AS Admin?")
                        if ask:
                            Auth()
                        else:
                            pass
                    else:
                        adminbar()

                        
                mydb.commit()
                mydb.close()

        # btn_login = ctk.CTkButton(frame_log2, text='Click Here To Register As Admin', height=45, width=450, command=lambda:adminbar())
        # btn_login.place(x=25, y= 450)
        # btn_login.configure(font=('calibre',12,'normal'))


    ############################################ ADMIN BAR SECTION ###########################################################
        ####################################                                ##################################################
        ##################################                                     ###############################################

    def adminbar():
        frame_admin = Frame(root, width=width,height=height, bg='black')
        frame_admin.grid(row=1, column = 0)

        frame_sidebar = Frame(frame_admin, width=width//5,height=height, bg='black', relief=RAISED)
        frame_sidebar.place(x = 50, y = 0)

        global btn_dash
        btn_dash = Menubutton(frame_sidebar, text="Dashboard",relief=RAISED,  bg='black', fg='white')
        btn_dash.pack(side='top', ipadx=50, ipady=15, pady=10)
        btn_dash.config(font=("Bahnschrift", 13))
        btn_dash.menu = Menu(btn_dash, tearoff = 0)
        btn_dash.menu.config(font=("Bahnschrift", 15))
        btn_dash["menu"] = btn_dash.menu

        btn_dash.menu.add_command(label="Dashboard", command=lambda:main())
        btn_dash.menu.add_command(label="Add Admin", command=lambda:Auth())
        btn_dash.menu.add_command(label="Edit Profile", command=lambda:Auth_edit())
        
        # btn_dash = Button(frame_sidebar, text='DashBoard', bg='black', fg='white', command=lambda:main())
        # btn_dash.pack(side='top', ipadx=40, ipady=15, pady=10)
        # btn_dash.config(font=("Bahnschrift", 15))

        btn_dash2 = Button(frame_sidebar, text='Children >>', background='black', fg='white', command=lambda:children())
        btn_dash2.pack(side='top', ipadx=40, ipady=15, pady=10)
        btn_dash2.config(font=("Bahnschrift", 15))

        btn_dash3 = Button(frame_sidebar, text='Abuse >>>>', bg='black', fg='white', command=lambda:abuse())
        btn_dash3.pack(side='top', ipadx=40, ipady=15, pady=10)
        btn_dash3.config(font=("Bahnschrift", 15))

        btn_dash = Button(frame_sidebar, text='Reports >>', bg='black', fg='white', command=lambda:report())
        btn_dash.pack(side='top', ipadx=40, ipady=15, pady=10)
        btn_dash.config(font=("Bahnschrift", 15))
      

        def main():
            frame_main = Frame(frame_admin,width=width, height=height, bg='white')
            frame_main.place(x=306, y=0)

            # img= (Image.open("icon.png"))
            # image= img.resize((30,26))

            # global new_image
            # new_image= ImageTk.PhotoImage(image)
            # image_label = Label(frame_main, image=new_image)
            # image_label.place(x = 23, y = 30)


            lbl1 = Label(frame_main, text='Dashboard', bg='white')
            lbl1.place(x = 23, y = 30)
            lbl1.config(font=("Bahnschrift", 18))

            lbl1 = Label(frame_main, text='Statistics', bg='white')
            lbl1.place(x = 146, y = 37)
            lbl1.config(font=("Bahnschrift", 13))

            lbl1 = Label(frame_main, text='Overview', bg='white')
            lbl1.place(x = 224, y = 37)
            lbl1.config(font=("Bahnschrift", 13))

            framing = Frame(frame_main, width=width//1.3, height = 45, bg='#ADD8E6')
            framing.place(x = 20, y = 90)

            img2= (Image.open("info-icon.png"))
            image2= img2.resize((30,26))

            global new_image2
            new_image2= ImageTk.PhotoImage(image2)
            image_label2 = Label(framing, image=new_image2, bg='#ADD8E6')
            image_label2.place(x = 10, y = 7)

            lbl2 = Label(framing, text='Child Abuse System For Keeping Records of Children And their Cases!', bg='#ADD8E6')
            lbl2.place(x = 50, y = 6)
            lbl2.config(font=("Bahnschrift", 15))

            ####################  Frame One ########################################################################
            frame1 = Frame(frame_main,width=width//5.5, height = height//4.5, bg='blue')
            frame1.place(x = 20, y = 150)

            img_1= (Image.open("chat.png"))
            image_1= img_1.resize((120,140))

            global new_image_1
            new_image_1= ImageTk.PhotoImage(image_1)
           
            lbl_fr_img = Label(frame1, image=new_image_1, bg='blue')
            lbl_fr_img.place(x = 0, y = 1)
            lbl_fr_img.config(font=("Bahnschrift", 13))

            def frame_one_fuction():
                mydb = mysql.connector.connect(
                        host = "localhost",
                        user= "root",
                        password = "",
                        port= 3306,
                        database="childdb"
                        )
                cursor = mydb.cursor() 
                frame_one_rec = """ SELECT count(id) FROM child_reg;"""
                cursor.execute(frame_one_rec)
                results_one = cursor.fetchall()
                for result in results_one:
                    for i in result:
                        child_row_num = i
                        
                mydb.commit()
                mydb.close()
                
                if child_row_num <10:
                    lbl_fr_2 = Label(frame1, text=child_row_num, bg='blue')
                    lbl_fr_2.place(x = 225, y = 1)
                    lbl_fr_2.config(font=("Bahnschrift", 50))
                elif child_row_num>9:
                    lbl_fr_2 = Label(frame1, text="9+", bg='blue')
                    lbl_fr_2.place(x = 210, y = 1)
                    lbl_fr_2.config(font=("Bahnschrift", 50))

                def framing_1():
                    
                    sms = messagebox.askyesno("CHILDREN DETAILS", "THERE ARE %s CHILDREN REGISTERED \nDO YOU WANT TO REVIEW THEM?"%(child_row_num))
                    if sms:
                        children()

                btn_fr_3 = Button(frame1, text='Details...', width=30, height=2, bg='white', bd=5, command=lambda:framing_1())
                btn_fr_3.place(x = 0, y = 130)
                btn_fr_3.config(font=("Bahnschrift", 13))
            frame_one_fuction()

            lbl_fr_3 = Label(frame1, text='Children', bg='blue')
            lbl_fr_3.place(x = 210, y = 100)
            lbl_fr_3.config(font=("Bahnschrift", 13))

            

            ############################# Frame Two #################################################################
            frame2 = Frame(frame_main,width=width//5.5, height = height//4.5, bg='#32CD32')
            frame2.place(x = 320, y = 150)

            img_2= (Image.open("stack.png"))
            image_2= img_2.resize((115,130))

            global new_image_2
            new_image_2= ImageTk.PhotoImage(image_2)

            lbl_fr1_2 = Label(frame2, image=new_image_2, bg='#32CD32')
            lbl_fr1_2.place(x = 0, y = 1)
            lbl_fr1_2.config(font=("Bahnschrift", 13))

            def frame_two_fuction():
                mydb = mysql.connector.connect(
                        host = "localhost",
                        user= "root",
                        password = "",
                        port= 3306,
                        database="childdb"
                        )
                cursor = mydb.cursor() 
                frame_two_rec = """ SELECT count(id) FROM abuse_reg WHERE status = 'PENDING';"""
                cursor.execute(frame_two_rec)
                results_one = cursor.fetchall()
                for result in results_one:
                    for i in result:
                        abuse_row_num = i
                    
                mydb.commit()
                mydb.close()
                
                if abuse_row_num <10:
                    lbl_fr2_2 = Label(frame2, text=abuse_row_num, bg='#32CD32')
                    lbl_fr2_2.place(x = 210, y = 1)
                    lbl_fr2_2.config(font=("Bahnschrift", 50))
                elif abuse_row_num>9:
                    lbl_fr2_2 = Label(frame2, text='9+', bg='#32CD32')
                    lbl_fr2_2.place(x = 225, y = 1)
                    lbl_fr2_2.config(font=("Bahnschrift", 50))

                def framing_2():
                    sms = messagebox.askyesno("ABUSE DETAILS", "THERE ARE %s ABUSE REGISTERED \nDO YOU WANT TO REVIEW THEM?"%(abuse_row_num))
                    if sms:
                        abuse()

                btn_fr1_3 = Button(frame2, text='Details...', width=30, height=2, bg='white', bd=5, command=lambda:framing_2())
                btn_fr1_3.place(x = 0, y = 130)
                btn_fr1_3.config(font=("Bahnschrift", 13))
            frame_two_fuction()

            lbl_fr3_2 = Label(frame2, text='Abuse',  bg='#32CD32')
            lbl_fr3_2.place(x = 210, y = 100)
            lbl_fr3_2.config(font=("Bahnschrift", 13))

            

            ############################# Frame Three #################################################################
            frame3 = Frame(frame_main,width=width//5.5, height = height//4.5, bg='#F4BB44')
            frame3.place(x = 620, y = 150)

            img_3= (Image.open("cart.png"))
            image_3= img_3.resize((115,140))

            global new_image_3
            new_image_3= ImageTk.PhotoImage(image_3)

            lbl_fr2_3 = Label(frame3, image= new_image_3, bg='#F4BB44')
            lbl_fr2_3.place(x = 0, y = 1)
            lbl_fr2_3.config(font=("Bahnschrift", 13))

            def frame_three_fuction():
                mydb = mysql.connector.connect(
                        host = "localhost",
                        user= "root",
                        password = "",
                        port= 3306,
                        database="childdb"
                        )
                cursor = mydb.cursor() 
                frame_three_rec = """ SELECT count(id) FROM abuse_reg;"""
                cursor.execute(frame_three_rec)
                results_one = cursor.fetchall()
                for result in results_one:
                    for i in result:
                        abuse_row_num = i
                      
                mydb.commit()
                mydb.close()
                
                if abuse_row_num <10:
                    lbl_fr3_3 = Label(frame3, text=abuse_row_num, bg='#F4BB44')
                    lbl_fr3_3.place(x = 225, y = 1)
                    lbl_fr3_3.config(font=("Bahnschrift", 50))
                elif abuse_row_num>9:
                    lbl_fr3_3 = Label(frame3, text='9+', bg='#F4BB44')
                    lbl_fr3_3.place(x = 210, y = 1)
                    lbl_fr3_3.config(font=("Bahnschrift", 50))

                def framing_3():
                    sms = messagebox.askyesno("ABUSE REPORTED", "THERE ARE %s CASES REPORTED \nDO YOU WANT REVIEW THEM?"%(abuse_row_num))
                    if sms:
                        report()

                btn_fr2_3 = Button(frame3, text='Details', width=30, height=2, bg='white', bd=5, command = lambda:framing_3())
                btn_fr2_3.place(x = 0, y = 130)
                btn_fr2_3.config(font=("Bahnschrift", 13))

            frame_three_fuction()

            lbl_fr4_3 = Label(frame3, text='Cases', bg='#F4BB44')
            lbl_fr4_3.place(x = 210, y = 100)
            lbl_fr4_3.config(font=("Bahnschrift", 13))

            

            ############################# Frame Four #################################################################
            frame4 = Frame(frame_main,width=width//5.5, height = height//4.5, bg='red')
            frame4.place(x = 920, y = 150)
            
            img_4= (Image.open("report.png"))
            image_4= img_4.resize((115,140))

            global new_image_4
            new_image_4= ImageTk.PhotoImage(image_4)

            lbl_fr3_4 = Label(frame4, image=new_image_4, bg='red')
            lbl_fr3_4.place(x = 0, y = 1)
            lbl_fr3_4.config(font=("Bahnschrift", 13))

            

            lbl_fr5_4 = Label(frame4, text='Resolved', bg='red')
            lbl_fr5_4.place(x = 200, y = 100)
            lbl_fr5_4.config(font=("Bahnschrift", 13))

            

            def frame_four_fuction():
                mydb = mysql.connector.connect(
                        host = "localhost",
                        user= "root",
                        password = "",
                        port= 3306,
                        database="childdb"
                        )
                cursor = mydb.cursor() 
                frame_four_rec = """ SELECT count(id) FROM abuse_reg WHERE status = 'SOLVED' ;"""
                cursor.execute(frame_four_rec)
                results_two = cursor.fetchall()
                for results in results_two:
                    for i in results:
                        resolved_row_num = i
                      
                mydb.commit()
                mydb.close()
                
                if resolved_row_num <10:
                    lbl_fr4_4 = Label(frame4, text=resolved_row_num, bg='red')
                    lbl_fr4_4.place(x = 210, y = 1)
                    lbl_fr4_4.config(font=("Bahnschrift", 50))
                elif resolved_row_num>9:
                    lbl_fr4_4 = Label(frame4, text='9+', bg='red')
                    lbl_fr4_4.place(x = 210, y = 1)
                    lbl_fr4_4.config(font=("Bahnschrift", 50))

                def framing_4():
                    sms = messagebox.askyesno("ABUSE REPORTED", "THERE ARE %s CASES REPORTED \nDO YOU WANT REVIEW THEM?"%(resolved_row_num))
                    if sms:
                        report()

                btn_fr2_4 = Button(frame4, text='Details', width=30, height=2, bg='white', bd=5, command = lambda:framing_4())
                btn_fr2_4.place(x = 0, y = 130)
                btn_fr2_4.config(font=("Bahnschrift", 13))

            frame_four_fuction()




            #####################################################################
            ##############################################################################

            lbl_title = Label(frame_main, text='Lists of Cases', bg='#E1D9D1', width=130)
            lbl_title.place(x = 20, y = 360)
            lbl_title.config(font=("Bahnschrift", 12))

            game_scroll = Scrollbar(frame_main,orient='vertical', width=30)
            game_scroll.place(x = (width//1.3)-16, y= 390)

            global table_dash
            table_dash = ttk.Treeview(frame_main, style="mystyle.Treeview", yscrollcommand=game_scroll.set)
            table_dash['columns']= ("S/N", "Date", "Abuse ID", "Type Of Abuse", "Abuse Name", "Reporter", "Reported To", "Status")
            table_dash.column("#0", width=0, stretch=NO)
            table_dash.column("S/N", width=10, anchor = CENTER)
            table_dash.column("Date", width=80, anchor = CENTER)
            table_dash.column("Abuse ID", width=80, anchor = CENTER)
            table_dash.column("Type Of Abuse", width=80, anchor = CENTER)
            table_dash.column("Abuse Name", width=80, anchor = CENTER)
            table_dash.column("Reporter", width=80, anchor = CENTER)
            table_dash.column("Reported To", width=80, anchor = CENTER)
            table_dash.column("Status", width=80, anchor = CENTER)
            table_dash.place(x = 20, y= 390, width= (width//1.3)-40,  height = 650)
            table_dash.heading("S/N", text = "S/N")
            table_dash.heading("Date", text = "Date")
            table_dash.heading("Abuse ID", text = "Abuse ID")
            table_dash.heading("Type Of Abuse", text = "Type Of Abuse")
            table_dash.heading("Abuse Name", text = "Abuse Name")
            table_dash.heading("Reporter", text = "Reporter")
            table_dash.heading("Reported To", text = "Reported To")
            table_dash.heading("Status", text = "Status")

            style =ttk.Style()
            font1 = ['Times',12, 'normal']
            font2 = ['Times',10, 'normal']
            style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=font2)
            style.configure("mystyle.Treeview.Heading",font=font1)
            style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])

            def main_admin_query():
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
                    for i in results:
                        table_dash.insert("",'end', values=(i[0], i[23], i[1], i[2], i[3], i[17], i[9], i[24]))
                mydb.commit()
                mydb.close()


            main_admin_query()


        ###################################  Main Frame for Children Section ######################################
        ################################
        #############################
        ##########################

        def children():
            frame_childbar = Frame(frame_admin,width=width, height=height, bg='white')
            frame_childbar.place(x=306, y=0)

            lbl1 = Label(frame_childbar, text='Children', bg='white')
            lbl1.place(x = 23, y = 30)
            lbl1.config(font=("Bahnschrift", 18))

            lbl1 = Label(frame_childbar, text='Lists of Children', bg='white')
            lbl1.place(x = 120, y = 37)
            lbl1.config(font=("Bahnschrift", 13))

            btn1 = Button(frame_childbar, text='Insert New Record', width=17, height=2, bg='#ADD8E6', command=lambda:popupmsg_child())
            btn1.place(x = 23, y = 80)
            btn1.config(font=("Bahnschrift", 11))

            lbl2 = Label(frame_childbar, text='Lists of Children', bg='#E1D9D1', width=129)
            lbl2.place(x = 23, y = 155)
            lbl2.config(font=("Bahnschrift", 12))

            game_scroll = Scrollbar(frame_childbar,orient='vertical', width=30)
            game_scroll.place(x = (width//1.3)-16, y= 185)
            

            global table_dash
            table_dash = ttk.Treeview(frame_childbar, style="mystyle.Treeview", yscrollcommand=game_scroll.set)
            table_dash['columns']= ("S/N", "Date", "Names", "Abuse ID", "State", "Country")
            table_dash.column("#0", width=0, stretch=NO)
            table_dash.column("S/N", width=10, anchor = CENTER)
            table_dash.column("Date", width=80, anchor = CENTER)
            table_dash.column("Names", width=80, anchor = CENTER)
            table_dash.column("Abuse ID", width=80, anchor = CENTER)
            table_dash.column("State", width=80, anchor = CENTER)
            table_dash.column("Country", width=80, anchor = CENTER)
            
            table_dash.place(x = 20, y= 185, width= (width//1.3)-40,  height = 650)
            table_dash.heading("S/N", text = "S/N")
            table_dash.heading("Date", text = "Date")
            table_dash.heading("Names", text = "Names")
            table_dash.heading("Abuse ID", text = "Abuse ID")
            table_dash.heading("State", text = "State")
            table_dash.heading("Country", text = "Country")

            def delete():
                if table_dash.focus():
                    # Get selected item to Delete
                    selected_item = table_dash.selection()[0]
                    askdel = messagebox.askyesno("Confirmation", "Do you want to Delete this Record?")
                    if askdel:
                        table_dash.delete(selected_item)
                        messagebox.showinfo("INFO", "For Security and unbaised Purpose,\nData will only be deleted on table but preserved on database")
                    else:
                        pass
                else:
                    messagebox.showwarning("Alert", "Select A Row To Delete")

            

            def view():
                if table_dash.focus():
                    import customtkinter as ctk
                    import mysql.connector
                    from datetime import datetime
                    from tkinter import messagebox, ttk
                    
                    from PIL import ImageTk, Image

                    
                    popup = Tk()
                    popup.wm_title("!")
                    popup.attributes('-topmost', True)

                    try:
                        # windows only (remove the minimize/maximize button)
                        popup.attributes('-toolwindow', True)
                    except TclError:
                        pass

                    frame2 = Frame(popup, width=550, height=260)
                    frame2.grid(row=0, column=0)

                    detail = []
                    # Get selected item to Edit
                    selected_item = table_dash.focus()
                    details = table_dash.item(selected_item)
                    detailing = details.get("values")[0]
                    
                    detail.append(detailing)     
                    

                    mydb = mysql.connector.connect(
                            host = "localhost",
                            user= "root",
                            password = "",
                            port= 3306,
                            database="childdb"
                            )
                    cursor = mydb.cursor() 
                    view_rec = """ SELECT * FROM child_reg WHERE id = %s"""
                    
                    val2 = (detail)
                    cursor.execute(view_rec, val2)
                    results = cursor.fetchall()
                    if results == "":
                        pass
                    else:
                        for r in results:
                            names = r[2]
                            name = r[1]
                            c_state = r[3]
                            c_country = r[4] 
                            father = r[6]
                            father2 = r[7]
                            mother = r[13]
                            mother2 = r[12]
                            f_country = r[11]
                            m_country = r[18]
                            a_id = r[20]

                            
                            
                            message = """
                    A case was reported of whose the victim name is {} {}
                    from {} state in {}.
                    \n
                    The Father of The Child is {} {} from {}.
                    While The Mother's Name is {} {} from {}.\n
                    For Further Enquiry On The Abused,
                    Check Report on Abuse With Abuse ID {}
                    
                    """.format(names,name,c_state,c_country,father2,father,f_country,mother2,mother, m_country,a_id)
                        
                    # imaging = Image.open(BytesIO(pic))
                    # print(imaging)
                    # image1= imaging.resize((120,150))
                    # global img_child
                    # img_child = ImageTk.PhotoImage(image1)
                    # lbl_img = Label(frame1, image=img_child)
                    # lbl_img.place(x = 0, y = 0)
                    

                    lbl = Label(frame2, text=message)
                    lbl.place(x = 5, y = 20)
                    lbl.config(font=("Bahnschrift", 11))

                    popup.mainloop()
                else:
                    from tkinter import messagebox
                    messagebox.showwarning("Alert", "Select A Row To View")

            def edit():
                if table_dash.focus():
                    import customtkinter as ctk
                    from tkinter import messagebox
                    from datetime import datetime
                    import mysql.connector
                    from tkinter import ttk

                    
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

                    detail = []
                    # Get selected item to Edit
                    selected_item = table_dash.focus()
                    details = table_dash.item(selected_item)
                    detailing = details.get("values")[0]

                    detail.append(detailing)
            

                    mydb = mysql.connector.connect(
                            host = "localhost",
                            user= "root",
                            password = "",
                            port= 3306,
                            database="childdb"
                            )
                    cursor = mydb.cursor() 
                    view_rec = """ SELECT * FROM child_reg WHERE id = %s"""
                    val = (detail)
                    cursor.execute(view_rec, val)
                    results = cursor.fetchall()
                    for j in results:
                        first_name.insert(0, j[1])
                        last_name.insert(0, j[2])
                        state.insert(0, j[3])
                        country.insert(0, j[4])
                        address.insert(0, j[5])
                        father_name.insert(0, j[6])
                        father_phone.insert(0, j[8])
                        father_email.insert(0, j[9])
                        father_state.insert(0, j[10])
                        father_country.insert(0, j[11])
                        father_address.insert(0, j[12])
                        mother_name.insert(0, j[13])
                        mother_phone.insert(0, j[15])
                        mother_email.insert(0, j[16])
                        mother_state.insert(0, j[17])
                        mother_country.insert(0, j[18])
                        mother_address.insert(0, j[19])
                        abuse_id.insert(0, j[20])


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
                        

                        try:
                            mydb = mysql.connector.connect(
                                    host = "localhost",
                                    user= "root",
                                    password = "",
                                    port= 3306,
                                    database="childdb"
                                    )
                            cursor = mydb.cursor() 
                            for indetail in detail:
                                indetail = str(indetail)
                                print(indetail)
                                insert_table = """UPDATE child_reg
                                                    SET
                        
                                                    child_first_name = %s, child_last_name = %s,child_state = %s, child_country = %s, child_address = %s,
                                                    father_last_name = %s, father_phone = %s, father_email = %s, father_state = %s, father_country = %s, father_Address = %s,
                                                    mother_last_name = %s, mother_phone = %s, mother_email = %s, mother_state = %s, mother_country = %s,mother_address = %s,
                                                    abuse_id = %s
                                                    WHERE id = %s
                                                    """
                                vals = (child_f_name, child_l_name,child_state, child_country, child_add, f_f_name,f_phone, f_email,
                                        f_state, f_country, f_add,m_f_name, m_phone, m_email, m_state, m_country, m_add,id_child, indetail)
                                cursor.execute(insert_table, vals)      
                                mydb.commit()
                                mydb.close()
                            messagebox.showinfo("SUCCESS", "RECORD INSERTED")
                        except Exception as e:
                            messagebox.showerror("Error", e)

                    popup.mainloop()
                else:
                    from tkinter import messagebox
                    messagebox.showwarning("Alert", "Select A Row To Edit")
         

            style =ttk.Style()
            font1 = ['Times',12, 'normal']
            font2 = ['Times',10, 'normal']
            style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=font2)
            style.configure("mystyle.Treeview.Heading",font=font1)
            style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])


            btn_view = Button(frame_childbar, text='view', width=14, height=2, bg='white', command=lambda:view())
            btn_view.place(x = 800, y = 80)
            btn_view.config(font=("Bahnschrift", 11))

            btn_edit = Button(frame_childbar, text='Edit', width=14, height=2, bg='#ADD8E6', command=lambda:edit())
            btn_edit.place(x = 930, y = 80)
            btn_edit.config(font=("Bahnschrift", 11))

            btn_del = Button(frame_childbar, text='Delete', width=14, height=2, bg='red', command=lambda:delete())
            btn_del.place(x = 1060, y = 80)
            btn_del.config(font=("Bahnschrift", 11))
            

            def child_admin_query():
               
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
                    messagebox.showerror("Error","Empty Record")
                else:
                    for i in results:
                        name = (i[1]+" "+i[2])
                        table_dash.insert("",'end', values=(i[0], i[21], name, i[20], i[3], i[4]))
                mydb.commit()
                mydb.close()
                

            child_admin_query()

        ###################################################################################################
            ############################################################################################
            ###################################### ABUSE SECTION #######################################

        def abuse():
            frame_abusebar = Frame(frame_admin,width=width, height=height, bg='white')
            frame_abusebar.place(x=306, y=0)

            lbl1 = Label(frame_abusebar, text='Abuse', bg='white')
            lbl1.place(x = 23, y = 30)
            lbl1.config(font=("Bahnschrift", 20))

            lbl1 = Label(frame_abusebar, text='Records of Abuse', bg='white')
            lbl1.place(x = 105, y = 39)
            lbl1.config(font=("Bahnschrift", 13))

            btn1 = Button(frame_abusebar, text='Insert New Record', width=17, height=2, bg='#ADD8E6', command=lambda:popupmsg_abuse())
            btn1.place(x = 23, y = 80)
            btn1.config(font=("Bahnschrift", 11))

            lbl2 = Label(frame_abusebar, text='Records of Abuse', bg='#E1D9D1', width=129)
            lbl2.place(x = 23, y = 155)
            lbl2.config(font=("Bahnschrift", 12))

            game_scroll = Scrollbar(frame_abusebar,orient='vertical', width=30)
            game_scroll.place(x = (width//1.3)-16, y= 185)

            btn_view = Button(frame_abusebar, text='view', width=14, height=2, bg='white', command=lambda:view())
            btn_view.place(x = 800, y = 80)
            btn_view.config(font=("Bahnschrift", 11))

            btn_edit = Button(frame_abusebar, text='Edit', width=14, height=2, bg='#ADD8E6', command=lambda:edit())
            btn_edit.place(x = 930, y = 80)
            btn_edit.config(font=("Bahnschrift", 11))

            btn_del = Button(frame_abusebar, text='Delete', width=14, height=2, bg='red', command=lambda:delete())
            btn_del.place(x = 1060, y = 80)
            btn_del.config(font=("Bahnschrift", 11))

            global table_abuse
            table_abuse = ttk.Treeview(frame_abusebar, style="mystyle.Treeview", yscrollcommand=game_scroll.set)
            table_abuse['columns']= ("S/N", "Date", "Abuse ID", "Type Of Abuse", "Abuse Name", "Reporter", "Reported To", "Status")
            table_abuse.column("#0", width=0, stretch=NO)
            table_abuse.column("S/N", width=10, anchor = CENTER)
            table_abuse.column("Date", width=80, anchor = CENTER)
            table_abuse.column("Abuse ID", width=80, anchor = CENTER)
            table_abuse.column("Type Of Abuse", width=80, anchor = CENTER)
            table_abuse.column("Abuse Name", width=80, anchor = CENTER)
            table_abuse.column("Reporter", width=80, anchor = CENTER)
            table_abuse.column("Reported To", width=80, anchor = CENTER)
            table_abuse.column("Status", width=80, anchor = CENTER)
            table_abuse.place(x = 20, y= 185, width= (width//1.3)-40,  height = 650)
            table_abuse.heading("S/N", text = "S/N")
            table_abuse.heading("Date", text = "Date")
            table_abuse.heading("Abuse ID", text = "Abuse ID")
            table_abuse.heading("Type Of Abuse", text = "Type Of Abuse")
            table_abuse.heading("Abuse Name", text = "Abuse Name")
            table_abuse.heading("Reporter", text = "Reporter")
            table_abuse.heading("Reported To", text = "Reported To")
            table_abuse.heading("Status", text = "Status")

            style =ttk.Style()
            font1 = ['Times',12, 'normal']
            font2 = ['Times',10, 'normal']
            style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=font2)
            style.configure("mystyle.Treeview.Heading",font=font1)
            style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])

            def delete():
                if table_abuse.focus():
                    # Get selected item to Delete
                    selected_item = table_abuse.selection()[0]
                    askdel = messagebox.askyesno("Confirmation", "Do you want to Delete this Record?")
                    if askdel:
                        table_abuse.delete(selected_item)
                        messagebox.showinfo("INFO", "For Security and unbaised Purpose,\nData will only be deleted on table but preserved on database")
                    else:
                        pass
                else:
                    messagebox.showwarning("Alert", "Select A Row To Delete")
            
            def view():
                if table_abuse.focus():
                    import customtkinter as ctk
                    import mysql.connector
                    from datetime import datetime
                    from tkinter import messagebox, ttk
                    
                    from PIL import ImageTk, Image

                    
                    popup = Tk()
                    popup.wm_title("!")

                    try:
                        # windows only (remove the minimize/maximize button)
                        popup.attributes('-toolwindow', True)
                    except TclError:
                        pass

                    # frame1 = Frame(popup, width=120, height=150, bg="blue")
                    # frame1.grid(row=0, column=0)

                    frame2 = Frame(popup, width=580, height=240)
                    frame2.grid(row=0, column=0)

                    detail = []
                    # Get selected item to Edit
                    selected_item = table_abuse.focus()
                    details = table_abuse.item(selected_item)
                    detailing = details.get("values")[0]
                    
                    detail.append(detailing)     
                    print(detail)                 

                    mydb = mysql.connector.connect(
                            host = "localhost",
                            user= "root",
                            password = "",
                            port= 3306,
                            database="childdb"
                            )
                    cursor = mydb.cursor() 
                    view_rec = """ SELECT * FROM abuse_reg WHERE id = %s"""
                    
                    val2 = (detail)
                    cursor.execute(view_rec, val2)
                    results = cursor.fetchall()
                    if results == "":
                        pass
                    else:
                        for r in results:
                            names = r[3]
                            c_state = r[7]
                            c_country = r[8] 
                            ABUSE_TYPE = r[2]
                            reporter_name = r[17]
                            station_name = r[9]
                            officer = r[11]
                            status = r[24]

                        
                            
                            message = """
                    A case was reported of whose the victim name is {}
                    from {} state in {}.
                    \n
                    The victim has been subjected to {}.
                    The case which was reported by {}, has been 
                    reported to {} station in which 
                    Officer {} has been assigned to the case. 
                    The status of the case is currently {}""".format(names, c_state, c_country, ABUSE_TYPE, reporter_name, station_name, 
                                                                            officer, status)
                        
                    # imaging = Image.open(BytesIO(pic))
                    # image1= imaging.resize((120,150))
                    # img20 = ImageTk.PhotoImage(image1)

                    # lbl = Label(frame1, image = img20)
                    # lbl.place(x = 0, y = 0)
                    

                    lbl = Label(frame2, text=message)
                    lbl.place(x = 5, y = 20)
                    lbl.config(font=("Bahnschrift", 11))

                    popup.call('wm', 'attribute', '.', '-topmost', '1')
                    popup.mainloop()
                else:
                    from tkinter import messagebox
                    messagebox.showwarning("Alert", "Select A Row To View")

            def edit():
                if table_abuse.focus():
                    import customtkinter as ctk
                    import mysql.connector
                    from datetime import datetime
                    from tkinter import messagebox, ttk
    
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

                    detail = []
                    # Get selected item to Edit
                    selected_item = table_abuse.focus()
                    details = table_abuse.item(selected_item)
                    detailing = details.get("values")[0]
                    
                    detail.append(detailing)

                    mydb = mysql.connector.connect(
                            host = "localhost",
                            user= "root",
                            password = "",
                            port= 3306,
                            database="childdb"
                            )
                    cursor = mydb.cursor() 
                    view_rec = """ SELECT * FROM abuse_reg WHERE id = %s"""
                    val = (detail)
                    cursor.execute(view_rec, val)
                    results = cursor.fetchall()
                    if results == "":
                        pass
                    else:
                        for j in results:
                            abuse_id_1.insert(0, j[1])
                            type_abuse.insert(0, j[2])
                            abused_n.insert(0, j[3])
                            abused_p.insert(0, j[4])
                            abused_addr.insert(0, j[5])
                            abused_mail.insert(0, j[6])
                            a_state.insert(0, j[7])
                            a_country.insert(0, j[8])
                            station_n.insert(0, j[9])
                            station_addr.insert(0, j[10])
                            p_ic.insert(0, j[11])
                            officer_phone.insert(0, j[12])
                            Officer_email.insert(0, j[13])
                            officer_address.insert(0, j[14])
                            officer_state.insert(0, j[15])
                            officer_country.insert(0, j[16])
                            r_name.insert(0, j[17])
                            r_phone.insert(0, j[18])
                            r_email.insert(0, j[19])
                            r_addr.insert(0, j[20])
                            r_state.insert(0, j[21])
                            r_country.insert(0, j[22])
                            status_1.insert(0, j[24])
                    mydb.commit()
                    mydb.close()


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

                        try:

                            mydb = mysql.connector.connect(
                                    host = "localhost",
                                    user= "root",
                                    password = "",
                                    port= 3306,
                                    database="childdb"
                                    )
                            cursor = mydb.cursor() 
                            for indetail in detail:
                                indetail = str(indetail)
                                insert_rec =  """                     
                                                UPDATE abuse_reg
                                                SET
                                                abuse_id = %s, type_abuse = %s, abused_name = %s, abused_phone = %s, abused_address = %s, abused_email = %s, abused_state = %s, abused_country = %s,
                                                station_reported = %s, station_address = %s, person_incharge = %s, person_phone = %s, person_email = %s, person_address = %s, person_state = %s,
                                                person_country = %s, reporter_name = %s, reporter_phone = %s, reporter_email = %s, reporter_address = %s, reporter_state = %s, 
                                                reporter_country = %s, status = %s
                                                WHERE id = %s"""
                                
                                vals = (abuse_id, type, cname, cphone, caddr, cemail, cstate, ccountry,station, saddr, pname, 
                                        pphone, pemail, paddr, pstate, pcountry, rname, rphone, remail, raddr, rstate, rcountry, status, indetail)
                                cursor.execute(insert_rec, vals)            
                                mydb.commit()
                                mydb.close()
                            messagebox.showinfo("SUCCESS", "RECORD INSERTED")
                        except Exception as e:
                            messagebox.showerror("Error", e)

                        popup.mainloop()
                else:
                    from tkinter import messagebox
                    messagebox.showwarning("Alert", "Select A Row To Edit")

            def abuse_admin_query():
                mydb = mysql.connector.connect(
                        host = "localhost",
                        user= "root",
                        password = "",
                        port= 3306,
                        database="childdb"
                        )
                cursor = mydb.cursor() 
                view_rec = """ SELECT * FROM abuse_reg WHERE status = 'PENDING' """
                cursor.execute(view_rec)
                results = cursor.fetchall()
                if results == "":
                    pass
                else:
                    for i in results:
                        table_abuse.insert("",'end', values=(i[0], i[23], i[1], i[2], i[3], i[17], i[9], i[24]))
                mydb.commit()
                mydb.close()


            abuse_admin_query()

        def report():
            frame_report = Frame(frame_admin,width=width, height=height, bg='white')
            frame_report.place(x=306, y=0)

            lbl1 = Label(frame_report, text='Case Reports', bg='white')
            lbl1.place(x = 23, y = 30)
            lbl1.config(font=("Bahnschrift", 18))

            lbl1 = Label(frame_report, text='Lists of Case Report', bg='white')
            lbl1.place(x = 175, y = 38)
            lbl1.config(font=("Bahnschrift", 12))

            lbl2 = Label(frame_report, text='Lists of Reports', bg='#E1D9D1', width=129)
            lbl2.place(x = 23, y = 80)
            lbl2.config(font=("Bahnschrift", 12))


            game_scroll = Scrollbar(frame_report,orient='vertical', width=30)
            game_scroll.place(x = (width//1.3)-16, y= 110)

            global table_report
            table_report = ttk.Treeview(frame_report, style="mystyle.Treeview", yscrollcommand=game_scroll.set)
            table_report['columns']= ("S/N", "Date", "Abuse ID", "Type Of Abuse", "Abuse Name", "Reporter", "Reported To", "Status")
            table_report.column("#0", width=0, stretch=NO)
            table_report.column("S/N", width=10, anchor = CENTER)
            table_report.column("Date", width=80, anchor = CENTER)
            table_report.column("Abuse ID", width=80, anchor = CENTER)
            table_report.column("Type Of Abuse", width=80, anchor = CENTER)
            table_report.column("Abuse Name", width=80, anchor = CENTER)
            table_report.column("Reporter", width=80, anchor = CENTER)
            table_report.column("Reported To", width=80, anchor = CENTER)
            table_report.column("Status", width=80, anchor = CENTER)
            table_report.place(x = 20, y= 110, width= (width//1.3)-40,  height = 650)
            table_report.heading("S/N", text = "S/N")
            table_report.heading("Date", text = "Date")
            table_report.heading("Abuse ID", text = "Abuse ID")
            table_report.heading("Type Of Abuse", text = "Type Of Abuse")
            table_report.heading("Abuse Name", text = "Abuse Name")
            table_report.heading("Reporter", text = "Reporter")
            table_report.heading("Reported To", text = "Reported To")
            table_report.heading("Status", text = "Status")

            style =ttk.Style()
            font1 = ['Times',12, 'normal']
            font2 = ['Times',10, 'normal']
            style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=font2)
            style.configure("mystyle.Treeview.Heading",font=font1)
            style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])

            
            def edit():
                if table_abuse.focus():
                    import customtkinter as ctk
                    import mysql.connector
                    from datetime import datetime
                    from tkinter import messagebox, ttk
    
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

                    detail = []
                    # Get selected item to Edit
                    selected_item = table_report.focus()
                    details = table_report.item(selected_item)
                    detailing = details.get("values")[0]
                    
                    detail.append(detailing)

                    mydb = mysql.connector.connect(
                            host = "localhost",
                            user= "root",
                            password = "",
                            port= 3306,
                            database="childdb"
                            )
                    cursor = mydb.cursor() 
                    view_rec = """ SELECT * FROM abuse_reg WHERE id = %s"""
                    val = (detail)
                    cursor.execute(view_rec, val)
                    results = cursor.fetchall()
                    if results == "":
                        pass
                    else:
                        for j in results:
                            abuse_id_1.insert(0, j[1])
                            type_abuse.insert(0, j[2])
                            abused_n.insert(0, j[3])
                            abused_p.insert(0, j[4])
                            abused_addr.insert(0, j[5])
                            abused_mail.insert(0, j[6])
                            a_state.insert(0, j[7])
                            a_country.insert(0, j[8])
                            station_n.insert(0, j[9])
                            station_addr.insert(0, j[10])
                            p_ic.insert(0, j[11])
                            officer_phone.insert(0, j[12])
                            Officer_email.insert(0, j[13])
                            officer_address.insert(0, j[14])
                            officer_state.insert(0, j[15])
                            officer_country.insert(0, j[16])
                            r_name.insert(0, j[17])
                            r_phone.insert(0, j[18])
                            r_email.insert(0, j[19])
                            r_addr.insert(0, j[20])
                            r_state.insert(0, j[21])
                            r_country.insert(0, j[22])
                            status_1.insert(0, j[24])
                    mydb.commit()
                    mydb.close()


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

                        try:

                            mydb = mysql.connector.connect(
                                    host = "localhost",
                                    user= "root",
                                    password = "",
                                    port= 3306,
                                    database="childdb"
                                    )
                            cursor = mydb.cursor() 
                            for indetail in detail:
                                indetail = str(indetail)
                                insert_rec =  """                     
                                                UPDATE abuse_reg
                                                SET
                                                abuse_id = %s, type_abuse = %s, abused_name = %s, abused_phone = %s, abused_address = %s, abused_email = %s, abused_state = %s, abused_country = %s,
                                                station_reported = %s, station_address = %s, person_incharge = %s, person_phone = %s, person_email = %s, person_address = %s, person_state = %s,
                                                person_country = %s, reporter_name = %s, reporter_phone = %s, reporter_email = %s, reporter_address = %s, reporter_state = %s, 
                                                reporter_country = %s, status = %s
                                                WHERE id = %s"""
                                
                                vals = (abuse_id, type, cname, cphone, caddr, cemail, cstate, ccountry,station, saddr, pname, 
                                        pphone, pemail, paddr, pstate, pcountry, rname, rphone, remail, raddr, rstate, rcountry, status, indetail)
                                cursor.execute(insert_rec, vals)            
                                mydb.commit()
                                mydb.close()
                            messagebox.showinfo("SUCCESS", "RECORD INSERTED")
                        except Exception as e:
                            messagebox.showerror("Error", e)

                        popup.mainloop()
                else:
                    from tkinter import messagebox
                    messagebox.showwarning("Alert", "Select A Row To Edit")

            btn_del = Button(frame_report, text='Edit', width=14, height=2, bg='blue', command=lambda:edit())
            btn_del.place(x = 1060, y = 20)
            btn_del.config(font=("Bahnschrift", 11))

            def report_admin_query():
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
                    for i in results:
                        table_report.insert("",'end', values=(i[0], i[23], i[1], i[2], i[3], i[17], i[9], i[24]))
                mydb.commit()
                mydb.close()


            report_admin_query()

            


         

        main()
    front_page()
    
      









topbar()


root.mainloop()
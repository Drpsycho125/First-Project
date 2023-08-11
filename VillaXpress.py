from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import sqlite3
import random
import string
import datetime

system = CTk()
system.title("Parcel Tracking System")
system.geometry('990x670')
system.resizable(False, False)
system.iconbitmap('3041529.ico')

#Background Image
original = Image.open('newBackground.jpg')
resize = original.resize((990, 600), Image.LANCZOS)
background = ImageTk.PhotoImage(resize)

#Logo Image
logo_original = Image.open('new_logo.png')
resized = logo_original.resize((160, 60), Image.LANCZOS)
logo = ImageTk.PhotoImage(resized)

#Register Image
r_image = Image.open('login_background.jpg')
r_image = r_image.resize((990, 600), Image.LANCZOS)
r_image = ImageTk.PhotoImage(r_image)

#Search Image
s_image = Image.open('searching_logo.png')

s_image = CTkImage(s_image, size = (50, 50))

#About Image
a_image = Image.open('about_background.png')
a_image = a_image.resize((990, 600), Image.LANCZOS)
a_image = ImageTk.PhotoImage(a_image)

#Address Image
ad_image = Image.open('address_logo.png')
ad_image = ad_image.resize((120, 120), Image.LANCZOS)
ad_image = ImageTk.PhotoImage(ad_image)

#Contact Image
con_image = Image.open('phone_logo.png')
con_image = con_image.resize((120, 120), Image.LANCZOS)
con_image = ImageTk.PhotoImage(con_image)

#Email Image
em_image = Image.open('email_logo.png')
em_image = em_image.resize((120, 120), Image.LANCZOS)
em_image = ImageTk.PhotoImage(em_image)

#Kim Harry Oclarit Image
ko_image = Image.open('KimH.jpg')
ko_image = ko_image.resize((80, 80), Image.LANCZOS)
ko_image = ImageTk.PhotoImage(ko_image)

#Joseph Cosmiano Image
jc_image = Image.open('Jos.jpg')
jc_image = jc_image.resize((80, 80), Image.LANCZOS)
jc_image = ImageTk.PhotoImage(jc_image)

#Leonardo Sajulga Image
ls_image = Image.open('Leo.jpg')
ls_image = ls_image.resize((80, 80), Image.LANCZOS)
ls_image = ImageTk.PhotoImage(ls_image)

#Shainie Derita Image
sd_image = Image.open('Shai.jpg')
sd_image = sd_image.resize((80, 80), Image.LANCZOS)
sd_image = ImageTk.PhotoImage(sd_image)

#Princess Junta Tanqui-on Image
pt_image = Image.open('Prin.jpg')
pt_image = pt_image.resize((80, 80), Image.LANCZOS)
pt_image = ImageTk.PhotoImage(pt_image)

#Kimjie Anoc Image
ka_image = Image.open('KimJ.jpg')
ka_image = ka_image.resize((80, 80), Image.LANCZOS)
ka_image = ImageTk.PhotoImage(ka_image)

conn = sqlite3.connect('newdata.db')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS parcel
                  (tracking_id TEXT PRIMARY KEY,
                  name TEXT,
                  contact TEXT,
                  product_name TEXT,
                  price INTEGER,
                  quantity INTEGER,
                  weight INTEGER,
                  delivery_date TEXT,
                  transaction_type TEXT,
                  delivery_address TEXT,
                  seller TEXT, 
                  seller_add TEXT, 
                  seller_con TEXT, 
                  status TEXT DEFAULT 'In Transit')''')
conn.commit()


def home():
    home_b.configure(fg = "white")
    register_b.configure(fg = "black")
    search_b.configure(fg = "black")
    about_b.configure(fg = "black")
    #Button Animations
    #Mouse In
    def Hover11(event):
        contact_b.configure(width = 10, height = 2, font = ("Arial Black", 12, 'bold'))
        contact_b.place(x = 96, y = 516)
    def Hover21(event):
        disco_b.configure(width = 13, height = 2, font = ("Arial Black", 12, 'bold'))
        disco_b.place(x = 246, y = 516)

    #Mouse Out
    def Hover12(event):
        contact_b.configure(width = 10, height = 2, font = ("Arial", 12, 'bold'))
        contact_b.place(x = 100, y = 520)
    def Hover22(event):
        disco_b.configure(width = 13, height = 2, font = ("Arial", 12, 'bold'))
        disco_b.place(x = 250, y = 520)
    canvas1 = CTkCanvas(system, width = 990, height = 600)
    canvas1.place(x = 0, y = 68)
    image_item = canvas1.create_image(0, 0, anchor = NW, image=background)
    canvas1.move(image_item, -4, 0)

    #Home page Text Animation
    def float_in1(canvas, text_id, text, x, y, speed):
        y -= speed
        if y > 150:
            canvas1.coords(text_id, x, y)
            canvas1.after(10, float_in1, canvas, text_id, text, x, y, speed)
    def float_in2(canvas, text_id, text, x, y, speed):
        y -= speed
        if y > 300:
            canvas1.coords(text_id, x, y)
            canvas1.after(10, float_in2, canvas, text_id, text, x, y, speed)

    greeting = "Welcome to our \nParcel Tracking System!"
    paragraph = "Our user-friendly platform provides a hassle-free way to\ntrack your parcels from the comfort of your home.\nStay updated on the whereabouts of your packages\nwith real-time tracking information and receive instant\nnotifications for any status change.\n\nExperience the convince of our Parcel Tracking System\nand take control of your deliveries today!"

    x = 290
    y = 200
    speed = 1
    
    title = canvas1.create_text(x, y, text = greeting, font = ("Arial Black", 25, 'bold'), fill ="white", justify = LEFT)
    float_in1(canvas1, title, greeting, x, y, speed)

    x = 325
    y = 350
    speed = 1
    sentence = canvas1.create_text(x, y, text = paragraph, font = ("Arial", 14, 'bold'), fill ="white")
    float_in2(canvas1, sentence, paragraph, x, y, speed)

    def contact_invoke(event):
        home_b.configure(fg = "black")
        register_b.configure(fg = "black")
        search_b.configure(fg = "black")
        about_b.configure(fg = "black")
    def discover_invoke(event):
        home_b.configure(fg = "black")
        register_b.configure(fg = "black")
        search_b.configure(fg = "black")
        about_b.configure(fg = "black")
    contact_b = Button(system, text = "Contact Us", height = 2, width = 10, bg = "#FD7014", fg = "white", font = ("Arial", 12, 'bold'), activebackground = "#FD7014", activeforeground="white", bd = 1, highlightthickness = 0, relief = FLAT, command = contact)
    contact_b.place(x = 100, y = 520)
    contact_b.bind("<Enter>", Hover11)
    contact_b.bind("<Leave>", Hover12)
    contact_b.bind("<Button-1>", contact_invoke)

    disco_b = Button(system, text = "Discover More", height = 2, width = 13 , bg = "white", fg = "#FD7014", font = ("Arial", 12, 'bold'), activebackground = "white", activeforeground="#FD7014", bd = 1, highlightthickness = 0, relief = FLAT, command = discover)
    disco_b.place(x = 250, y = 520)
    disco_b.bind("<Enter>", Hover21)
    disco_b.bind("<Leave>", Hover22)
    disco_b.bind("<Button-1>", discover_invoke)

    system.mainloop()

#Pages
def register():
    def add_parcel():
    
        name = name_entry.get()
        contact = contact_entry.get()
        product_name = product_name_entry.get()
        price = price_entry.get()
        quantity = quantity_entry.get()
        weight = weight_entry.get()
        delivery_date = delivery_date_entry.get()
        transaction_type = current_var.get()
        delivery_address = delivery_address_entry.get()
        seller = seller_name.get()
        seller_add = seller_address.get()
        seller_con = seller_contact.get()

        letters_and_digits = string.ascii_uppercase + string.digits
        tracking_id = ''.join(random.choice(letters_and_digits) for _ in range(8))

        cursor.execute("INSERT INTO parcel (tracking_id, name, contact, product_name, price, quantity, weight, delivery_date, transaction_type, delivery_address, seller, seller_add, seller_con) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (tracking_id , name, contact, product_name, price, quantity, weight, delivery_date, transaction_type, delivery_address, seller, seller_add, seller_con))
        conn.commit()

        message = CTkToplevel(system)
        message.geometry('300x200')
        message.title('Registered')
        message.configure(fg_color = "#FD7014")

        def close():
            message.destroy()
    
        CTkLabel(message, text = "Successfully Registered!", font = ("Arial", 15, 'bold'), fg_color = "#FD7014", text_color = "white").place(x = 57, y = 50)
        CTkLabel(message, text = "Tracking ID:", font = ("Arial", 15, 'bold'), fg_color = "#FD7014", text_color = "white").place(x = 58, y = 90)
        message_entry = Entry(message, width = 15, font = ("Arial", 12, 'bold'), highlightthickness=0, bd= 4, relief = FLAT, fg = "green")
        message_entry.insert(0, tracking_id)
        message_entry.configure(state = 'readonly', readonlybackground='#FD7014')
        message_entry.place(x = 148, y = 90)

        CTkButton(message, text = "OK", height=40, width=80, text_color="#FD7014", fg_color= "white", font = ("Arial", 15, 'bold'), command = close).place(x = 110, y = 135)

        name_entry.delete(0, END)
        contact_entry.delete(0, END)
        product_name_entry.delete(0, END)
        price_entry.delete(0, END)
        quantity_entry.delete(0, END)
        weight_entry.delete(0, END)
        delivery_date_entry.delete(0, END)
        delivery_address_entry.delete(0, END)
        seller_name.delete(0, END)
        seller_address.delete(0, END)
        seller_contact.delete(0, END)

    register = Frame(system, width = 990, height = 600, bg = 'gray')
    register.place(x = 0, y = 68)
    canvas2 = CTkCanvas(register, width = 990, height = 600)
    canvas2.place(x = 0, y = 0)
    image_item1 = canvas2.create_image(0, 0, anchor = NW, image=r_image)
    canvas2.move(image_item1, -4, 0)

    #Add Button Animation
    def button_hover1(event):
        add_button.configure(fg_color = "white", text_color = "#FD7014", width = 165, height = 80, font = ("Arial Black", 35, 'bold'))
        add_button.place(x = 750, y = 470) 
    def button_hover2(event):
        add_button.configure(fg_color = "#FD7014", text_color = "white", width = 150, height = 65, font = ("Arial", 30, 'bold'))
        add_button.place(x = 760, y = 480)

    home_b.configure(fg = "black")
    register_b.configure(fg = "#FD7014")
    search_b.configure(fg = "black")
    about_b.configure(fg = "black")

    #Register Widgets
    buyer = CTkFrame(register, width = 400, height = 220, fg_color = "#FD7014", bg_color = "transparent", corner_radius = 15).place(x = 70, y = 50)
    CTkLabel(buyer, text = "Buyer Information", text_color = "white", font = ("Times", 25, "bold", "underline"), bg_color = "#FD7014").place(x = 170, y = 130)
    name_entry = CTkEntry(buyer, placeholder_text = "Name", placeholder_text_color = "#FD7014", border_color = "#FD7014", fg_color= "white", text_color = "#FD7014", height= 40, width = 350, font = ("Arial", 15, "bold"), bg_color = "#FD7014")
    name_entry.place(x = 100, y = 190)
    contact_entry = CTkEntry(buyer, placeholder_text = "Contact", placeholder_text_color = "#FD7014", border_color = "#FD7014", fg_color= "white", text_color = "#FD7014", height= 40, width = 350, font = ("Arial", 15, "bold"), bg_color = "#FD7014")
    contact_entry.place(x = 100, y = 260)
    seller = CTkFrame(register, width = 400, height = 250, fg_color = "#FD7014", bg_color = "transparent", corner_radius = 15)
    seller.place(x = 70, y = 300)
    CTkLabel(buyer, text = "Seller Information", text_color = "white", font = ("Times", 25, "bold", "underline"), bg_color = "#FD7014").place(x = 170, y = 390)
    seller_name = CTkEntry(buyer, placeholder_text = "Name", placeholder_text_color = "#FD7014", border_color = "#FD7014", fg_color= "white", text_color = "#FD7014", height= 40, width = 350, font = ("Arial", 15, "bold"), bg_color = "#FD7014")
    seller_name.place(x = 100, y = 450)
    seller_address = CTkEntry(buyer, placeholder_text = "Contact", placeholder_text_color = "#FD7014", border_color = "#FD7014", fg_color= "white", text_color = "#FD7014", height= 40, width = 350, font = ("Arial", 15, "bold"), bg_color = "#FD7014")
    seller_address.place(x = 100, y = 500)
    seller_contact = CTkEntry(buyer, placeholder_text = "Address", placeholder_text_color = "#FD7014", border_color = "#FD7014", fg_color= "white", text_color = "#FD7014", height= 40, width = 350, font = ("Arial", 15, "bold"), bg_color = "#FD7014")
    seller_contact.place(x = 100, y = 550)
    parcel = CTkFrame(register, width = 400, height = 400, fg_color = "#FD7014", bg_color = "transparent", corner_radius = 15).place(x = 510, y = 50)
    CTkLabel(buyer, text = "Parcel Information", text_color = "white", font = ("Times", 25, "bold", "underline"), bg_color = "#FD7014").place(x = 620, y = 130)
    product_name_entry = CTkEntry(buyer, placeholder_text = "Product Name", placeholder_text_color = "#FD7014", border_color = "#FD7014", fg_color= "white", text_color = "#FD7014", height= 40, width = 350, font = ("Arial", 15, "bold"), bg_color = "#FD7014")
    product_name_entry.place(x = 540, y = 190)
    price_entry = CTkEntry(buyer, placeholder_text = "Price", placeholder_text_color = "#FD7014", border_color = "#FD7014", fg_color= "white", text_color = "#FD7014", height= 40, width = 200, font = ("Arial", 15, "bold"), bg_color = "#FD7014")
    price_entry.place(x = 540, y = 235)
    quantity_entry = CTkEntry(buyer, placeholder_text = "Quantity", placeholder_text_color = "#FD7014", border_color = "#FD7014", fg_color= "white", text_color = "#FD7014", height= 40, width = 200, font = ("Arial", 15, "bold"), bg_color = "#FD7014")
    quantity_entry.place(x = 540, y = 280)
    weight_entry = CTkEntry(buyer, placeholder_text = "Weight", placeholder_text_color = "#FD7014", border_color = "#FD7014", fg_color= "white", text_color = "#FD7014", height= 40, width = 200, font = ("Arial", 15, "bold"), bg_color = "#FD7014")
    weight_entry.place(x = 540, y = 325)
    CTkLabel(buyer, text = "kg", font = ("Arial", 15, "bold"), bg_color = "#FD7014").place(x = 760, y = 330)
    delivery_date_entry = CTkEntry(buyer, placeholder_text = "Delivery Date", placeholder_text_color = "#FD7014", border_color = "#FD7014", fg_color= "white", text_color = "#FD7014", height= 40, width = 200, font = ("Arial", 15, "bold"), bg_color = "#FD7014")
    delivery_date_entry.place(x = 540, y = 370)
    CTkLabel(buyer, text = "mm/dd/yyyy", font = ("Arial", 15, "bold"), bg_color = "#FD7014").place(x = 760, y = 375)
    CTkLabel(buyer, text = "Transaction Type", font = ("Arial", 15, "bold"), bg_color = "#FD7014").place(x = 550, y = 420)
    current_var = StringVar()
    combobox = CTkComboBox(buyer, variable = current_var, height= 40, border_color = "#FD7014", fg_color= "white", width = 200, font = ("Arial", 15, "bold"), text_color = "#FD7014",  bg_color = "#FD7014", state = "readonly", values = ["COD", "E-Wallet"])
    combobox.place(x = 690, y = 415)
    combobox.set("COD")
    delivery_address_entry = CTkEntry(buyer, placeholder_text = "Delivery Address", placeholder_text_color = "#FD7014", text_color = "#FD7014", border_color = "#FD7014", fg_color= "white", height= 40, width = 350, font = ("Arial", 15, "bold"), bg_color = "#FD7014")
    delivery_address_entry.place(x = 540, y = 460)
    add_button = CTkButton(register, command = add_parcel,text = 'Add', width = 150, height = 65, font = ("Arial", 30, 'bold'), bg_color = "transparent", border_width = 3, border_color = "#FD7014", hover_color = "#FD7014", corner_radius = 15, fg_color = "#FD7014", text_color = "white")
    add_button.place(x = 760, y = 480)
    add_button.bind('<Enter>', button_hover1)
    add_button.bind('<Leave>', button_hover2)

def search():
    
    def search_parcel():
            tracking_id = search_entry.get()

            cursor.execute("SELECT * FROM parcel WHERE tracking_id=?", (tracking_id,))
            parcel = cursor.fetchone()

            if parcel:
                all_items = table1.get_children()
                for item in all_items:
                    table1.delete(item)

                all_items = table2.get_children()
                for item in all_items:
                    table2.delete(item)

                tracking_id_label.configure(text = str(parcel[0]))
                status_label.configure(text = parcel[13])
                delivered_button.configure(state = NORMAL)
                return_to_sender_button.configure(state = NORMAL)
                reset_date_button.configure(state = NORMAL)


                stored_name = parcel[1]
                stored_contact = parcel[2]
                stored_product_name = parcel[3]
                stored_price = parcel[4]
                stored_quantity = parcel[5]
                stored_weight = parcel[6]
                stored_delivery_date = parcel[7]
                stored_transaction_type = parcel[8]
                stored_delivery_address = parcel[9]
                stored_seller = parcel[10]
                stored_seller_add = parcel[11]
                stored_seller_con = parcel[12]
                stored_status = parcel[13] 

                if parcel[13] == 'Return to \nSender':
                    delivered_button.configure(state = 'disabled')
                    return_to_sender_button.configure(state = 'normal')
                    reset_date_button.configure(state='disabled')  
                elif parcel[13] == 'Delivered':
                    delivered_button.configure(state = 'normal')
                    return_to_sender_button.configure(state = 'disabled')
                    reset_date_button.configure(state='disabled')   
                

                table1.insert('', 'end', values = (tracking_id, stored_name, stored_contact, stored_seller, stored_product_name, stored_quantity, stored_price))
                table2.insert('', 'end', values = (stored_seller_con, stored_seller_add, stored_weight, stored_transaction_type, stored_delivery_date, stored_delivery_address, stored_status))

            else:
                tracking_id_label.configure(text = "Not Found")
                status_label.configure(text = "Not Found")
                delivered_button.configure(state = DISABLED)
                return_to_sender_button.configure(state = DISABLED)
                reset_date_button.configure(state = DISABLED)

    def mark_delivered():
            tracking_id = search_entry.get()

            cursor.execute("UPDATE parcel SET status='Delivered' WHERE tracking_id=?", (tracking_id,))
            conn.commit()

            cursor.execute("SELECT * FROM parcel WHERE tracking_id=?", (tracking_id,))
            parcel = cursor.fetchone()

            if parcel:
                all_items = table1.get_children()
                for item in all_items:
                    table1.delete(item)

                all_items = table2.get_children()
                for item in all_items:
                    table2.delete(item)

                stored_name = parcel[1]
                stored_contact = parcel[2]
                stored_product_name = parcel[3]
                stored_price = parcel[4]
                stored_quantity = parcel[5]
                stored_weight = parcel[6]
                stored_delivery_date = parcel[7]
                stored_transaction_type = parcel[8]
                stored_delivery_address = parcel[9]
                stored_seller = parcel[10]
                stored_seller_add = parcel[11]
                stored_seller_con = parcel[12]
                stored_status = parcel[13] 

                table1.insert('', 'end', values = (tracking_id, stored_name, stored_contact, stored_seller, stored_product_name, stored_quantity, stored_price))
                table2.insert('', 'end', values = (stored_seller_con, stored_seller_add, stored_weight, stored_transaction_type, stored_delivery_date, stored_delivery_address, stored_status))

                status_label.configure(text = "Delivered")
                return_to_sender_button.configure(state='disabled')
                reset_date_button.configure(state='disabled')

    def reset_date():
            tracking_id = search_entry.get()

            cursor.execute("SELECT delivery_date FROM parcel WHERE tracking_id=?", (tracking_id,))
            current_date = cursor.fetchone()[0]

            if current_date:
                current_date = datetime.datetime.strptime(current_date, "%m/%d/%Y").date()
  
                estimated_days = 7 
                new_date = current_date + datetime.timedelta(days=estimated_days)

                while new_date.month != current_date.month:

                    exceeding_days = (new_date - current_date).days - (new_date.day - 1)
                    new_date -= datetime.timedelta(days=exceeding_days)
                    new_date = new_date.replace(day=1)
                    new_date += datetime.timedelta(days=1)

                new_date_str = new_date.strftime("%m/%d/%Y")

                cursor.execute("UPDATE parcel SET delivery_date=? WHERE tracking_id=?", (new_date_str, tracking_id))
                conn.commit()

                cursor.execute("SELECT * FROM parcel WHERE tracking_id=?", (tracking_id,))
                parcel = cursor.fetchone()

                if parcel:
                    all_items = table1.get_children()
                    for item in all_items:
                        table1.delete(item)

                    all_items = table2.get_children()
                    for item in all_items:
                        table2.delete(item)

                    stored_name = parcel[1]
                    stored_contact = parcel[2]
                    stored_product_name = parcel[3]
                    stored_price = parcel[4]
                    stored_quantity = parcel[5]
                    stored_weight = parcel[6]
                    stored_delivery_date = parcel[7]
                    stored_transaction_type = parcel[8]
                    stored_delivery_address = parcel[9]
                    stored_seller = parcel[10]
                    stored_seller_add = parcel[11]
                    stored_seller_con = parcel[12]
                    stored_status = parcel[13] 

                    table1.insert('', 'end', values = (tracking_id, stored_name, stored_contact, stored_seller, stored_product_name, stored_quantity, stored_price))
                    table2.insert('', 'end', values = (stored_seller_con, stored_seller_add, stored_weight, stored_transaction_type, stored_delivery_date, stored_delivery_address, stored_status))

                    status_label.configure(text = stored_status)
                    reset_date_button.configure(state='disabled')

    def return_to_sender():
            tracking_id = search_entry.get()

            cursor.execute("UPDATE parcel SET status='Return to \nSender' WHERE tracking_id=?", (tracking_id,))
            conn.commit()

            cursor.execute("SELECT * FROM parcel WHERE tracking_id=?", (tracking_id,))
            parcel = cursor.fetchone()

            if parcel:
                all_items = table1.get_children()
                for item in all_items:
                    table1.delete(item)

                all_items = table2.get_children()
                for item in all_items:
                    table2.delete(item)

            stored_name = parcel[1]
            stored_contact = parcel[2]
            stored_product_name = parcel[3]
            stored_price = parcel[4]
            stored_quantity = parcel[5]
            stored_weight = parcel[6]
            stored_delivery_date = parcel[7]
            stored_transaction_type = parcel[8]
            stored_delivery_address = parcel[9]
            stored_seller = parcel[10]
            stored_seller_add = parcel[11]
            stored_seller_con = parcel[12]
            stored_status = parcel[13]

            table1.insert('', 'end', values = (tracking_id, stored_name, stored_contact, stored_seller, stored_product_name, stored_quantity, stored_price))
            table2.insert('', 'end', values = (stored_seller_con, stored_seller_add, stored_weight, stored_transaction_type, stored_delivery_date, stored_delivery_address, stored_status))
            
            status_label.configure(text = "Return to Sender")
            delivered_button.configure(state='disabled')
            reset_date_button.configure(state='disabled')

    home_b.configure(fg = "black")
    register_b.configure(fg = "black")
    search_b.configure(fg = "#FD7014")
    about_b.configure(fg = "black")
    search = Frame(system, width = 990, height = 600, bg = '#FD7014')
    search.place(x = 0, y = 68)
    search_entry = CTkEntry(search, placeholder_text = "Tracking  ID", placeholder_text_color = "#FD7014", border_color = "#FD7014", fg_color= "white", text_color = "#FD7014", height= 50, width = 200, font = ("Arial", 15, "bold"), bg_color = "#FD7014")
    search_entry.place(x = 30, y = 35)
    CTkButton(search, command = search_parcel, image = s_image, hover_color="white", bg_color= "#FD7014", fg_color="white", text = '', width = 20, height = 40).place(x = 250, y = 30)
    CTkLabel(search, text = "Tracking ID:", font = ("Arial", 20, "bold"), bg_color = "#FD7014").place(x = 550, y = 30)
    tracking_id_label = CTkLabel(search, text = "", font = ("Arial", 20, "bold"), bg_color = "#FD7014")
    tracking_id_label.place(x = 700, y = 30)
    CTkLabel(search, text = "Status:", font = ("Arial", 20, "bold"), bg_color = "#FD7014").place(x = 550, y = 80)
    status_label = CTkLabel(search, text = "", font = ("Arial", 20, "bold"), bg_color = "#FD7014")
    status_label.place(x = 700, y = 80)
    delivered_button = CTkButton(search, text = 'Delivered', state = DISABLED, command = mark_delivered, hover_color="white", bg_color= "#FD7014", font = ("Arial", 20, "bold"), text_color='#FD7014', fg_color="white", width = 20, height = 40)
    delivered_button.place(x = 30, y = 150)
    return_to_sender_button = CTkButton(search, text = 'Return to Sender', state = DISABLED, command = return_to_sender, hover_color="white", bg_color= "#FD7014", font = ("Arial", 20, "bold"), text_color='#FD7014', fg_color="white", width = 20, height = 40)
    return_to_sender_button.place(x = 150, y = 150)
    reset_date_button = CTkButton(search, text = 'Reset Date',state = DISABLED, command = reset_date, hover_color="white", bg_color= "#FD7014", font = ("Arial", 20, "bold"), text_color='#FD7014', fg_color="white", width = 20, height = 40)
    reset_date_button.place(x = 350, y = 150)

    style = ttk.Style()
    style.theme_use('default')
    style.configure('Treeview', foreground = "#FD7014", font = ("Arial", 10, "bold"), height = 10)
    style.configure('TreeviewHeading', background = "#FD7014", font = ("Arial", 20, "bold"))

    columns1 = ('tracking_id', 'buyer_name', 'buyer_contact', 'seller_name', 'product_name', 'quantity', 'price')
    table1 = ttk.Treeview(search, columns=columns1, show='headings', height = 15)
    table1.heading('tracking_id', text='Tracking ID')
    table1.column('tracking_id', width = 141, stretch=NO)
    table1.heading('buyer_name', text='Buyer Name')
    table1.column('buyer_name', width = 141, stretch=NO)
    table1.heading('buyer_contact', text='Buyer Contact')
    table1.column('buyer_contact', width = 141, stretch=NO)
    table1.heading('seller_name', text='Seller Name')
    table1.column('seller_name', width = 141, stretch=NO)
    table1.heading('product_name', text='Product Name')
    table1.column('product_name', width = 141, stretch=NO)
    table1.heading('quantity', text='Quantity')
    table1.column('quantity', width = 141, stretch=NO)
    table1.heading('price', text='Price')
    table1.column('price', width = 141, stretch=NO)
    table1.place(x = 0, y = 250)

    columns2 = ('seller_con', 'seller_add', 'weight', 'type', 'delivery_date', 'delivery_address', 'status')
    table2 = ttk.Treeview(search, columns=columns2, show='headings', height = 15)
    table2.heading('seller_con', text='Seller Contact')
    table2.column('seller_con', width = 141, stretch=NO)
    table2.heading('seller_add', text='Seller Address')
    table2.column('seller_add', width = 141, stretch=NO)
    table2.heading('weight', text='Weight')
    table2.column('weight', width = 141, stretch=NO)
    table2.heading('type', text='Type')
    table2.column('type', width = 141, stretch=NO)
    table2.heading('delivery_date', text='Delivery Date')
    table2.column('delivery_date', width = 141, stretch=NO)
    table2.heading('delivery_address', text='Delivery Address')
    table2.column('delivery_address', width = 141, stretch=NO)
    table2.heading('status', text='Status')
    table2.column('status', width = 141, stretch=NO)
    table2.place(x = 0, y = 400)

def about():
    home_b.configure(fg = "black")
    register_b.configure(fg = "black")
    search_b.configure(fg = "black")
    about_b.configure(fg = "#FD7014")
    about = Frame(system, width = 990, height = 600, bg = 'white')
    about.place(x = 0, y = 68)
    Label(about, text = "Get To Know Our Team", bg = 'white', fg = 'black', font = ("Times", 25, "bold")).place(x = 320, y = 10)
    canvas3 = CTkCanvas(system, width = 990, height = 600)
    canvas3.place(x = 0, y = 68)
    image_item1 = canvas3.create_image(0, 0, anchor = NW, image=a_image)
    canvas3.move(image_item1, -1, 0)
    canvas3.create_text(510, 40, text = "Get To Know Our Team", fill='black', font = ("Times", 30, "bold"))
    frame = CTkFrame(canvas3, bg_color="transparent", fg_color = "white", border_width = 4, width = 700, height = 100, border_color= "black").place(x = 150, y = 470)
    frame1 = CTkFrame(canvas3, bg_color="transparent", fg_color = "black", width = 80, height = 80).place(x = 460, y = 100)
    Label(frame1, image = ko_image).place(x = 460, y = 165)
    frame2 = CTkFrame(canvas3, bg_color="transparent", fg_color = "black", width = 80, height = 80).place(x = 320, y = 220)
    Label(frame2, image = jc_image).place(x = 320, y = 285)
    frame3 = CTkFrame(canvas3, bg_color="transparent", fg_color = "black", width = 80, height = 80).place(x = 595, y = 220)
    Label(frame3, image = ls_image).place(x = 595, y = 285)
    frame4 = CTkFrame(canvas3, bg_color="transparent", fg_color = "black", width = 80, height = 80).place(x = 180, y = 340)
    Label(frame4, image = sd_image).place(x = 180, y = 405)
    frame5 = CTkFrame(canvas3, bg_color="transparent", fg_color = "black", width = 80, height = 80).place(x = 460, y = 340)
    Label(frame5, image = pt_image).place(x = 460, y = 405)
    frame6 = CTkFrame(canvas3, bg_color="transparent", fg_color = "black", width = 80, height = 80).place(x = 730, y = 340)
    Label(frame6, image = ka_image).place(x = 730, y = 405)
    canvas3.create_text(500, 90, text = "Founder", fill='#FD7014', font = ("Calibri", 12, "bold"))
    canvas3.create_text(500, 190, text = "Kim Harry Oclarit", fill='black', font = ("Times", 10, "bold"))
    canvas3.create_text(360, 210, text = "Developer", fill='#FD7014', font = ("Calibri", 12, "bold"))
    canvas3.create_text(360, 310, text = "Joseph Cosmiano", fill='black', font = ("Times", 10, "bold"))
    canvas3.create_text(635, 210, text = "Researcher", fill='#FD7014', font = ("Calibri", 12, "bold"))
    canvas3.create_text(635, 310, text = "Leonardo Sajulga", fill='black', font = ("Times", 10, "bold"))
    canvas3.create_text(220, 330, text = "Researcher", fill='#FD7014', font = ("Calibri", 12, "bold"))
    canvas3.create_text(220, 430, text = "Shainie Derita", fill='black', font = ("Times", 10, "bold"))
    canvas3.create_text(500, 330, text = "Researcher", fill='#FD7014', font = ("Calibri", 12, "bold"))
    canvas3.create_text(500, 430, text = "Princess Junta Tanqui-on", fill='black', font = ("Times", 10, "bold"))
    canvas3.create_text(770, 330, text = "Researcher", fill='#FD7014', font = ("Calibri", 12, "bold"))
    canvas3.create_text(770, 430, text = "Kimjie Anoc", fill='black', font = ("Times", 10, "bold"))

    text = "     VillaXpress offers a reliable and efficient\nparcel system for all your shipping needs. Trust\n  us to deliver packages with care and on time."
    CTkLabel(frame, text = text, font = ("Times", 25, "bold"), text_color = 'black', fg_color = "white").place(x = 260, y = 543)


def contact():
    home_b.configure(fg = "black")
    register_b.configure(fg = "black")
    search_b.configure(fg = "black")
    about_b.configure(fg = "black")
    contact = Frame(system, width = 990, height = 600, bg = "white")
    contact.place(x = 0, y = 68)
    Label(contact, text = "Contacts", bg = 'white', fg = '#FD7014', font = ("Times", 30, "bold")).place(x = 420, y = 10)
    CTkFrame(contact, height = 400, width = 250, fg_color="white", border_color= "#FD7014", border_width=5).place(x = 90, y = 120)
    Label(contact, image = ad_image, highlightthickness=0).place(x = 150, y = 130)
    address = "Province: Misamis Oriental\n\nMunicipality: Villanueva\n\nBarangay:Poblacion 2\n\nPostal Code:9002\n\nRegion: Northern Mindanao\n\nRegion: X\n\nPhilippines: Mindanao"
    Label(contact, text = address, bg = 'white', fg = '#FD7014', font = ("Times", 12, "bold")).place(x = 115, y = 250)
    CTkFrame(contact, height = 400, width = 250, fg_color="white", border_color= "#FD7014", border_width=5).place(x = 380, y = 120)
    Label(contact, image = con_image, highlightthickness=0).place(x = 440, y = 130)
    contacts = "Company:\n\n 09533600996\n\nFounder :\n\n09275724647 \n\nDeveloper:\n\n 09673271230"
    Label(contact, text = contacts, bg = 'white', fg = '#FD7014', font = ("Times", 14, "bold")).place(x = 445, y = 260)
    CTkFrame(contact, height = 400, width = 250, fg_color="white", border_color= "#FD7014", border_width=5).place(x = 665, y = 120)
    email = "Company\n\n villaexpress@gmail.com\n\nFounder :\n\nkimharryoclarit@hotmail.com \n\nDeveloper:\n\n cosmiano.joseph02@gmail.com"
    Label(contact, text = email, bg = 'white', fg = '#FD7014', font = ("Times", 12, "bold")).place(x = 680, y = 260)
    Label(contact, image = em_image, highlightthickness=0).place(x = 725, y = 130)


def discover():

    home_b.configure(fg = "black")
    register_b.configure(fg = "black")
    search_b.configure(fg = "black")
    about_b.configure(fg = "black")
    style = ttk.Style()
    style.theme_use('default')
    style.configure('TFrame', background= "white")
    discover = Frame(system, width = 990, height = 600, bg = "white")
    discover.place(x = 0, y = 68)

    canvas = Canvas(discover, width=970, height=600, bg = "white")
    canvas.pack(side='left', fill='both', expand=True)
    scrollbar = CTkScrollbar(discover, orientation='vertical', command=canvas.yview)
    scrollbar.pack(side='right', fill='y')
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollable_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    r = "By registering with our Parcel Tracking System, you gain access to a\n personalized dashboard where you can conveniently manage and track\nall your parcels in one place. Registration is quick and easy, allowing you\nto enjoy the full benefits of our tracking system."
    s = "Our powerful search functionality enables you to effortlessly\nlocate your parcels by simply entering the tracking number\nor relevant details. With real-time updates and comprehensive\ntracking information, you can stay informed about the current\nstatus and estimated delivery time of your packages."
    a = "Discover more about our Parcel Tracking System and the values\nwe uphold. Learn about our commitment to providing a seamless\ntracking experience, our dedication to customer satisfaction, and\nour continuous efforts to improve the efficiency and reliability of\nour services. Find out how we strive to exceed your expectations."
    c = "Have a question or need assistance? Our customer support team\nis here to help. Whether you have inquiries about tracking your\nparcels, encountering issues, or seeking additional information,\n we are just a click or a call away. Reach out to us via our contact\ndetails, and our friendly representatives will provide prompt and\nreliable support."
    con = "\n\n\n\nExperience the convenience and peace of mind that comes with\nour Parcel Tracking System. Register today, search for your parcels\neffortlessly, learn more about our commitment to excellence, and\ncontact us for any assistance you may need. We are dedicated to\nensuring your tracking experience is as smooth and efficient as possible.\n\n\n\n\n"
    Label(scrollable_frame, text = "Learn More about our Parcel Tracking System", font = ("Times", 25, "bold"), bg= "white").pack(padx = 140, pady = 10)
    Label(scrollable_frame, text = "Register Parcel: ", font = ("Times", 25, "bold"), fg = '#FD7014', bg= "white").pack(padx = 140, pady = 40)
    Label(scrollable_frame, text = r, font = ("Times", 18, "bold"), bg= "white").pack(padx = 140, pady = 1)
    Label(scrollable_frame, text = "Search Parcel: ", font = ("Times", 25, "bold"), fg = '#FD7014', bg= "white").pack(padx = 140, pady = 50)
    Label(scrollable_frame, text = s, font = ("Times", 18, "bold"), bg= "white").pack(padx = 140, pady = 1)
    Label(scrollable_frame, text = "About Us: ", font = ("Times", 25, "bold"), fg = '#FD7014', bg= "white").pack(padx = 140, pady = 60)
    Label(scrollable_frame, text = a, font = ("Times", 18, "bold"), bg= "white").pack(padx = 140, pady = 1)
    Label(scrollable_frame, text = "Contact Us: ", font = ("Times", 25, "bold"), fg = '#FD7014', bg= "white").pack(padx = 140, pady = 70)
    Label(scrollable_frame, text = c, font = ("Times", 18, "bold"), bg= "white").pack(padx = 140, pady = 1)
    Label(scrollable_frame, text = con, font = ("Times", 18, "bold"), bg= "white").pack(padx = 140, pady = 1)



#Main Page
#Navigation Bar Animation
#Mouse In
def Hover1(event):
    home_b.configure(fg = "white", width = 14, height = 2, font = "Arial 16 bold")
    home_b.place(x = 225)       
def Hover2(event):
    register_b.configure(fg = "#FD7014", width = 14, height = 2, font = "Arial 16 bold")
    register_b.place(x = 415)
def Hover3(event):
    search_b.configure(fg = "#FD7014", width = 14, height = 2, font = "Arial 16 bold")
    search_b.place(x = 605)
def Hover4(event):
    about_b.configure(fg = "#FD7014", width = 14, height = 2, font = "Arial 16 bold")
    about_b.place(x = 795)

#Mouse Out
def Hover5(event):
    home_b.configure(bg = "#FD7014", fg = "black", width = 15, height = 2, font = "Arial 15 bold")
    home_b.place(x = 230)

def Hover6(event):
    register_b.configure(bg = "white", fg = "black", width = 15, height = 2, font = "Arial 15 bold")
    register_b.place(x = 420)
 
def Hover7(event):
    search_b.configure(bg = "white", fg = "black", width = 15, height = 2, font = "Arial 15 bold")
    search_b.place(x = 610)

def Hover8(event):
    about_b.configure(bg = "white", fg = "black", width = 15, height = 2, font = "Arial 15 bold")
    about_b.place(x = 800)


def home_invoke(event):
    home_b.configure(fg = "white")
    register_b.configure(fg = "black")
    search_b.configure(fg = "black")
    about_b.configure(fg = "black")
def register_invoke(event):
    home_b.configure(fg = "black")
    register_b.configure(fg = "#FD7014")
    search_b.configure(fg = "black")
    about_b.configure(fg = "black")
def search_invoke(event):
    home_b.configure(fg = "black")
    register_b.configure(fg = "black")
    search_b.configure(fg = "#FD7014")
    about_b.configure(fg = "black")
def about_invoke(event):
    home_b.configure(fg = "black")
    register_b.configure(fg = "black")
    search_b.configure(fg = "black")
    about_b.configure(fg = "#FD7014")

navbar = Frame(system, height = 70, width = 990, bg = 'white').place(x = 0, y = 0)
Label(navbar, image = logo, bd= 3, highlightthickness = 0, relief = FLAT).place(x = 20, y = 0)
home_b = Button(navbar, text = 'Home', width = 16, height = 2, bg="#FD7014", fg="white",  font = "Arial 15 bold", bd= 1, highlightthickness = 0, relief = FLAT, activebackground = "#FD7014", activeforeground="white", command = home)
home_b.place(x = 230)
home_b.bind("<Enter>", Hover1)
home_b.bind("<Leave>", Hover5)
home_b.bind("<Button-1>", home_invoke)
register_b = Button(navbar, text = 'Register',bg = "white", width = 16, height = 2, font = "Arial 15 bold", bd= 1, highlightthickness = 0, relief = FLAT, activebackground = "white", activeforeground="#FD7014", command = register)
register_b.place(x = 420)
register_b.bind("<Enter>", Hover2)
register_b.bind("<Leave>", Hover6)
register_b.bind("<Button-1>", register_invoke)
search_b = Button(navbar, text = 'Search',bg = "white", width = 16, height = 2, font = "Arial 15 bold", bd= 1, highlightthickness = 0, relief = FLAT, activebackground = "white", activeforeground="#FD7014", command = search)
search_b.place(x = 610)
search_b.bind("<Enter>", Hover3)
search_b.bind("<Leave>", Hover7)
search_b.bind("<Button-1>", search_invoke)
about_b = Button(navbar, text = 'About Us',bg = "white", width = 16, height = 2, font = "Arial 15 bold", bd= 1, highlightthickness = 0, relief = FLAT, activebackground = "white", activeforeground="#FD7014", command = about)
about_b.place(x = 800)
about_b.bind("<Enter>", Hover4)
about_b.bind("<Leave>", Hover8)
about_b.bind("<Button-1>", about_invoke)

home_b.configure(fg = "white")
register_b.configure(fg = "black")
search_b.configure(fg = "black")
about_b.configure(fg = "black")
home()
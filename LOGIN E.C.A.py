import tkinter as tk
from tkinter import Image, Tk, messagebox
import tkinter
from tkinter.tix import IMAGETEXT

import mysql.connector

def login():
    input_user = entry_user.get()
    input_pass = entry_pass.get()
    login_type = login_var.get()

    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sagarme",
            database="grocery_store"
        )

        cursor = connection.cursor()

        if login_type == "Customer":
            query = "SELECT * FROM customers WHERE username = %s AND password = %s"
            cursor.execute(query, (input_user, input_pass))
            row = cursor.fetchone()
            if row:
                customer_id = row[0]
                messagebox.showinfo("Login Successful", f"Welcome, Customer {row[1]} {row[2]}!")
                # Perform actions for successful customer login
            else:
                messagebox.showerror("Login Failed", "Invalid username or password.")

        elif login_type == "Admin":
            if input_user == "Admin" and input_pass == "dbms_pro1":
                messagebox.showinfo("Login Successful", "Welcome, Admin!")
                # Perform actions for successful admin login
            else:
                messagebox.showerror("Login Failed", "Invalid username or password.")

        elif login_type == "Employee":
            query = "SELECT * FROM employee WHERE username = %s AND password = %s"
            cursor.execute(query, (input_user, input_pass))
            row = cursor.fetchone()
            if row:
                messagebox.showinfo("Login Successful", f"Welcome, Employee {row[1]}!")
                # Perform actions for successful employee login
            else:
                messagebox.showerror("Login Failed", "Invalid username or password.")

        else:
            messagebox.showerror("Error", "Invalid login type.")

    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to connect to MySQL: {error}")

    finally:
        if 'connection' in locals():
            connection.close()

# Tkinter setup
            
root = tk.Tk()
root.geometry("1270x700+0+0")
root.title("Login")
main_frame=tk.Frame(root, bg='light blue')
main_frame.place(x=500, y=260, width=600, height=400)

img_logo = Image.open('images/pngegg (1).png')
img_logo = img_logo.resize((50, 50))
photo_logo = IMAGETEXT.PhotoImage(img_logo)
logo =tk. Label(root, image=photo_logo)
logo.place(x=20, y=20, width=50, height=50)

login_var = tk.StringVar()
login_var.set("select") 

lbl_user =tk. Label(main_frame, text="username", font=('times new roman', 20), bg='light blue')
lbl_user.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_user =tk. Entry(main_frame, font=('times new roman', 14),bg='pink')
entry_user.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # password
lbl_pass =tk. Label(main_frame, text="password", font=('times new roman', 20), bg='lightblue')
lbl_pass.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_pass =tk. Entry(main_frame, font=('times new roman', 14),show="*",bg='pink')
entry_pass.grid(row=1, column=1, padx=10, pady=5, sticky="w")




label_login_type = tk.Label(main_frame, text="Login Type",font=('times new roman', 20), bg='lightblue')
label_login_type.grid(row=2, column=0, sticky="w")
option_menu = tk.OptionMenu(main_frame, login_var, "Customer", "Admin", "Employee")
option_menu.grid(row=2, column=1,padx=10,pady=5,sticky="w")

button_login = tk.Button(main_frame, text="Login", command=login,bg="blue",width=20,height=2)
button_login.grid(row=3, column=1, padx=10, pady=50, sticky="w")

root.mainloop()


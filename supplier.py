from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

class grocerysupplier:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1270x700+0+0")
        self.root.title('SUPPLIER')

        # Variables
        self.var_supplier_id = StringVar()
        self.var_name = StringVar()
        self.var_phone = StringVar()
        self.var_description = StringVar()

        # Title label
        lab_title = Label(self.root, text="Supplier Details", font=('times new roman', 37, 'bold'), fg='darkblue', bg='white')
        lab_title.place(x=0, y=0, width=1270, height=50)

        # Image logo
        img_logo = Image.open('images/pngegg (1).png')
        img_logo = img_logo.resize((50, 50))
        self.photo_logo = ImageTk.PhotoImage(img_logo)
        self.logo = Label(self.root, image=self.photo_logo)
        self.logo.place(x=420, y=0, width=50, height=50)

        # Main frame
        main_frame = Frame(self.root, bd=3, relief=RIDGE, bg='light blue')
        main_frame.place(x=5, y=160, width=1270, height=470)

        Label(root,text="grocery store|develop by xxxx",bg="#c36464",fg='#fff',font='arial 10 bold').pack(side=BOTTOM,fill=X)

        # Lower frame


        # Employee ID
        lbl_supplier_id = Label(main_frame, text="Supplier ID:", font=('times new roman', 20), bg='light blue')
        lbl_supplier_id.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        entry_supplier_id = Entry(main_frame, textvariable=self.var_supplier_id, font=('times new roman', 14), bd=2, relief=RIDGE)
        entry_supplier_id.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Name
        lbl_name = Label(main_frame, text="Name:", font=('times new roman', 20), bg='lightblue')
        lbl_name.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        entry_name = Entry(main_frame, textvariable=self.var_name, font=('times new roman', 14), bd=2, relief=RIDGE)
        entry_name.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Phone
        lbl_phone = Label(main_frame, text="Phone:", font=('times new roman', 20), bg='light blue')
        lbl_phone.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        entry_phone = Entry(main_frame, textvariable=self.var_phone, font=('times new roman', 14), bd=2, relief=RIDGE)
        entry_phone.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Description
        lbl_description = Label(main_frame, text="Description:", font=('times new roman', 20), bg='lightblue')
        lbl_description.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        txt_description = Text(main_frame, font=('times new roman', 14), bd=2, relief=RIDGE, height=5,width=50)
        txt_description.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Image in upper frame
        img5 = Image.open('images/pngmage5.png')
        img5 = img5.resize((130, 220))
        self.photo5 = ImageTk.PhotoImage(img5)
        img_5 = Label(main_frame, image=self.photo5)
        img_5.place(x=470, y=320, width=180, height=220)

        #button

        btn_add = Button(main_frame, text='SAVE',command=self.add_supplier, font=("arial", 15, 'bold'), width=13, bg='light green')
        btn_add.place(x=40,y=320,width=100,height=40)

        btn_update = Button(main_frame, text='UPDATE',command=self.update_supplier, font=("arial", 15, 'bold'), width=13, bg='purple')
        btn_update.place(x=150,y=320,width=100,height=40)

        btn_delete = Button(main_frame, text='DELETE',command=self.delete_supplier, font=("arial", 15, 'bold'), width=13, bg='yellow')
        btn_delete.place(x=260,y=320,width=100,height=40)

        btn_clear = Button(main_frame, text='CLEAR',command=self.reset_supplier_data, font=("arial", 15, 'bold'), width=13, bg='brown')
        btn_clear.place(x=370,y=320,width=100,height=40)

        #SEARCH
        

        search_by = Label(main_frame, font=('arial 10 bold'), text='SEARCH BY:', fg='white', bg='brown')
        search_by.grid(row=0,column=3,padx=5)

        self.var_com_search = StringVar()
        com_txt_search = ttk.Combobox(main_frame, textvariable=self.var_com_search, state="readonly", font=("arial", 12, "bold"), width=18)
        com_txt_search['value'] = ('select option', 'supplier_id', 'phone')
        com_txt_search.grid(row=0, column=4, sticky=W, padx=5)

        self.var_search = StringVar()
        txt_search = ttk.Entry(main_frame, textvariable=self.var_search, width=22, font=("arial", 11, "bold"))
        txt_search.grid(row=0, column=5, padx=5)

        btn_search = Button(main_frame, text="Search",command=self.search_data, font=('arial', 11, 'bold'), width=14, bg='brown')
        btn_search.grid(row=0, column=6, padx=5)

        btn_showall=Button(main_frame,text="SHOW all",command=self.fetch_supplier_data,font=('arial',11,'bold'),width=14,bg='brown')
        btn_showall.place(x=500,y=10)


        
        table_frame = Frame(main_frame, bd=5, relief=RIDGE, bg='white')
        table_frame.place(x=650, y=70, width=610, height=400)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.supplier_table = ttk.Treeview(table_frame, column=('supplier_id', 'name', 'phone', 'description'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.supplier_table.xview)
        scroll_y.config(command=self.supplier_table.yview)

        self.supplier_table.heading('supplier_id', text='ID')
        self.supplier_table.heading('name', text='Name')
        self.supplier_table.heading('phone', text='Phone')
        self.supplier_table.heading('description', text='Description')

        self.supplier_table['show'] = 'headings'
        self.supplier_table.column("supplier_id", width=100)
        self.supplier_table.column("name", width=100)
        self.supplier_table.column("phone", width=100)
        self.supplier_table.column("description", width=100)
        self.supplier_table.pack(fill=BOTH,expand=1)
        self.supplier_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_supplier_data()


    def add_supplier(self):
        if self.var_name.get() == "" or self.var_phone.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='sagarme', database='grocery_store')
                my_cursor = conn.cursor()
                
                # Check if the phone number already exists in the database
                my_cursor.execute("SELECT * FROM supplier WHERE phone = %s", (self.var_phone.get(),))
                result = my_cursor.fetchone()
                if result:
                    messagebox.showerror("Error", "Phone number already exists!")
                else:
                    # If the phone number doesn't exist, proceed with adding the supplier
                    my_cursor.execute("INSERT INTO supplier (supplier_id, name, phone, description) VALUES (%s, %s, %s, %s)",
                                      (self.var_supplier_id.get(), self.var_name.get(), self.var_phone.get(), self.var_description.get()))
                    conn.commit()
                    self.fetch_supplier_data()
                    conn.close()
                    messagebox.showinfo("Success", "Supplier added successfully!")
            except Exception as es:
                messagebox.showerror("Error", f"Error adding supplier: {str(es)}")
    
    def fetch_supplier_data(self):
        try:
            conn = mysql.connector.connect(host='localhost', username='root', password='sagarme', database='grocery_store')
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM supplier")
            data = my_cursor.fetchall()
            if len(data) != 0:
                self.supplier_table.delete(*self.supplier_table.get_children())
                for i in data:
                    self.supplier_table.insert("", END, values=i)
                conn.commit()
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching supplier data: {str(e)}")
    def update_supplier(self):
        if self.var_name.get() == "" or self.var_phone.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                update = messagebox.askyesno('Update', "Are you sure you want to update this supplier?")
                if update:
                    conn = mysql.connector.connect(host='localhost', username='root', password='sagarme', database='grocery_store')
                    my_cursor = conn.cursor()
                    my_cursor.execute("UPDATE supplier SET name=%s, phone=%s, description=%s WHERE supplier_id=%s",
                                      (self.var_name.get(), self.var_phone.get(), self.var_description.get(), self.var_supplier_id.get()))
                    conn.commit()
                    self.fetch_supplier_data()
                    conn.close()
                    messagebox.showinfo("Success", "Supplier details updated successfully!")
            except Exception as es:
                messagebox.showerror("Error", f"Error updating supplier: {str(es)}")

    def delete_supplier(self):
        if self.var_supplier_id.get() == "":
            messagebox.showerror("Error", "Supplier ID is required")
        else:
            try:
                delete = messagebox.askyesno("Delete", "Are you sure you want to delete this supplier?")
                if delete:
                    conn = mysql.connector.connect(host='localhost', username='root', password='sagarme', database='grocery_store')
                    my_cursor = conn.cursor()
                    my_cursor.execute("DELETE FROM supplier WHERE supplier_id=%s", (self.var_supplier_id.get(),))
                    conn.commit()
                    self.fetch_supplier_data()
                    conn.close()
                    messagebox.showinfo("Success", "Supplier deleted successfully!")
            except Exception as es:
                messagebox.showerror("Error", f"Error deleting supplier: {str(es)}")

    def reset_supplier_data(self):
        self.var_supplier_id.set("")
        self.var_name.set("")
        self.var_phone.set("")
        self.var_description.set("")
#search function========
    def search_data(self):
        if self.var_com_search.get() == "" or self.var_search.get() == "":
            messagebox.showerror("Error", "Please select an option")
        else:
            try:
                conn = mysql.connector.connect(
                    host='localhost',
                    username='root',
                    password='sagarme',
                    database='grocery_store'
                )
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM supplier WHERE " + str(self.var_com_search.get()) + " LIKE '%" + str(self.var_search.get()) + "%'")
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.supplier_table.delete(*self.supplier_table.get_children())
                    for row in rows:
                        self.supplier_table.insert("", END, values=row)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
    def get_cursor(self, event):
        cursor_row = self.supplier_table.focus()
        content = self.supplier_table.item(cursor_row)
        data = content['values']

        self.var_supplier_id.set(data[0])
        self.var_name.set(data[1])
        self.var_phone.set(data[2])
        self.var_description.set(data[3]) 


if __name__ == "__main__":
    root = Tk()
    d = grocerysupplier(root)
    root.mainloop()

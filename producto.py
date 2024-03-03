from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

class groceryproduct:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1270x700+0+0")
        self.root.title('product')
        self.root.config(bg="white")
        self.root.focus_force()
        #variable
        self.product_id_var=StringVar()
        self.category_var = StringVar()
        self.supplier_var = StringVar()
        self.product_name_var = StringVar()
        self.quantity_var = IntVar()
        self.price_var = DoubleVar()
        self.status_var = StringVar()
        self.var_com_search=StringVar()
        self.var_search=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        #product frame=========
        product_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_frame.place(x=10,y=10,width=500,height=500)


        title=Label(product_frame,text='Manage product details',font=("groudy old style",15),bg="#0f4d7d",fg="white")
        title.pack(side=TOP,fill=X)
        #label==========
        self.lbl_category=Label(product_frame,text="Category",font=("groudy old style",18),bg="white").place(x=30,y=60)
        self. lbl_supplier=Label(product_frame,text="supplier",font=("groudy old style",18),bg="white").place(x=30,y=110)
        self .lbl_product_name=Label(product_frame,text="productname",font=("groudy old style",18),bg="white").place(x=30,y=160)
        self .lbl_quantity=Label(product_frame,text="quantity",font=("groudy old style",18),bg="white").place(x=30,y=210)
        self. lbl_price=Label(product_frame,text="price",font=("groudy old style",18),bg="white").place(x=30,y=260)
        self. lbl_status=Label(product_frame,text="status",font=("groudy old style",18),bg="white").place(x=30,y=310)
        #entry and combo======
        category_combo = ttk.Combobox(product_frame, textvariable=self.category_var,values=self.cat_list, state="readonly")
        category_combo.place(x=200, y=60)
        category_combo.current(0)

        supplier_combo = ttk.Combobox(product_frame, textvariable=self.supplier_var,values=self.sup_list ,state="readonly")
        supplier_combo.place(x=200, y=110)
        supplier_combo.current(0)

        product_name_entry = Entry(product_frame, textvariable=self.product_name_var, font=("groudy old style", 18))
        product_name_entry.place(x=200, y=160)

        quantity_entry = Entry(product_frame, textvariable=self.quantity_var, font=("groudy old style", 18))
        quantity_entry.place(x=200, y=210)

        price_entry = Entry(product_frame, textvariable=self.price_var, font=("groudy old style", 18))
        price_entry.place(x=200, y=260)

        status_combo = ttk.Combobox(product_frame, textvariable=self.status_var, values=("select","active","Inactive"),font=("groudy old style", 18))
        status_combo.place(x=200, y=310)
        status_combo.current(0)
        #button 
        btn_add=Button(product_frame,text='SAVE',command=self.add_product,font=("arial",15,'bold'),width=13,bg='blue',cursor="hand2")
        btn_add.place(x=10 ,y=400 ,width=100 ,height=40)

        btn_update=Button(product_frame,text='UPDATE',command=self.update_product,font=("arial",15,'bold'),width=13,bg='blue',cursor="hand2")
        btn_update.place(x=130 ,y=400 ,width=100 ,height=40)

        btn_delete=Button(product_frame,text='DELETE',command=self.delete_product,font=("arial",15,'bold'),width=13,bg='blue',cursor="hand2")
        btn_delete.place(x=240 ,y=400 ,width=100 ,height=40)

        btn_clear=Button(product_frame,text='CLEAR',command=self.clear,font=("arial",15,'bold'),width=13,bg='blue',cursor="hand2")
        btn_clear.place(x=350 ,y=400 ,width=100 ,height=40)

        btn_back=Button(product_frame,text='BACK',command=self.back_to_home,font=("arial",15,'bold'),width=13,bg='red',cursor="hand2")
        btn_back.place(x=350 ,y=450 ,width=100 ,height=40)
        #image=========
        img8 = Image.open('images/img8.jpg')
        img8 = img8.resize((500, 180)) 
        self.photo8 = ImageTk.PhotoImage(img8)
        self.img_8 = Label(self.root, image=self.photo8)
        self.img_8.place(x=10, y=510, width=500, height=180)

        



        #searchframe=========
        search_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text='Search product info',fg='red',bg='light pink')
        search_frame.place(x=550,y=10,width=700,height=60)

        com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,state="readonly",font=("arial",12,"bold"),width=18)
        com_txt_search['value']=('select',"category","supplier","name")
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)
        com_txt_search.current(0)


        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=("arial",11,"bold"))
        txt_search.grid(row=0,column=2,padx=5)
        btn_search=Button(search_frame,text="search",font=('arial',11,'bold'),width=14,bg='brown')
        btn_search.grid(row=0,column=3,)

        #product table==============================

        table_frame = Frame(self.root, bd=3, relief=RIDGE, bg='white')
        table_frame.place(x=550, y=70, width=700, height=500)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.product_table=ttk.Treeview(table_frame,column=('product_id','category','supplier','name','quantity','price','status'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.product_table.xview)
        scroll_y.config(command=self.product_table.yview)

        self.product_table.heading('product_id',text='Id')
        self.product_table.heading('category',text='Category')
        self.product_table.heading('supplier',text='supplier')
        self.product_table.heading('name',text='name')
        self.product_table.heading('quantity',text='quantity')
        self.product_table.heading('price',text='price')
        self.product_table.heading('status',text='STATUS')
        
        

        self.product_table['show']='headings'
        self.product_table.column("product_id",width=30)
        self.product_table.column("category",width=30)
        self.product_table.column("supplier",width=30)
        self.product_table.column("name",width=30)
        self.product_table.column("quantity",width=30)
        self.product_table.column("price",width=30)
        self.product_table.column("status",width=30)
       
        
        

        self.product_table.pack(fill=BOTH,expand=1)
        self.product_table.bind("<ButtonRelease-1>",self.get_product)
        self.show_products()
        self.fetch_cat_sup()


    def fetch_cat_sup(self):
                self.cat_list.append("empty")
                self.sup_list.append("empty")
                
                conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="sagarme",
                database="grocery_store"  
            )
                cursor = conn.cursor()
                try:
                    cursor.execute("SELECT name from category")
                    cat=cursor.fetchall()
                    self.cat_list.append("empty")
                    if len(cat)>0:
                        del self.cat_list[:]
                        self.cat_list.append("select")

                        for i in cat:
                            self.cat_list.append(i[0])

                    cursor.execute("SELECT name from supplier")
                    sup=cursor.fetchall()
                    self.sup_list.append("empty")
                    if len(sup)>0:
                        del self.sup_list[:]
                        self.sup_list.append("select")

                        for i in sup:
                          self.sup_list.append(i[0])

                    



                except mysql.connector.Error as e:
                  messagebox.showerror("Error", f"Error adding product: {e}")    


    def add_product(self):
    # Get values from entry boxes and comboboxes
        category = self.category_var.get()
        supplier = self.supplier_var.get()
        product_name = self.product_name_var.get()
        quantity = self.quantity_var.get()
        price = self.price_var.get()
        status = self.status_var.get()
    
    # Check if any field is empty
        if category == "" or supplier == "" or product_name == "" or quantity == "" or price == "" or status == "":
            messagebox.showerror("Error", "Please fill in all fields.")
            return

    # Connect to MySQL database
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="sagarme",
                database="grocery_store" 
            )
            cursor = conn.cursor()

            # Check if product name already exists
            cursor.execute("SELECT * FROM products WHERE name = %s", (product_name,))
            existing_product = cursor.fetchone()
            if existing_product:
                messagebox.showerror("Error", "Product already exists.")
                return
    
            # Insert into database
            cursor.execute("INSERT INTO products (category, supplier, name, quantity, price, status) VALUES (%s, %s, %s, %s, %s, %s)",
                           (category, supplier, product_name, quantity, price, status))
            conn.commit()
            messagebox.showinfo("Success", "Product added successfully!")
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error adding product: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
                self.show_products() 
    def show_products(self):
        try:
            # Connect to MySQL 
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="sagarme",
                database="grocery_store" 
            )
            cursor = conn.cursor()

            # Fetch products from the database
            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()
    
            # Clear existing items in the product table
            for i in self.product_table.get_children():
                self.product_table.delete(i)

            # Insert fetched products into the product table
            for product in products:
                self.product_table.insert('', END, values=product)

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error fetching products: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()


    def get_product(self,event):
        f=self.product_table.focus()
        content=(self.product_table.item(f))
        row=content['values']
        self.product_id_var.set(row[0])
        self.category_var.set(row[1]),
        self.supplier_var.set(row[2]),
        self.product_name_var.set(row[3]),
        self.quantity_var.set(row[4]),
        self.price_var.set(row[5]),
        self.status_var.set(row[6])


    def update_product(self):
        try:
            # Check if a product is selected
            selected_item = self.product_table.selection()
            if not selected_item:
                messagebox.showerror("Error", "Please select a product to update.")
                return
    
            # Get the product ID of the selected product
            product_id = self.product_table.item(selected_item)['values'][0]
            if not product_id:
                messagebox.showerror("Error", "Please select a product to update.")
                return
    
                # Connect to MySQL database
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="sagarme",
                database="grocery_store"  
            )
            cursor = conn.cursor()
    
            category = self.category_var.get()
            supplier = self.supplier_var.get()
            product_name = self.product_name_var.get()
            quantity = self.quantity_var.get()
            price = self.price_var.get()
            status = self.status_var.get()

        
            cursor.execute("UPDATE products SET category = %s, supplier = %s, name = %s, quantity = %s, price = %s, status = %s WHERE product_id = %s",
                           (category, supplier, product_name, quantity, price, status, product_id))
            conn.commit()
            messagebox.showinfo("Success", "Product updated successfully!")

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error updating product: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
                self.show_products()

    def delete_product(self):
        try:
            # Check if a product is selected
            selected_item = self.product_table.selection()
            if not selected_item:
                messagebox.showerror("Error", "Please select a product to delete.")
                return

        # Get the product ID of the selected product
            product_id = self.product_table.item(selected_item)['values'][0]
            if not product_id:
                messagebox.showerror("Error", "Please select a product to delete.")
                return
    
            # Connect to MySQL database
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="sagarme",
                database="grocery_store"  
            )
            cursor = conn.cursor()
    
            cursor.execute("DELETE FROM products WHERE product_id = %s", (product_id,))
            conn.commit()
            messagebox.showinfo("Success", "Product deleted successfully!")

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error deleting product: {e}")
        finally:
            if conn is not None and conn.is_connected():
                cursor.close()
                conn.close()
                self.show_products()

    def clear(self):
      self.category_var.set("")
      self.supplier_var.set("")
      self.product_name_var.set("")
      self.quantity_var.set("")
      self.price_var.set("")
      self.status_var.set("")

    def back_to_home(self):
        self.root.destroy()


        

if __name__=="__main__":
  root = Tk()
  app = groceryproduct(root)
  root.mainloop()

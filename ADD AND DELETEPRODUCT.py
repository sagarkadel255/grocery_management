import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

# Function to establish a MySQL connection
def get_sql_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='sagarme',
        database='grocery_store'
    )

# Function to insert a new product
def insert_product():
    name = name_entry.get()
    category = category_entry.get()
    quantity = int(quantity_entry.get())
    price = float(price_entry.get())
    
    if name and category and quantity and price:
        try:
            connection = get_sql_connection()
            cursor = connection.cursor()
            query = "INSERT INTO products (name, category, quantity, price) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (name, category, quantity, price))
            connection.commit()
            connection.close()
            messagebox.showinfo("Success", "Product inserted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", "Please fill all fields.")

# Function to delete a product
def delete_product():
    product_id = int(product_id_entry.get())
    if product_id:
        try:
            connection = get_sql_connection()
            cursor = connection.cursor()
            query = "DELETE FROM products WHERE product_id = %s"
            cursor.execute(query, (product_id,))
            connection.commit()
            connection.close()
            messagebox.showinfo("Success", "Product deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", "Please enter product ID.")

# Create the main window
root = tk.Tk()
root.title("Product Management System")

# Create a frame for inserting products
insert_frame = ttk.LabelFrame(root, text="Insert Product")
insert_frame.grid(row=0, column=0, padx=10, pady=10)

name_label = ttk.Label(insert_frame, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = ttk.Entry(insert_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

category_label = ttk.Label(insert_frame, text="Category:")
category_label.grid(row=1, column=0, padx=5, pady=5)
category_entry = ttk.Entry(insert_frame)
category_entry.grid(row=1, column=1, padx=5, pady=5)

quantity_label = ttk.Label(insert_frame, text="Quantity:")
quantity_label.grid(row=2, column=0, padx=5, pady=5)
quantity_entry = ttk.Entry(insert_frame)
quantity_entry.grid(row=2, column=1, padx=5, pady=5)

price_label = ttk.Label(insert_frame, text="Price:")
price_label.grid(row=3, column=0, padx=5, pady=5)
price_entry = ttk.Entry(insert_frame)
price_entry.grid(row=3, column=1, padx=5, pady=5)

insert_button = ttk.Button(insert_frame, text="Insert", command=insert_product)
insert_button.grid(row=4, columnspan=2, padx=5, pady=5, sticky="we")

# Create a frame for deleting products
delete_frame = ttk.LabelFrame(root, text="Delete Product")
delete_frame.grid(row=0, column=1, padx=10, pady=10)

product_id_label = ttk.Label(delete_frame, text="Product ID:")
product_id_label.grid(row=0, column=0, padx=5, pady=5)
product_id_entry = ttk.Entry(delete_frame)
product_id_entry.grid(row=0, column=1, padx=5, pady=5)

delete_button = ttk.Button(delete_frame, text="Delete", command=delete_product)
delete_button.grid(row=1, columnspan=2, padx=5, pady=5, sticky="we")

root.mainloop()


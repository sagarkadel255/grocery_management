import tkinter as tk
from tkinter import ttk
import mysql.connector

class GroceryStoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Grocery Store")

        # Establish database connection
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="sagarme",  # Replace with your MySQL password
            database="grocery_store"
        )
        self.cursor = self.connection.cursor()

        self.create_widgets()

    def create_widgets(self):
        # Header
        self.header = tk.Label(self.root, text="Grocery Store", font=('Helvetica', 24))
        self.header.pack()

        # Navigation Tabs
        self.tabControl = ttk.Notebook(self.root)

        # Products Tab
        self.products_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.products_tab, text="Products Database")

        self.products_frame = tk.Frame(self.products_tab)
        self.products_frame.pack()

        self.products_label = tk.Label(self.products_frame, text="Products:")
        self.products_label.grid(row=0, column=0)

        self.display_products()

        # Customers Tab
        self.customers_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.customers_tab, text="Customer List")

        self.customers_frame = tk.Frame(self.customers_tab)
        self.customers_frame.pack()

        self.customers_label = tk.Label(self.customers_frame, text="Customers:")
        self.customers_label.grid(row=0, column=0)

        self.display_customers()

        # Orders Tab
        self.orders_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.orders_tab, text="Orders")

        self.orders_frame = tk.Frame(self.orders_tab)
        self.orders_frame.pack()

        self.orders_label = tk.Label(self.orders_frame, text="Orders:")
        self.orders_label.grid(row=0, column=0)

        self.display_orders()

        # Categories Tab
        self.categories_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.categories_tab, text="Categories")

        self.categories_frame = tk.Frame(self.categories_tab)
        self.categories_frame.pack()

        self.categories_label = tk.Label(self.categories_frame, text="Categories:")
        self.categories_label.grid(row=0, column=0)

        self.display_categories()

        # Total Sales Tab
        self.sales_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.sales_tab, text="Total Sales")

        self.sales_frame = tk.Frame(self.sales_tab)
        self.sales_frame.pack()

        self.sales_label = tk.Label(self.sales_frame, text="Total Sales:")
        self.sales_label.grid(row=0, column=0)

        self.display_total_sales()

        # Pack the tab control
        self.tabControl.pack(expand=1, fill="both")

    def display_products(self):
        # Fetch products from database
        self.cursor.execute("SELECT * FROM products")
        products = self.cursor.fetchall()

        # Display products in a table
        for i, product in enumerate(products):
            for j, item in enumerate(product):
                label = tk.Label(self.products_frame, text=item)
                label.grid(row=i+1, column=j)

    def display_customers(self):
        # Fetch customers from database
        self.cursor.execute("SELECT * FROM customers")
        customers = self.cursor.fetchall()

        # Display customers in a table
        for i, customer in enumerate(customers):
            for j, item in enumerate(customer):
                label = tk.Label(self.customers_frame, text=item)
                label.grid(row=i+1, column=j)

    def display_orders(self):
        # Fetch orders from database
        self.cursor.execute("SELECT * FROM orders")
        orders = self.cursor.fetchall()

        # Display orders in a table
        for i, order in enumerate(orders):
            for j, item in enumerate(order):
                label = tk.Label(self.orders_frame, text=item)
                label.grid(row=i+1, column=j)

    def display_categories(self):
        # Fetch categories from database
        self.cursor.execute("SELECT * FROM category")
        categories = self.cursor.fetchall()

        # Display categories in a table
        for i, category in enumerate(categories):
            for j, item in enumerate(category):
                label = tk.Label(self.categories_frame, text=item)
                label.grid(row=i+1, column=j)

    def display_total_sales(self):
        # Fetch total sales from database
        self.cursor.execute("SELECT SUM(total) FROM sales")
        total_sales = self.cursor.fetchone()[0]  # Fetch the total sales value

        # Display total sales
        label = tk.Label(self.sales_frame, text=total_sales)
        label.grid(row=1, column=0)


if __name__ == "__main__":
    root = tk.Tk()
    app = GroceryStoreApp(root)
    root.mainloop()


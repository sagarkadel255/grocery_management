
from tkinter import *
from tkinter import ttk
from category import grocerycategory
from employee import groceryemployee
from producto import groceryproduct
from supplier import grocerysupplier
from billing import grocerybill
import mysql.connector

class home:
    def __init__(self, root):
        self.root=root
        self.background = "#06283D"
        self.framebg = "#EDEDED"
        self.framebg = "06283D"
        root.title("grocery strore management")
        root.geometry("1270x670+0+0")
        root.config(bg=self.background)
        # Establish a connection to MySQL database
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sagarme",
            database="grocery_store"
        )

        # Top frame
        Label(root, text="contact us", width=10, bg="#f0687c", anchor='e').place(x=0,y=0,width=1280,height=30)
        Label(root, text="OUR GROCERY STORE", width=10, height=3, bg="#c36464", fg='#fff', font='arial 23 bold').place(x=0,y=30,width=1280,height=100)
        Label(root,text="grocery store|develop my xxxx",bg="#c36464",fg='#fff',font='arial 10 bold').pack(side=BOTTOM,fill=X)
        # Search box
        Search = StringVar()
        Entry(root, textvariable=Search, width=15, bd=2, font="arial 23").place(x=820, y=70)

        # Dashboard
        dashboard_button = Button(root, text="DASHBOARD", font='arial 15 bold', bg="blue", width=20, height=2)
        dashboard_button.place(x=0, y=130)

        products_button = Button(root, text="Products",command=self.product, font='arial 15 bold', bg='lightblue', width=20, height=2)
        products_button.place(x=0, y=195)

        supplier_button = Button(root, text="Supplier",command=self.supplier, font='arial 15 bold', bg="lightblue", width=20, height=2)
        supplier_button.place(x=0, y=260)

        employees_button = Button(root, text="Employee", command=self.employee,font='arial 15 bold', bg="lightblue", width=20, height=2)
        employees_button.place(x=0, y=325)

        categories_button = Button(root, text="Categories",command=self.category, font='arial 15 bold', bg="lightblue", width=20, height=2)
        categories_button.place(x=0, y=390)

        bills_button = Button(root, text="bills", font='arial 15 bold',command=self.bill, bg="lightblue", width=20, height=2)
        bills_button.place(x=0, y=455)

        logout_button=Button(root,text="logout",command="self.logout",font=("times new roman",15,"bold"),bg="lightblue",width=10)
        logout_button.place(x=1170,y=90)

        # Labels to display counts
        self.lbl_product=Label(root,text="Total product\n[ 0 ]",bd=5,relief=RIDGE,bg="purple",fg="black",font=("goudy old style",20, "bold"))
        self.lbl_product.place(x=280,y=150,height=150,width=300)

        self.lbl_employee=Label(root,text="Total employee\n[ 0 ]",bd=5,relief=RIDGE,bg="orange",fg="black",font=("goudy old style",20, "bold"))
        self.lbl_employee.place(x=600,y=150,height=150,width=300)

        self.lbl_category=Label(root,text="Total category \n[ 0 ]",bd=5,relief=RIDGE,bg="light green",fg="black",font=("goudy old style",20, "bold"))
        self.lbl_category.place(x=920,y=150,height=150,width=300)

        self.lbl_supplier=Label(root,text="Total supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="brown",fg="black",font=("goudy old style",20, "bold"))
        self.lbl_supplier.place(x=280,y=320,height=150,width=300)

        self. lbl_bill=Label(root,text="Total bill\n[ 0 ]",bd=5,relief=RIDGE,bg="yellow",fg="black",font=("goudy old style",20, "bold"))
        self. lbl_bill.place(x=600,y=320,height=150,width=300)
      # Update counts initially
        self.update_counts()

    def update_counts(self):
        total_products = self.get_total_data("products")
        total_employees = self.get_total_data("employees")
        total_suppliers = self.get_total_data("supplier")
        total_categories = self.get_total_data("category")
        total_bills=self.get_total_data("bills")

        self.lbl_product.config(text=f"Total product\n[ {total_products} ]")
        self.lbl_employee.config(text=f"Total employee\n[ {total_employees} ]")
        self.lbl_supplier.config(text=f"Total supplier\n[ {total_suppliers} ]")
        self.lbl_category.config(text=f"Total category \n[ {total_categories} ]")
        self.lbl_bill.config(text=f"Total bills \n[ {total_bills} ]")


    def get_total_data(self, table_name):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = cursor.fetchone()[0]
        return count

    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=groceryemployee(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=grocerysupplier(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=grocerycategory(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=groceryproduct(self.new_win)

    def bill(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=grocerybill(self.new_win)


        
    def logout(self):
        confirm = input("Are you sure you want to log out? (yes/no): ")
        if confirm.lower() == "yes":
            print("Logging out...") 
            
            print("Logged out successfully.")
        else:
            print("Logout canceled.")

        self.logout()
    

if __name__=="__main__":
    root = Tk()
    app = home(root)
    root.mainloop()

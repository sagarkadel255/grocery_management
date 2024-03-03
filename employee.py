from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
class groceryemployee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x700+0+0")
        self.root.title('EMPLOYEE')



        #variable
        
        self.var_employee_id=StringVar()
        self.var_name=StringVar()
        self.var_password=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_salary=StringVar()
        self.var_dob=StringVar()
        
        
        

        lab_title = Label(self.root, text="EMPLOYEE MANAGE", font=('times new roman', 37, 'bold'), fg='darkblue', bg='white')
        lab_title.place(x=0, y=0, width=1530, height=50)

        # Image logo
        img_logo = Image.open('images/pngegg (1).png')
        img_logo = img_logo.resize((50, 50))
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        self.logo = Label(self.root, image=self.photo_logo)
        self.logo.place(x=430, y=0, width=50, height=50)

        # Image frame
        img_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        img_frame.place(x=0, y=50, width=1540, height=110)

        #Image frames
        img1 = Image.open('images/pngegg (2).png')
        img1 = img1.resize((150, 120))
        self.photo1 = ImageTk.PhotoImage(img1)
        self.img_1 = Label(img_frame, image=self.photo1)
        self.img_1.place(x=0, y=0, width=400, height=120)

        img2 = Image.open('images/pngegg (3).png')
        img2 = img2.resize((540, 120))
        self.photo2 = ImageTk.PhotoImage(img2)
        self.img_2 = Label(img_frame, image=self.photo2)
        self.img_2.place(x=300, y=0, width=540, height=120)

        img3 = Image.open('images/pngegg.png')
        img3 = img3.resize((540, 120))
        self.photo3 = ImageTk.PhotoImage(img3)
        self.img_3 = Label(img_frame, image=self.photo3)
        self.img_3.place(x=800, y=0, width=540, height=120)
        #main frame

        main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        main_frame.place(x=0, y=160, width=1450, height=460)

        # Upper frame
        upper_frame = LabelFrame(main_frame, text='Employee Info', bd=2, bg='white', fg='red', font=('times new roman', 18))
        upper_frame.place(x=10, y=0, width=1250, height=210)

        # Employee ID
        self.lbl_employee_id = Label(upper_frame, text="Employee ID:", font=('times new roman', 14), bg='white')
        self.lbl_employee_id.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_employee_id = Entry(upper_frame,textvariable=self.var_employee_id, font=('times new roman', 14), bd=2, relief=RIDGE)
        self.entry_employee_id.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Name
        self.lbl_name = Label(upper_frame, text="Name:", font=('times new roman', 14), bg='white')
        self.lbl_name.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_name = Entry(upper_frame,textvariable=self.var_name, font=('times new roman', 14), bd=2, relief=RIDGE)
        self.entry_name.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Password
        self.lbl_password = Label(upper_frame, text="Password:", font=('times new roman', 14), bg='white')
        self.lbl_password.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_password = Entry(upper_frame,textvariable=self.var_password ,font=('times new roman', 14), bd=2, relief=RIDGE)
        self.entry_password.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Email
        self.lbl_email = Label(upper_frame, text="Email:", font=('times new roman', 14), bg='white')
        self.lbl_email.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.entry_email = Entry(upper_frame,textvariable=self.var_email ,font=('times new roman', 14), bd=2, relief=RIDGE)
        self.entry_email.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Phone
        self.lbl_phone = Label(upper_frame, text="Phone:", font=('times new roman', 14), bg='white')
        self.lbl_phone.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.entry_phone = Entry(upper_frame,textvariable=self.var_phone, font=('times new roman', 14), bd=2, relief=RIDGE)
        self.entry_phone.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        # Gender
        self.lbl_gender = Label(upper_frame, text="Gender:", font=('times new roman', 14), bg='white')
        self.lbl_gender.grid(row=0, column=2, padx=10, pady=5, sticky="w")
        self.var_gender = StringVar()
        self.cmb_gender = ttk.Combobox(upper_frame, textvariable=self.var_gender, font=('times new roman', 14), state='readonly')
        self.cmb_gender['values'] = ('Male', 'Female')
        self.cmb_gender.grid(row=0, column=3, padx=10, pady=5, sticky="w")

        # Date of Birth
        self.lbl_dob = Label(upper_frame, text="Date of Birth:", font=('times new roman', 14), bg='white')
        self.lbl_dob.grid(row=3, column=2, padx=10, pady=5, sticky="w")
        self.entry_dob = Entry(upper_frame,textvariable=self.var_dob ,font=('times new roman', 14), bd=2, relief=RIDGE)
        self.entry_dob.grid(row=3, column=3, padx=10, pady=5, sticky="w")


        
        # Salary
        self.lbl_salary = Label(upper_frame, text="Salary:", font=('times new roman', 14), bg='white')
        self.lbl_salary.grid(row=0, column=4, padx=10, pady=5, sticky="w")
        self.entry_salary = Entry(upper_frame,textvariable= self.var_salary,font=('times new roman', 14), bd=2, relief=RIDGE)
        self.entry_salary.grid(row=0, column=5, padx=10, pady=5, sticky="w")

        # Status
        self.lbl_status = Label(upper_frame, text="Status:", font=('times new roman', 14), bg='white')
        self.lbl_status.grid(row=2, column=4, padx=10, pady=5, sticky="w")
        self.var_status = StringVar()
        self.cmb_status = ttk.Combobox(upper_frame, textvariable=self.var_status, font=('times new roman', 14), state='readonly')
        self.cmb_status['values'] = ('Half', 'Single', 'Married')
        self.cmb_status.grid(row=2, column=5, padx=10, pady=5, sticky="w")

        # Province
        self.lbl_province = Label(upper_frame, text="Province:", font=('times new roman', 14), bg='white')
        self.lbl_province.grid(row=3, column=4, padx=10, pady=5, sticky="w")
        self.var_province = StringVar()
        self.cmb_province = ttk.Combobox(upper_frame, textvariable=self.var_province, font=('times new roman', 14), state='readonly')
        self.cmb_province['values'] = ('1', '2', '3', '4', '5', '6', '7')
        self.cmb_province.grid(row=3, column=5, padx=10, pady=5, sticky="w")



        # #department

        self.lbl_department = Label(upper_frame, text="Department:", font=('times new roman', 14), bg='white')
        self.lbl_department.grid(row=2, column=2, padx=10, pady=5, sticky="w")
        self.var_department = StringVar()
        self.cmb_department = ttk.Combobox(upper_frame, textvariable=self.var_department, font=('times new roman', 14), state='readonly')
        self.cmb_department['values'] = ('sales manage', 'product manage','cleaning manage','bill manage')
        self.cmb_department.grid(row=2, column=3, padx=10, pady=5, sticky="w")

        #image in frameupper
        img5 = Image.open('images/pngmage5.png')
        img5 = img5.resize((130, 220))
        self.photo5 = ImageTk.PhotoImage(img5)
        self.img_5 = Label(upper_frame, image=self.photo5)
        self.img_5.place(x=995, y=0, width=130, height=220)


        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='darkblue')
        button_frame.place(x=1110,y=0,width=240,height=220)

        btn_add=Button(button_frame,text='SAVE',command=self.add_data,font=("arial",13,'bold'),width=9,bg='blue')
        btn_add.grid(row=0,column=0,padx=1,pady=3)

        btn_update=Button(button_frame,text='UPDATE',command=self.update_data,font=("arial",13,'bold'),width=11,bg='blue')
        btn_update.grid(row=2,column=0,padx=1,pady=4)

        btn_delete=Button(button_frame,text='DELETE',command=self.delete_data,font=("arial",13,'bold'),width=13,bg='blue')
        btn_delete.grid(row=3,column=0,padx=1,pady=4)

        btn_clear=Button(button_frame,text='CLEAR',command=self.reset_data,font=("arial",13,'bold'),width=13,bg='blue')
        btn_clear.grid(row=4,column=0,padx=1,pady=4)









        # Lower frame
        lower_frame = LabelFrame(main_frame, text='Employee Detail', bd=2, relief=RIDGE, bg='white', fg='red')
        lower_frame.place(x=10, y=220, width=1250, height=220)

        search_frame=LabelFrame(lower_frame,bd=2,relief=RIDGE,text='search employee info',fg='red',bg='light pink')
        search_frame.place(x=0,y=0,width=1250,height=60)

        search_by=Label(search_frame,font=('arial 10 bold'),text='SEARCH BY:',fg='white',bg='brown')
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        #search

        self.var_com_search=StringVar()
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,state="readonly",font=("arial",12,"bold"),width=18)
        com_txt_search['value']=('select option','employee_id','phone')
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)


        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=("arial",11,"bold"))
        txt_search.grid(row=0,column=2,padx=5)

        
        btn_search=Button(search_frame,text="Search",command=self.search_data,font=('arial',11,'bold'),width=14,bg='brown')
        btn_search.grid(row=0,column=3,padx=5)

        btn_showall=Button(search_frame,text="SHOW all",command=self.fetch_data,font=('arial',11,'bold'),width=14,bg='brown')
        btn_showall.grid(row=0,column=4,padx=5)


        #__________employee table________#
        table_frame = Frame(lower_frame, bd=3, relief=RIDGE, bg='white')
        table_frame.place(x=0, y=60, width=1250, height=140)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=('employee_id','name','password','email','phone','dob','salary','gender','department','province','status'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('employee_id',text='id')
        self.employee_table.heading('name',text='NAME')
        self.employee_table.heading('password',text='PASSWORD')

        self.employee_table.heading('email',text='email')
        self.employee_table.heading('phone',text='PHONE')
        self.employee_table.heading('dob',text='DOB')

        
        self.employee_table.heading('salary',text='SAlARY')
        self.employee_table.heading('gender',text='GENDER')
        self.employee_table.heading('department',text='department')
        
        self.employee_table.heading('province',text='province')

        

        self.employee_table.heading('status',text='STATUS')
        
        

        self.employee_table['show']='headings'
        self.employee_table.column("employee_id",width=30)
        self.employee_table.column("name",width=30)
        self.employee_table.column("password",width=30)
        self.employee_table.column("email",width=30)
        self.employee_table.column("phone",width=30)
        self.employee_table.column("dob",width=30)
        self.employee_table.column("salary",width=30)
        self.employee_table.column("gender",width=30)
        self.employee_table.column("department",width=30)
        self.employee_table.column("province",width=30)
        self.employee_table.column("status",width=30)
        
        

        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        #add employee
    def add_data(self):

      if (
          self.var_employee_id.get() == "" or self.var_name.get() == ""):
      
          messagebox.showerror("Error", "All fields are required!")
      else:
          try:
              conn = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  password="sagarme",
                  database="grocery_store"
              )
              my_cursor = conn.cursor()
             
              my_cursor.execute("INSERT INTO employees (employee_id, name, password, email, phone, dob, salary, gender, department, province, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
    (
        self.var_employee_id.get(),
        self.var_name.get(),
        self.var_password.get(),
        self.var_email.get(),
        self.var_phone.get(),
        self.var_dob.get(),
        self.var_salary.get(),
        self.var_gender.get(),
        self.var_department.get(),
        self.var_province.get(),
        self.var_status.get()
    )
)

              conn.commit()
              self.fetch_data()  
              conn.close()
              messagebox.showinfo("Success", "Data added successfully!",parent=self.root)
                # Clear entry fields after successful insertion
          except Exception as es:
                messagebox.showerror("Error", f"Error adding data: {str(es)}",parent=self.root)

                #fetch data func==========


    def fetch_data(self):

        conn = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  password="sagarme",
                  database="grocery_store"
              )
        cur = conn.cursor()
        cur.execute("Select * from employees")
        data=cur.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        #get func



    def get_cursor(self,event=""):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content['values']

        self.var_employee_id.set(data[0])
        self.var_name.set(data[1])
        self.var_password.set(data[2])
        self.var_email.set(data[3])
        self.var_phone.set(data[4])
        self.var_dob.set(data[5])
        self.var_salary.set(data[6])
        self.var_gender.set(data[7])
        self.var_department.set(data[8])
        self.var_province.set(data[9])
        self.var_status.set(data[10])
        
                  
        #update func
    def update_data(self):
        if self.var_name.get() == "" or self.var_email.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                update = messagebox.askyesno('Update', "Are you sure to update?")
                if update:
                    conn = mysql.connector.connect(host='localhost', username='root', password='sagarme', database='grocery_store')
                    my_cursor = conn.cursor()
                    my_cursor.execute("UPDATE employees SET name=%s, email=%s, phone=%s, password=%s, salary=%s, department=%s, gender=%s, status=%s, dob=%s, province=%s WHERE employee_id=%s", ( 
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_password.get(),
                        self.var_salary.get(),
                        self.var_department.get(),
                        self.var_gender.get(),
                        self.var_status.get(),
                        self.var_dob.get(),
                        self.var_province.get(),
                        self.var_employee_id.get()
                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Employee successfully updated", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Error updating data: {str(es)}", parent=self.root)


                #delete func
    def delete_data(self):
        if self.var_employee_id.get()=="":
            messagebox.showerror("error","all field are required")
        else:
            try:
                delete=messagebox.askyesno("delete","are u sure ",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='sagarme',database='grocery_store')
                    my_cursor=conn.cursor()
                    sql='delete from employees where employee_id=%s'
                    value=(self.var_employee_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","successfully delete", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"due to: {str(e)}",parent=self.root)    
    #reset func
    def reset_data(self):
        self.var_employee_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_password.set("")
        self.var_salary.set("")
        self.var_department.set("select department")
        self.var_gender.set("select gender")
        self.var_status.set("select status")
        self.var_dob.set("")
        self.var_province.set("select province")          

    def search_data(self):
        if self.var_com_search.get()== "" or self.var_search.get()== "":
            messagebox.showerror("error","please select option")    

        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='sagarme',database='grocery_store')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from employees where '  + str(self.var_com_search.get())+"  LIKE '%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:

                        self.employee_table.insert("",END,values=i)
                conn.commit
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"due to: {str(es)}",parent=self.root)                    
if __name__ == "__main__":
    root = Tk()
    d = groceryemployee(root)
    root.mainloop()


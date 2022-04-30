from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime



class LibraryMangementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Mangement System")
        self.root.geometry("1550x800+0+0")


        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.contact_var=StringVar()
        self.book_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.dateDue_var=StringVar()
        self.days_var=StringVar()
        self.finalprice_var=StringVar()

        lbtitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbtitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)

        DataFrameLeft=LabelFrame(frame,text="LIBRARY STUDENT INFORMATION",bg="powder blue",fg="green",bd=15,relief=RIDGE,font=("times new roman",15,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblPRN_NO=Label(DataFrameLeft,bg="powder blue",text="PRN No:",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblPRN_NO.grid(row=0,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.prn_var,width=24)
        txtPRN_NO.grid(row=0,column=1)

        lblStudentID=Label(DataFrameLeft,font=("arial",14,"bold"),text="Student ID:",bg="powder blue",padx=2,pady=6)
        lblStudentID.grid(row=1,column=0,sticky=W)
        lblStudentID=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.id_var,width=24)
        lblStudentID.grid(row=1,column=1)


        lblFirstName=Label(DataFrameLeft,font=("arial",14,"bold"),text="First Name:",bg="powder blue",padx=2,pady=6)
        lblFirstName.grid(row=2,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.firstname_var,width=24)
        txtFirstName.grid(row=2,column=1)

        lblLastName=Label(DataFrameLeft,font=("arial",14,"bold"),text="Last Name:",bg="powder blue",padx=2,pady=6)
        lblLastName.grid(row=3,column=0,sticky=W)
        lblLastName=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.lastname_var,width=24)
        lblLastName.grid(row=3,column=1)

        lblMobile=Label(DataFrameLeft,font=("arial",14,"bold"),text="Contact No:",bg="powder blue",padx=2,pady=6)
        lblMobile.grid(row=4,column=0,sticky=W)
        lblMobile=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.contact_var,width=24)
        lblMobile.grid(row=4,column=1)

        lblBookName=Label(DataFrameLeft,font=("arial",14,"bold"),text="Book No:",bg="powder blue",padx=2,pady=6)
        lblBookName.grid(row=0,column=2,sticky=W)
        lblBookName=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.book_var,width=24)
        lblBookName.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,font=("arial",14,"bold"),text="Book Title:",bg="powder blue",padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        lblBookTitle=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.booktitle_var,width=24)
        lblBookTitle.grid(row=1,column=3)

        lblAuthor=Label(DataFrameLeft,font=("arial",14,"bold"),text="Author Name:",bg="powder blue",padx=2,pady=6)
        lblAuthor.grid(row=2,column=2,sticky=W)
        lblAuthor=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.author_var,width=24)
        lblAuthor.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,font=("arial",14,"bold"),text="Date Borrowed:",bg="powder blue",padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        lblDateBorrowed=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateborrowed_var,width=24)
        lblDateBorrowed.grid(row=3,column=3)

        lblDateDue=Label(DataFrameLeft,font=("arial",14,"bold"),text="Date Due:",bg="powder blue",padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        lblDateDue=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateDue_var,width=24)
        lblDateDue.grid(row=4,column=3)

        lblDaysOnBook=Label(DataFrameLeft,font=("arial",14,"bold"),text="Days On Book:",bg="powder blue",padx=2,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        lblDaysOnBook=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.days_var,width=24)
        lblDaysOnBook.grid(row=5,column=3)

        lblPrice=Label(DataFrameLeft,font=("arial",14,"bold"),text="Actual Price:",bg="powder blue",padx=2,pady=6)
        lblPrice.grid(row=6,column=2,sticky=W)
        lblPrice=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.finalprice_var,width=24)
        lblPrice.grid(row=6,column=3)




        





        DataFrameRight=LabelFrame(frame,text="BOOK DETAILS",bg="powder blue",fg="green",bd=15,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=950,y=5,width=530,height=350)

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=28,height=13,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=['Mathematics operations','Python Program','Java Theory','SQL Mind','Python3','Html Show',"CSS Knwoledge","Bootstrap Theory","Database","Freshers iT"]

        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection))
            x=value
            if (x=="Mathematics operations"):
                self.book_var.set("121")
                self.booktitle_var.set("Python Program")
                self.author_var.set("Dr James Dsoza")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.dateDue_var.set(d3)
                self.days_var.set(10)
                self.finalprice_var.set("Rs.200")



        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=24,height=13)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1530,height=70)

        btnAddData=Button(Framebutton,command=self.add_data,text="Add Book",font=("arial",14,"bold"),width=19,bg="Red",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,command=self.showData,text="Show Book",font=("arial",14,"bold"),width=19,bg="Red",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.update,text="Update Book",font=("arial",14,"bold"),width=19,bg="Red",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,text="Delete Book",font=("arial",14,"bold"),width=19,bg="Red",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,command=self.reset,text="Reset Book",font=("arial",14,"bold"),width=19,bg="Red",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,command=self.iExit,text="Exit",font=("arial",14,"bold"),width=20,bg="Red",fg="white")
        btnAddData.grid(row=0,column=5)





        Framedetailes=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framedetailes.place(x=0,y=600,width=1530,height=190)

        Table_frame=Frame(Framedetailes,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1450,height=185)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,column=("PRN No","Student Id","First Name","Last Name","Contact No","Book No","Book Title","Author Name","DateBorrowed","DateDue","Days","FinalPrice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)


        self.library_table.heading("PRN No",text="PRN No")
        self.library_table.heading("Student Id",text="Student Id")
        self.library_table.heading("First Name",text="First Name")
        self.library_table.heading("Last Name",text="Last Name")
        self.library_table.heading("Contact No",text="Contact No")
        self.library_table.heading("Book No",text="Book No")
        self.library_table.heading("Book Title",text="Book Title")
        self.library_table.heading("Author Name",text="Author Name")
        self.library_table.heading("DateBorrowed",text="DateBorrowed")
        self.library_table.heading("DateDue",text="DateDue")
        self.library_table.heading("Days",text="Days")
        self.library_table.heading("FinalPrice",text="FinalPrice")
    

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("PRN No",width=110)
        self.library_table.column("Student Id",width=110)
        self.library_table.column("First Name",width=110)
        self.library_table.column("Last Name",width=110)
        self.library_table.column("Contact No",width=110)
        self.library_table.column("Book No",width=110)
        self.library_table.column("Book Title",width=110)
        self.library_table.column("Author Name",width=110)
        self.library_table.column("DateBorrowed",width=110)
        self.library_table.column("DateDue",width=110)
        self.library_table.column("Days",width=110)
        self.library_table.column("FinalPrice",width=110)

        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Aniket@123",database="mydata1")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.prn_var.get(),
                                                                                            self.id_var.get(),
                                                                                            self.firstname_var.get(),
                                                                                            self.lastname_var.get(),
                                                                                            self.contact_var.get(),
                                                                                            self.book_var.get(),
                                                                                            self.booktitle_var.get(),
                                                                                            self.author_var.get(),
                                                                                            self.dateborrowed_var.get(),
                                                                                            self.dateDue_var.get(),
                                                                                            self.days_var.get(),
                                                                                            self.finalprice_var.get()

                                                                                         ))
        conn.commit()
        self.fatch_data()
        conn.close()

        messagebox.showinfo("Sucessfull!!","Great,Student Has been Inserted sucessfully")

    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Aniket@123",database="mydata1")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set PRN No=%s,Student Id=%s,Last Name=%s,Contact No=%s,Book No=%s,Book Title=%s,Author Name=%s,Dateborrowed=%s,DateDue=%s,Days=%s,FinalPrice=%s where First Name=%s",(
                                                                                                                       self.prn_var.get(),
                                                                                                                       self.id_var.get(),
                                                                                                                       self.lastname_var.get(),
                                                                                                                       self.contact_var.get(),
                                                                                                                       self.book_var.get(),
                                                                                                                       self.booktitle_var.get(),
                                                                                                                       self.author_var.get(),
                                                                                                                       self.dateborrowed_var.get(),
                                                                                                                       self.dateDue_var.get(),
                                                                                                                       self.days_var.get(),
                                                                                                                       self.finalprice_var.get(),
                                                                                                                       self.firstname_var.get(),
                                                                                                                       
                                                                                                                    ))
        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("success","Student Has Been Updated!")                                                                                                           

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Aniket@123",database="mydata1")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
                conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.prn_var.set(row[0]),
        self.id_var.set(row[1]),
        self.firstname_var.set(row[2]),
        self.lastname_var.set(row[3]),
        self.contact_var.set(row[4]),
        self.book_var.set(row[5]),
        self.booktitle_var.set(row[6]),
        self.author_var.set(row[7]),
        self.dateborrowed_var.set(row[8]),
        self.dateDue_var.set(row[9]),
        self.days_var.set(row[10]),
        self.finalprice_var.set(row[11])

    def showData(self):
        self.txtBox.insert(END,"PRN No\t\t"+self.prn_var.get()+"\n")
        self.txtBox.insert(END,"Student ID\t\t"+self.id_var.get()+"\n")
        self.txtBox.insert(END,"First Name\t\t"+self.firstname_var.get()+"\n")
        self.txtBox.insert(END,"Last Name\t\t"+self.lastname_var.get()+"\n")
        self.txtBox.insert(END,"Contact No\t\t"+self.contact_var.get()+"\n")
        self.txtBox.insert(END,"Book No\t\t"+self.book_var.get()+"\n")
        self.txtBox.insert(END,"Book Title\t\t"+self.booktitle_var.get()+"\n")
        self.txtBox.insert(END,"Author Name\t\t"+self.author_var.get()+"\n")
        self.txtBox.insert(END,"Date Borrowed\t\t"+self.dateborrowed_var.get()+"\n")
        self.txtBox.insert(END,"Date Due\t\t"+self.dateDue_var.get()+"\n")
        self.txtBox.insert(END,"Days On Book\t\t"+self.days_var.get()+"\n")
        self.txtBox.insert(END,"Actual Price\t\t"+self.finalprice_var.get()+"\n")

    def reset(self):
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.contact_var.set(""),
        self.book_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.dateDue_var.set(""),
        self.days_var.set(""),
        self.finalprice_var.set(""),
        self.txtBox.delete("1.0",END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Mangement System","Do You Want Exit?")
        if iExit>0:
            self.root.destroy()
            return                        

    
        



        



if __name__== "__main__" :
    root=Tk()
    obj=LibraryMangementSystem(root)
    root.mainloop()       
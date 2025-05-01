from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import mysql.connector

import DataAccess

def AuthenticateUser():
    uname=txtUserName.get()
    pwd=txtPassword.get()
    
    print(uname)
    count=DataAccess.AuthenticateUser(uname,pwd)
    
    if count[0][0]==1:
        root.destroy()
        import Admin_Dashboard
    else:
        print("Invalid User/Password")


#Window settings
root = Tk()

#getting screen width and height of display
root.geometry("%dx%d+%d+%d" % (350,270,500,175))
root.title("Admin Login...")
root.config(bg="light blue")


txtUserName=StringVar()
txtPassword=StringVar()

label_1=Label(root, text="USER NAME:",fg="Black", bg="light blue", font=("Calibri 13 bold"))
label_1.place(x=30, y=50)
txtUserName=Entry(root, textvar=txtUserName, width=25)
txtUserName.place(x=140, y=53)

label_2=Label(root, text="PASSWORD:", fg="Black", bg="light blue", font=("Calibri 13 bold"))
label_2.place(x=30, y=80)
txtPassword=Entry(root, show="*", width=25)
txtPassword.place(x=140, y=83)

Button(root, text="Submit", width=12, bg='blue', fg='white',command=AuthenticateUser).place(x=80, y=200)
Button(root, text="Close", width=12, bg='blue', fg='white',command=root.destroy).place(x=180, y=200)
#Button(root, text="Not a Member yet", width=15, bg='blue', fg='white').place(x=300, y=200)
root.mainloop()

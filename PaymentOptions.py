from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import mysql.connector

import DataAccess

def btnAsPayNow_click():
    messagebox.showinfo('Payment Confirmation Message', "Thank you for your payment!\n\nWe have received INR"+txtAmount.get()+" from you. The recipt of the bill wil be sent to you via email, also one SMS will be sent to your mobile no.\n\nOur reprentative will contact you soon. Thanks!")
    root.destroy()
    import VisitorsWindow

root = Tk()
root.geometry("%dx%d+%d+%d" % (350,350,500,200))
root.title("Payment Options...")
root.config(bg="silver")

var1 =IntVar()
var2 =IntVar()
var3 =IntVar()


lbl_heading1=Label(root, text="Enter a token amount:",bg="silver",font=("TimesNewRoman 12 bold"))
lbl_heading1.grid(row=0, sticky=W, padx=30,pady=8)

txtAmount=Entry(root, width=20)
txtAmount.grid(row=1, sticky=W, padx=30,pady=8)

lbl_heading2=Label(root, text="Payment Options:",bg="silver",font=("TimesNewRoman 12 bold"))
lbl_heading2.grid(row=2, sticky=W, padx=30,pady=8)

c1=Checkbutton(root, text='UPI',font=("Calibri 15"),bg="silver",variable=var1, onvalue=1, offvalue=0).grid(row=3, sticky=W, padx=55,pady=8)

c2=Checkbutton(root, text='Credit/Debit/ATM Card',font=("Calibri 15"),bg="silver",variable=var2, onvalue=1, offvalue=0).grid(row=4, sticky=W,padx=55,pady=8)

c3=Checkbutton(root, text='Net Banking',font=("Calibri 15"),bg="silver",variable=var3, onvalue=1, offvalue=0).grid(row=5, sticky=W, padx=55, pady=8)

Button(root, text="PAY NOW", width=12, bg='blue', fg='white', font=("calibri 13"),command=btnAsPayNow_click).place(x=50, y=280)
root.mainloop()

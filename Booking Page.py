from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import mysql.connector

import DataAccess

def AuthenticateUser():
    DOJ=txtDateOfJourney.get()
    email=txtEmailID.get()
    add=txtAddress.get()
    
    
root = Tk()

root.geometry("%dx%d+%d+%d" % (400,270,200,175))
root.title("Booking Details")
root.config(bg="light blue")

txtDateOfJourney=StringVar()
txtEmailID=StringVar()
txtAddress=StringVar()


label_1=Label(root, text="DateOfJourney:",fg="Black", bg="light blue", font=("Calibri 13 bold"))
label_1.place(x=30, y=50)
txtDateOfJourney=Entry(root, textvar=txtDateOfJourney, width=25)
txtDateOfJourney.place(x=140, y=53)

label_2=Label(root, text="EmailID:", fg="Black", bg="light blue", font=("Calibri 13 bold"))
label_2.place(x=30, y=80)
txtEmailID=Entry(root, textvar=txtEmailID, width=25)
txtEmailID.place(x=140, y=83)

label_3=Label(root, text="Address:", fg="Black", bg="light blue", font=("Calibri 13 bold"))
label_3.place(x=30, y=80)
txtAddress=Entry(root, textvar=txtAddress, width=25)
txtAddress.place(x=140, y=83)
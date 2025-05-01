from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import mysql.connector

root = Tk()
#getting screen width and height of display
Wwidth= root.winfo_screenwidth() 
Wheight= root.winfo_screenheight()
#setting tkinter window size
root.geometry("%dx%d" % (Wwidth, Wheight))
root.title("Admin Console")
root.config(bg="white")

lbl_heading=Label(root, text="Hotels in Delhi",fg="black",bg="light green",font=("Times New Roman",25),relief="ridge",pady=10,border=10).pack(fill='x')




root.mainloop()
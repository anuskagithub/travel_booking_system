from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import mysql.connector

def btnAsAdmin_clik():
    root.destroy()
    import AdminLogin
    
def btnAsVisitor_click():
    root.destroy()
    import VisitorsWindow
    
#Window settings
root = Tk()

#getting screen width and height of display
Wwidth= root.winfo_screenwidth() 
Wheight= root.winfo_screenheight()
#setting tkinter window size
root.geometry("%dx%d+%d+%d" % (Wwidth, Wheight,0,0))
root.title("Daily Travel Booking System")
root.config(bg="white")

lbl_Heading=Label(root, text="WELCOME TO DAILY TRAVEL BOOKING SYSTEM",fg="black",bg="light green",font=("Calibri 25 bold"),relief="ridge",pady=10,border=10).pack(fill='x')
canvas = Canvas(root, width = 1400, height = 280)
canvas.pack()

img = ImageTk.PhotoImage(Image.open("D:/Anuska/Travel2021/Daily_Travel_Booking/Pictures/HomePagebg.jpg"))
canvas.create_image(0, 0, anchor=NW, image=img)

#End Window Settings

#lbl_Heading1=Label(root, text="WELCOME TO DAILY TR11AVEL BOOKING SYSTEM", bg="light green",fg="Black",font=("ar 25 bold"))
#lbl_Heading1.place(x=275, y=40)

Home_Frame=Frame(root,bd=3, relief=RIDGE, bg="cadet blue")
Home_Frame.place(x=0, y=350, width=1365, height=80)    

lbl1=Label(Home_Frame, text="Our software is centered on making travel simple and has been designed to let you look for cheap packages and to complete your bookings in just a few clicks. We are known for\nproviding the best travel deals to travelers within India. Here, you can book flight tickets, hotels, and holiday packages at a cost-effective price.So,why go anywhere else?\nVisit us for a memorable travel experience your budget. EXPERIENCE THE INCREDIBLE INDIA WITH US!", bg="cadet blue",fg="black",font=("Arial 13 italic"))
lbl1.grid(row=0, column=0, padx=0,pady=0, sticky="w")


Home_Frame1=Frame(root,bg="white")
Home_Frame1.place(x=0, y=500, width=2000, height=130)  

btnAsAdmin=Button(Home_Frame1, command=btnAsAdmin_clik, text="LOGIN AS ADMIN",font=("Arial 12 bold"),bg="light Blue" ,width=35,height=5, pady=5).grid(row=1, column=6, padx=200, pady=10)
btnAsVisitor=Button(Home_Frame1, command=btnAsVisitor_click, text="LOGIN AS VISITOR",font=("Arial 12 bold"),bg="light Blue", width=35,height=5, pady=5).grid(row=1, column=12, padx=10, pady=10)
   
root.mainloop()
from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import mysql.connector

def btnAsFamilyTourPackage_clik():
    root.destroy()
    import FamilyTourPackage

def btnAsGroupTourPackage_clik():
    root.destroy()
    import GroupTourPackage

def btnAsSoloTourPackage_clik():
    root.destroy()
    import SoloTourPackage

def btnAsHotelBooking_clik():
    root.destroy()
    import HotelBooking_Search
    
def btnAsFlightBooking_clik():
    root.destroy()
    import Flight_Booking_Search

root = Tk()
#getting screen width and height of display
Wwidth= root.winfo_screenwidth() 
Wheight= root.winfo_screenheight()
#setting tkinter window size
root.geometry("%dx%d" % (Wwidth, Wheight))
root.title("Visitors' Page")
root.config(bg="white")

lbl_heading=Label(root, text="VISITORS'  PAGE",fg="black",bg="light green",font=("Times New Roman",25),relief="ridge",pady=10,border=10).pack(fill='x')

canvas = Canvas(root, width = 1400, height = 700)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("D:/Anuska/Travel2021/Daily_Travel_Booking/Pictures/visitors2.jpg"))
canvas.create_image(0, 0, anchor=NW, image=img)

b1=Button(root, fg="Black",bg="silver", text="FAMILY TOUR PACKAGE",font=("Times New Roman",11,"bold"),width=25,height=5,relief="raised", borderwidth=3,command=btnAsFamilyTourPackage_clik)
b1.place(x=80,y=410)

b2=Button(root, fg="Black",bg="cyan", text="GROUP TOUR PACKAGE",font=("Times New Roman",11,"bold"),width=25,height=5,relief="raised", borderwidth=3,command=btnAsGroupTourPackage_clik)
b2.place(x=595,y=410)

b3=Button(root, fg="Black",bg="gold", text="SOLO TOUR PACKAGE",font=("Times New Roman",11,"bold"),width=25,height=5,relief="raised", borderwidth=3,command=btnAsSoloTourPackage_clik)
b3.place(x=1040,y=410)

b5=Button(root, fg="Black",bg="orange", text="HOTEL BOOKING",font=("Times New Roman",11,"bold"),width=25,height=5,relief="raised", borderwidth=3,command=btnAsHotelBooking_clik)
b5.place(x=350,y=550)

b4=Button(root, fg="Black",bg="violet", text="FLIGHT BOOKING",font=("Times New Roman",11,"bold"),width=25,height=5,relief="raised", borderwidth=3,command=btnAsFlightBooking_clik)
b4.place(x=770,y=550)

lbl1=Label(root, text="Bsed on your booking the site admin will approve for the confirmation                                                                                                                                                                                                                             ", fg="black",font=("Arial 12 italic"))
lbl1.place(x=1, y=660)

root.mainloop()
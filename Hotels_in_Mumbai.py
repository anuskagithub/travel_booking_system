from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import mysql.connector
import random
import DataAccess

def btnAsBookMumbaiHotel1_clik():
    DataAccess.put_GlobalVal("Sofitel Mumbai BKC","Mumbai")
    root.destroy()
    import Booking_Hotel
   
def btnAsBookDelhiHotel2_clik():
    DataAccess.put_GlobalVal("ITC Maratha, Mumbai - a Luxury Collection Hotel","Mumbai")
    root.destroy()
    import Booking_Hotel

def btnAsBookDelhiHotel3_clik():
    DataAccess.put_GlobalVal("Trident, Nariman Point","Mumbai")
    root.destroy()
    import Booking_Hotel    

root = Tk()
#getting screen width and height of display
Wwidth= root.winfo_screenwidth() 
Wheight= root.winfo_screenheight()
#setting tkinter window size
root.geometry("%dx%d" % (Wwidth, Wheight))
root.title("Admin Console")
root.config(bg="white")

lbl_heading=Label(root, text="Hotels in Mumbai",fg="black",bg="light blue",font=("Times New Roman",25),relief="ridge",pady=10,border=10).pack(fill='x')

canvas = Canvas(root, width = 3000, height = 3000)
canvas.pack()

lstPack= []
lstPack.append("D:\Anuska\Travel2021\Daily_Travel_Booking\Pictures\MUMBAI_HotelBooking.jpg")

# Create a photoimage object of the image in the path
ycord=5
for iPack in lstPack:
    image1 = Image.open(iPack)
    test = ImageTk.PhotoImage(image1)
    
    label1 = Label(image=test)
    label1.image = test
    
    # Position image
    label1.place(x=10, y=85)
    ycord=ycord+150
    
Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=2,width=15, bg='light blue', fg='black',command=btnAsBookMumbaiHotel1_clik).place(x=1000, y=200)
Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=2,width=15, bg='light blue', fg='black',command=btnAsBookDelhiHotel2_clik).place(x=1000, y=380)
Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=2,width=15, bg='light blue', fg='black',command=btnAsBookDelhiHotel3_clik).place(x=1000, y=530)
root.mainloop()



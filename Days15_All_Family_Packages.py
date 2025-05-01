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
root.title("Family Packages")
root.config(bg="white")



lbl_heading=Label(root, text="15 Days Family Packages",fg="black",bg="light green",font=("Times New Roman",25),relief="ridge",pady=10,border=10).pack(fill='x')


def btnAsDays15_Rajasthan_clik():
    root.destroy()
    import Days15_Rajasthan_Package

def btnAsDays15_Kashmir_clik():
    root.destroy()
    import Days15_Kashmir_Package

def btnAsDays15_Ladakh_clik():
    root.destroy()
    import Days15_Ladakh_Package
    
def btnAsDAys15_SouthIndia_clik():
    root.destroy()
    import Days15_SouthIndia_Package


Home_Frame=Frame(root,borderwidth=6 ,bg="red")
Home_Frame.pack()  

canvas = Canvas(root, width = 3000, height = 3000)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("D:/Anuska/Travel2021/Daily_Travel_Booking/Pictures/FamilyTour.jpg"))
canvas.create_image(0, 0, anchor=NW, image=img)

b1=Button(root, fg="Black",bg="silver", text="RAJASTHAN\n\nExperience the heritage of Rajasthan",font=("Times New Roman",11,"bold"),width=30,height=5,relief="raised", borderwidth=3,command=btnAsDays15_Rajasthan_clik)
b1.place(x=30,y=450)

b2=Button(root, fg="Black",bg="cyan", text="KASHMIR\n\nKashmir-Paradise on the Earth",font=("Times New Roman",11,"bold"),width=30,height=5,relief="raised", borderwidth=3,command=btnAsDays15_Kashmir_clik)
b2.place(x=370,y=450)

b3=Button(root, fg="Black",bg="gold", text="LADAKH\n\nEscape the city life with these \nincredible short mountain getaways",font=("Times New Roman",11,"bold"),width=30,height=5,relief="raised", borderwidth=3,command=btnAsDays15_Ladakh_clik)
b3.place(x=710,y=450)

b4=Button(root, fg="Black",bg="violet", text="SOUTH INDIA\n\nGet to experience the peninsular \n region of the Indian subcontinent",font=("Times New Roman",11,"bold"),width=30,height=5,relief="raised", borderwidth=3, command=btnAsDAys15_SouthIndia_clik)
b4.place(x=1050,y=450)


lbl1=Label(root, text="Our software is centered on making travel simple and has been designed to let you look for cheap packages and to complete your bookings in just a few clicks. We are known for providing the \n best travel deals to travelers.We can satisfy all your travel needs. Here, you can book flight tickets, hotels, and holiday packages at a cost-effective price.So,why go anywhere else? \n Visit us for a memorable travel experience in your budget.", fg="black",font=("Arial 12 italic"))
lbl1.place(x=5, y=600)

root.mainloop()




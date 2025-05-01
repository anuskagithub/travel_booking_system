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
root.title("Solo Packages")
root.config(bg="white")



lbl_heading=Label(root, text="3 Days Solo Packages",fg="black",bg="light green",font=("Times New Roman",25),relief="ridge",pady=10,border=10).pack(fill='x')


def btnAsDays3_Nagtibba_Solo_Package_clik():
    root.destroy()
    import Days3_Nagtibba_Solo_Package

def btnAsDays3_Dayara_Solo_Package_clik():
    root.destroy()
    import Days3_Dayara_Solo_Package

def btnAsDays3_Bhrigu_Solo_Package_clik():
    root.destroy()
    import Days3_Bhrigu_Solo_Package   

    
Home_Frame=Frame(root,borderwidth=6 ,bg="red")
Home_Frame.pack()  

canvas = Canvas(root, width = 3000, height = 3000)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("D:/Anuska/Travel2021/Daily_Travel_Booking/Pictures/solo.jpg"))
canvas.create_image(0, 0, anchor=NW, image=img)

b1=Button(root, fg="Black",bg="silver", text="NAGTIBBA TREK\n\nThe abode of 'Nag Devta' or God of Snakes\nin Uttarakhand...",font=("Times New Roman",11,"bold"),width=30,height=5,relief="raised", borderwidth=3,command=btnAsDays3_Nagtibba_Solo_Package_clik)
b1.place(x=175,y=450)

b2=Button(root, fg="Black",bg="cyan", text="DAYARA BUGYAL TREK\n\nThe most enchanting and breathtaking trek\nin Uttarakhand...",font=("Times New Roman",11,"bold"),width=30,height=5,relief="raised", borderwidth=3,command=btnAsDays3_Dayara_Solo_Package_clik)
b2.place(x=535,y=450)

b3=Button(root, fg="Black",bg="gold", text="BHRIGU LAKE TREK\n\nA lake steeped in mythology\nin Himachal Pradesh...",font=("Times New Roman",11,"bold"),width=30,height=5,relief="raised", borderwidth=3,command=btnAsDays3_Bhrigu_Solo_Package_clik)
b3.place(x=875,y=450)


lbl1=Label(root, text="Our software is centered on making travel simple and has been designed to let you look for cheap packages and to complete your bookings in just a few clicks. We are known for providing the \n best travel deals to travelers.We can satisfy all your travel needs. Here, you can book flight tickets, hotels, and holiday packages at a cost-effective price.So,why go anywhere else? \n Visit us for a memorable travel experience in your budget.", fg="black",font=("Arial 12 italic"))
lbl1.place(x=5, y=600)

root.mainloop()



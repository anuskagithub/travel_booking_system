from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
#import mysqconnector

import DataAccess

def btnAsBookNow_clik():
    root.destroy()
    import FamilyPackage_BookingDetails
    
def btnAsShowGallery_clik():
    root.destroy()
    import Gallery    

def BookNow(pid):
    print(pid)
    
root = Tk()
#getting screen width and height of display
Wwidth= root.winfo_screenwidth() 
Wheight= root.winfo_screenheight()
#setting tkinter window size
root.geometry("%dx%d" % (Wwidth, Wheight))
root.title("Gallery")
root.config(bg="silver")

GalleryName=DataAccess.get_GlobalVal()[0][0]
GalleryPath=DataAccess.Get_GalleryPath(GalleryName)

GalleryName="Gallery of  "+GalleryName
lbl_heading=Label(root, text=GalleryName,fg="black",bg="light green",font=("Times New Roman",25),relief="ridge",pady=10,border=10).pack(fill='x')

canvas = Canvas(root, width = 3000, height = 3000)
canvas.pack()

if GalleryPath!='':
    img = ImageTk.PhotoImage(Image.open(GalleryPath))
else:
    img = ImageTk.PhotoImage(Image.open("D:/Anuska/Travel2021/Daily_Travel_Booking/Pictures/UnderConstruction.jpg"))  
    
canvas.create_image(0, 0, anchor=NW, image=img)

root.mainloop()
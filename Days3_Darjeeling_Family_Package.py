from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import mysql.connector

import DataAccess

def btnAsShowGallery_clik():
    DataAccess.put_GlobalVal("Darjeeling")
    root.destroy()
    import Gallery

def btnDarjeeling1_click():
    DataAccess.put_GlobalVal("Delightful Darjeeling","Family")
    root.destroy()
    import Booking_TourPackage
   
def btnDarjeeling2_click():
    DataAccess.put_GlobalVal("Darjeeling in 3 days","Family")
    root.destroy()
    import Booking_TourPackage

def btnDarjeeling3_click():
    DataAccess.put_GlobalVal("Darjeeling-The Queens of Hills","Family")
    root.destroy()
    import Booking_TourPackage

   
root = Tk()
#getting screen width and height of display
Wwidth= root.winfo_screenwidth() 
Wheight= root.winfo_screenheight()
#setting tkinter window size
root.geometry("%dx%d" % (Wwidth, Wheight))
root.title("Admin Console")
root.config(bg="silver")



lbl_heading=Label(root, text="Darjeeling 3 Days Family Package",fg="black",bg="light green",font=("Times New Roman",25),relief="ridge",pady=10,border=10).pack(fill='x')

canvas = Canvas(root, width = 1360, height = 650)
canvas.pack()

img = ImageTk.PhotoImage(Image.open("D:/Anuska/Travel2021/Daily_Travel_Booking/Pictures/Darjeeling_3Days_Package2.jpg"))
canvas.create_image(0, 0, anchor=NW, image=img)



lstPack= []
lstPack.append("D:\Anuska\Travel2021\Daily_Travel_Booking\Pictures\Darjeeling_3Days_Package.png")
#lstPack.append("Pictures/Darjeeling_3_days.png")
#lstPack.append("Pictures/FP_Rajasthan_15_Days.png")

# Create a photoimage object of the image in the path
ycord=5
p="p100"
for iPack in lstPack:
    image1 = Image.open(iPack)
    test = ImageTk.PhotoImage(image1)
    
    label1 = Label(image=test)
    label1.image = test
    
    # Position image
    label1.place(x=220, y=175)
    ycord=ycord+150
    
    Button(root, text="Gallery",font=("Times New Roman",13,"bold"), height=2,width=10, bg='light green', fg='black',command=btnAsShowGallery_clik).place(x=935, y=200)
    Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=2,width=10, bg='light green', fg='black',command=btnDarjeeling1_click).place(x=935, y=335)
    Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=2,width=10, bg='light green', fg='black',command=btnDarjeeling2_click).place(x=935, y=448)
    Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=2,width=10, bg='light green', fg='black',command=btnDarjeeling3_click).place(x=935, y=555)
    
root.mainloop()



##DAYS15_ANDAMAN & NICOBAR ISLANDS_GROUP_PACKAGE(HRISHEETA)##

from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
#import mysqconnector

import DataAccess

def btnANDAMAN1_click():
    DataAccess.put_GlobalVal("Majestic Andaman Tour")
    root.destroy()
    import Booking_TourPackage
   
def btnANDAMAN2_click():
    DataAccess.put_GlobalVal("Amazing Andaman - Deluxe")
    root.destroy()
    import Booking_TourPackage

def btnAsShowGallery_clik():
    DataAccess.put_GlobalVal("Andaman")
    root.destroy()
    import Gallery    


root = Tk()
#getting screen width and height of display
Wwidth= root.winfo_screenwidth() 
Wheight= root.winfo_screenheight()
#setting tkinter window size
root.geometry("%dx%d" % (Wwidth, Wheight))
root.title("Admin Console")
root.config(bg="silver")


lbl_heading=Label(root, text="Andaman & Nicobar Islands - 15 Days Group Package",fg="black",bg="light green",font=("Times New Roman",25),relief="ridge",pady=10,border=10).pack(fill='x')

canvas = Canvas(root, width = 3000, height = 3000)
canvas.pack()

img = ImageTk.PhotoImage(Image.open("D:\Anuska\Travel2021\Daily_Travel_Booking\Pictures\Andamanbg.webp"))
canvas.create_image(0, 0, anchor=NW, image=img)

lstPack= []
lstPack.append("D:\Anuska\Travel2021\Daily_Travel_Booking\Pictures\Andaman_15Days_GroupPackage.jpeg")
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
    label1.place(x=290, y=100)
    ycord=ycord+150
    
    Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=2,width=10, bg='light green', fg='black',command=btnANDAMAN1_click).place(x=900, y=230)
    Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=2,width=10, bg='light green', fg='black',command=btnANDAMAN2_click).place(x=900, y=448)
    Button(root, text="Gallery",font=("Times New Roman",13,"bold"), height=2,width=10, bg='light green', fg='black',command=btnAsShowGallery_clik).place(x=900, y=120)

root.mainloop()


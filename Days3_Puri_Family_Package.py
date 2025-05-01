from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import mysql.connector

import DataAccess

def btnPuri1_click():
    DataAccess.put_GlobalVal("Best of Puri","Family")
    root.destroy()
    import Booking_TourPackage
   
def btnPuri2_click():
    DataAccess.put_GlobalVal("Bhubaneswar & Puri in 3 Days","Family")
    root.destroy()
    import Booking_TourPackage

def btnPuri3_click():
    DataAccess.put_GlobalVal("Puri & Konark in 3 Days","Family")
    root.destroy()
    import Booking_TourPackage

def btnAsShowGallery_clik():
    DataAccess.put_GlobalVal("Puri")
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


lbl_heading=Label(root, text="PURI  - 3 Days Family Package",fg="black",bg="light green",font=("Times New Roman",25),relief="ridge",pady=10,border=10).pack(fill='x')

canvas = Canvas(root, width = 1360, height = 650)
canvas.pack()

img = ImageTk.PhotoImage(Image.open("D:\Anuska\Travel2021\Daily_Travel_Booking\Pictures\puribg.jpg"))
canvas.create_image(0, 0, anchor=NW, image=img)


lstPack= []
lstPack.append("D:\Anuska\Travel2021\Daily_Travel_Booking\Pictures\Puri_3DAys_Package.png")
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
    label1.place(x=230, y=170)
    ycord=ycord+150
    
    Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=2,width=10, bg='light green', fg='black',command=btnPuri1_click).place(x=950, y=335)
    Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=2,width=10, bg='light green', fg='black',command=btnPuri2_click).place(x=950, y=448)
    Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=2,width=10, bg='light green', fg='black',command=btnPuri3_click).place(x=950, y=555)
    Button(root, text="Gallery",font=("Times New Roman",13,"bold"), height=2,width=10, bg='light green', fg='black',command=btnAsShowGallery_clik).place(x=950, y=200)
root.mainloop()






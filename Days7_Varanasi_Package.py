from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import mysql.connector

import DataAccess


def btnVaranasi1_click():
    DataAccess.put_GlobalVal("Temples of Varanasi with a tour to Gaya","Family")
    root.destroy()
    import Booking_TourPackage
   
def btnVaranasi2_click():
    DataAccess.put_GlobalVal("New Delhi, Haridwar, Varanasi & Bodh Gaya-Kasi Yatra","Family")
    root.destroy()
    import Booking_TourPackage

def btnVaranasi3_click():
    DataAccess.put_GlobalVal("Enchanting Varanasi, Allahabad, Ayodhya And Bodhgaya Yatra","Family")
    root.destroy()
    import Booking_TourPackage

def btnAsShowGallery_clik():
    DataAccess.put_GlobalVal("Varanasi")
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



lbl_heading=Label(root, text="Varanasi - 7 Family Days Package",fg="black",bg="light green",font=("Times New Roman",25),relief="ridge",pady=10,border=10).pack(fill='x')

canvas = Canvas(root, width = 3000, height = 3000)
canvas.pack()

img = ImageTk.PhotoImage(Image.open("D:\\Anuska\\Travel2021\\Daily_Travel_Booking\\Pictures\\varanasibg.jpg"))
canvas.create_image(0, 0, anchor=NW, image=img)

lstPack= []
lstPack.append("D:\Anuska\Travel2021\Daily_Travel_Booking\Pictures\Varanasi_7Days_Package.png")
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
    label1.place(x=235, y=140)
    ycord=ycord+150
    
    Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=2,width=10, bg='light green', fg='black',command=btnVaranasi1_click).place(x=970, y=280)
    Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=2,width=10, bg='light green', fg='black',command=btnVaranasi2_click).place(x=970, y=420)
    Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=2,width=10, bg='light green', fg='black',command=btnVaranasi3_click).place(x=970, y=550)
    Button(root, text="Gallery",font=("Times New Roman",13,"bold"), height=2,width=10, bg='light green', fg='black',command=btnAsShowGallery_clik).place(x=970, y=150)
root.mainloop()




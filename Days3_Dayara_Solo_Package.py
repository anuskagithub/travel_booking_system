from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
#import mysqconnector

import DataAccess

def btnAsShowGallery_clik():
    DataAccess.put_GlobalVal("Dayara Bugyal")
    root.destroy()
    import Gallery

def btnDayaraBugyal1_click():
    DataAccess.put_GlobalVal("Solo Package of Dayara Bugyal trek","Solo")
    root.destroy()
    import Booking_TourPackage
   
def btnDayaraBugyal2_click():
    DataAccess.put_GlobalVal("Magical -Dayara Bugyal","Solo")
    root.destroy()
    import Booking_TourPackage

def btnDayaraBugyal3_click():
    DataAccess.put_GlobalVal("Dayara Bugyal in 3days","Solo")
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


lbl_heading=Label(root, text="Dayara Bugyal Trek 3 Days Package",fg="black",bg="light green",font=("Times New Roman",25),relief="ridge",pady=10,border=10).pack(fill='x')

canvas = Canvas(root, width = 3000, height = 3000)
canvas.pack()

img = ImageTk.PhotoImage(Image.open("D:\Anuska\Travel2021\Daily_Travel_Booking\Pictures\Dayara_Bugyalbg.jpg"))
canvas.create_image(0, 0, anchor=NW, image=img)

lstPack= []
lstPack.append("D:\Anuska\Travel2021\Daily_Travel_Booking\Pictures\Dayara_Bugyal_SoloPackage.JPG")
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
    label1.place(x=120, y=200)
    ycord=ycord+150
    
    Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=2,width=10, bg='light green', fg='black',command=btnDayaraBugyal1_click).place(x=1030, y=285)
    Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=2,width=10, bg='light green', fg='black',command=btnDayaraBugyal2_click).place(x=1030, y=360)
    Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=2,width=10, bg='light green', fg='black',command=btnDayaraBugyal3_click).place(x=1030, y=430)
    Button(root, text="Gallery",font=("Times New Roman",13,"bold"), height=2,width=10, bg='light green', fg='black',command=btnAsShowGallery_clik).place(x=1030, y=215)
    
root.mainloop()


from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
#import mysqconnector

import DataAccess

def btnBhirgu1_click():
    DataAccess.put_GlobalVal("Bhirgu Lake  Trek","Solo")
    root.destroy()
    import Booking_TourPackage
   
def btnBhirgu2_click():
    DataAccess.put_GlobalVal("Reasonable Bhirgu lake ","Solo")
    root.destroy()
    import Booking_TourPackage

def btnBhirgu3_click():
    DataAccess.put_GlobalVal("Adventures of Bhirgu lake","Solo")
    root.destroy()
    import Booking_TourPackage

def btnAsShowGallery_clik():
    DataAccess.put_GlobalVal("Bhirgu")
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


lbl_heading=Label(root, text="Bhrigu Lake Trek 3 Days Package",fg="black",bg="light green",font=("Times New Roman",25),relief="ridge",pady=10,border=10).pack(fill='x')

canvas = Canvas(root, width = 1400, height = 700)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("D:/Anuska/Travel2021/Daily_Travel_Booking/Pictures/bhirulakebg.jpg"))
canvas.create_image(0, 0, anchor=NW, image=img)

lstPack= []
lstPack.append("D:\Anuska\Travel2021\Daily_Travel_Booking\Pictures\Bhirgu_Lake_SoloPackage.JPG")
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
    label1.place(x=166, y=150)
    ycord=ycord+150
    
    Button(root, text="Gallery",font=("Times New Roman",13,"bold"), height=3,width=10, bg='light green', fg='black',command=btnAsShowGallery_clik).place(x=1075, y=150)
    Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=3,width=10, bg='light green', fg='black',command=btnBhirgu1_click).place(x=1075, y=225)
    Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=3,width=10, bg='light green', fg='black',command=btnBhirgu2_click).place(x=1075, y=300)
    Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=3,width=10, bg='light green', fg='black',command=btnBhirgu3_click).place(x=1075, y=375)
    
root.mainloop()



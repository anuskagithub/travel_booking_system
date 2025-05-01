##DAYS3_LONAVALA_GROUP_PACKAGE(HRISHEETA)##


from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
#import mysqconnector

import DataAccess

def btnLONAVALA1_click():
    DataAccess.put_GlobalVal("Short Trip to Lonavala Ex Pune - Weekend Getaway","Group")
    root.destroy()
    import Booking_TourPackage
   
def btnLONAVALA2_click():
    DataAccess.put_GlobalVal("Drivacation to Lonavala","Group")
    root.destroy()
    import Booking_TourPackage

def btnLONAVALA3_click():
    DataAccess.put_GlobalVal("Lonavala Self Drive - Ex Mumbai","Group")
    root.destroy()
    import Booking_TourPackage
    
def btnAsShowGallery_clik():
    DataAccess.put_GlobalVal("Lonavala")
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


lbl_heading=Label(root, text="LONAVALA  - 3 Days Group Package",fg="black",bg="light green",font=("Times New Roman",25),relief="ridge",pady=10,border=10).pack(fill='x')
#Button(root, text="Back",font=("Arial",9,"bold"), height=2,width=10, bg='light green', fg='black',command=btnBack_Click).place(x=15, y=20)

canvas = Canvas(root, width = 3000, height = 3000)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("D:\Anuska\Travel2021\Daily_Travel_Booking\Pictures\Lonavala_Bg.jpg"))
canvas.create_image(0, 0, anchor=NW, image=img)

lstPack= []
lstPack.append("D:\Anuska\Travel2021\Daily_Travel_Booking\Pictures\Lonavla_3Days_GroupPackage.jpeg")
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
    label1.place(x=220, y=190)
    ycord=ycord+150
    
    Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=2,width=10, bg='light green', fg='black',command=btnLONAVALA1_click).place(x=930, y=350)
    Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=2,width=10, bg='light green', fg='black',command=btnLONAVALA2_click).place(x=930, y=448)
    Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=2,width=10, bg='light green', fg='black',command=btnLONAVALA3_click).place(x=930, y=555)
    Button(root, text="Gallery",font=("Times New Roman",13,"bold"), height=2,width=10, bg='light green', fg='black',command=btnAsShowGallery_clik).place(x=930, y=240)
root.mainloop()

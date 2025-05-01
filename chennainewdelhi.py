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
root.title("Admin Console")
root.config(bg="white")

def btnAsBookNow_clik():
    root.destroy()
    import Booking_Flight

lbl_heading=Label(root, text="Chennai to New Delhi",fg="black",bg="violet",font=("Times New Roman",25),relief="ridge",pady=10,border=10).pack(fill='x')

canvas = Canvas(root, width = 3000, height = 3000)
canvas.pack()

img = ImageTk.PhotoImage(Image.open("D:\Anuska\Travel2021\Daily_Travel_Booking\Pictures\Flightbg.jpg"))
canvas.create_image(0, 0, anchor=NW, image=img)

lstPack= []
lstPack.append("D:\Anuska\Travel2021\Daily_Travel_Booking\Pictures\ChennaiToNewDelhi.PNG")
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
    label1.place(x=20, y=180)
    ycord=ycord+150
    
Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=1,width=15, bg='violet', fg='black',command=btnAsBookNow_clik).place(x=750, y=335)
Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=1,width=15, bg='violet', fg='black',command=btnAsBookNow_clik).place(x=750, y=395)
Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=1,width=15, bg='violet', fg='black',command=btnAsBookNow_clik).place(x=750, y=455)
Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=1,width=15, bg='violet', fg='black',command=btnAsBookNow_clik).place(x=750, y=509)
Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=1,width=15, bg='violet', fg='black',command=btnAsBookNow_clik).place(x=750, y=565)




root.mainloop()


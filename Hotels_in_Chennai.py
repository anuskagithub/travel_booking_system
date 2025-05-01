from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import DataAccess

root = Tk()
#getting screen width and height of display
Wwidth= root.winfo_screenwidth() 
Wheight= root.winfo_screenheight()
#setting tkinter window size
root.geometry("%dx%d" % (Wwidth, Wheight))
root.title("Admin Console")
root.config(bg="white")

def btnAsBookChennaiHotel1_clik():
    DataAccess.put_GlobalVal("The Leela Palace Chennai","Chennai")
    root.destroy()
    import Hotels_BookingDetails
    
def btnAsBookChennaiHotel2_clik():
    DataAccess.put_GlobalVal("Novotel Chennai Sipcot","Chennai")
    root.destroy()
    import Hotels_BookingDetails

def btnAsBookChennaiHotel3_clik():
    DataAccess.put_GlobalVal("ITC Grand","Chennai")
    root.destroy()
    import Hotels_BookingDetails    

lbl_heading=Label(root, text="Hotels in Chennai",fg="black",bg="light blue",font=("Times New Roman",25),relief="ridge",pady=10,border=10).pack(fill='x')

canvas = Canvas(root, width = 3000, height = 3000)
canvas.pack()

#img = ImageTk.PhotoImage(Image.open("D:/Anuska/Travel2021/Daily_Travel_Booking/Pictures/Alleppeybg6.jpeg"))
#canvas.create_image(0, 0, anchor=NW, image=img)

lstPack= []
lstPack.append("D:\Anuska\Travel2021\Daily_Travel_Booking\Pictures\CHENNAI_HotelBooking.jpg")
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
    label1.place(x=7, y=75)
    ycord=ycord+150
    
Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=2,width=15, bg='light blue', fg='black',command=btnAsBookNow1_clik).place(x=1130, y=320)
Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=2,width=15, bg='light blue', fg='black',command=btnAsBookNow2_clik).place(x=1130, y=430)
Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=2,width=15, bg='light blue', fg='black',command=btnAsBookNow3_clik).place(x=1130, y=540)



root.mainloop()

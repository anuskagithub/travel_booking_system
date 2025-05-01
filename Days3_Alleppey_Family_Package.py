from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import DataAccess

def btnAsBookNow1_clik():
    DataAccess.put_GlobalVal("Tour Package Of Alleppey","Family")
    root.destroy()
    import Booking_TourPackage
    
def btnAsBookNow2_clik():
    DataAccess.put_GlobalVal("Catch The Beaity Of The Setting Sun In Alleppey","Family")
    root.destroy()
    import Booking_TourPackage    

def btnAsBookNow3_clik():
    DataAccess.put_GlobalVal("Wonderful Alleppey Weekend Special","Family")
    root.destroy()
    import Booking_TourPackage
    
def btnAsShowGallery_clik():
    DataAccess.put_GlobalVal("Alleppey")
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
root.title("Admin Console")
root.config(bg="silver")
lbl_heading=Label(root, text="Alleppey 3 Days Family Package",fg="black",bg="light green",font=("Times New Roman",25),relief="ridge",pady=10,border=10).pack(fill='x')
canvas = Canvas(root, width = 3000, height = 3000)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("D:\Anuska\Travel2021\Daily_Travel_Booking\Pictures\Alleppeybg.jpg"))
canvas.create_image(0, 0, anchor=NW, image=img)
lstPack= []
lstPack.append("D:\Anuska\Travel2021\Daily_Travel_Booking\Pictures\Screenshot (379).png")
# Create a photoimage object of the image in the path
for iPack in lstPack:
    image1 = Image.open(iPack)
    test = ImageTk.PhotoImage(image1)
    label1 = Label(image=test)
    label1.image = test
        # Position image
    label1.place(x=220, y=200)
    Button(root, text="Gallery",font=("Times New Roman",13,"bold"), height=3,width=10, bg='light green', fg='black',command=btnAsShowGallery_clik).place(x=915, y=215)
    Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=3,width=10, bg='light green', fg='black',command=btnAsBookNow1_clik).place(x=915, y=315)
    Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=3,width=10, bg='light green', fg='black',command=btnAsBookNow2_clik).place(x=915, y=425)
    Button(root, text="Book Now",font=("Times New Roman",13,"bold"), height=3,width=10, bg='light green', fg='black',command=btnAsBookNow3_clik).place(x=915, y=530)
    
root.mainloop()

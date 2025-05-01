from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import mysql.connector

def btnAsSearch_clik():
    d=int(DurationOfVisit.get())
    if d==3:
        root.destroy()
        import Days3_All_Solo_Packages
    if d==7:
        root.destroy()
        import Days7_All_Solo_Packages
    
    if d==15:
        root.destroy()
        import Days15_All_Solo_Packages

root = Tk()
#getting screen width and height of display
Wwidth= root.winfo_screenwidth() 
Wheight= root.winfo_screenheight()
#setting tkinter window size
root.geometry("%dx%d" % (Wwidth, Wheight))
root.title("Admin Console")
root.config(bg="white")

n=StringVar()

lbl_heading=Label(root, text="Solo Tour Package",fg="black",bg="light green",font=("Times New Roman",25),relief="ridge",pady=10,border=10).pack(fill='x')

canvas = Canvas(root, width = 1360, height = 650)
canvas.pack()

img = ImageTk.PhotoImage(Image.open("D:/Anuska/Travel2021/Daily_Travel_Booking/Pictures/bg_DurationOfVisit.jpg"))
canvas.create_image(0, 0, anchor=NW, image=img)


label_DurationOfVisit=Label(root, text="Duration of Visit:",fg="Black", bg="white", font=("Times New Roman", 18, "bold"))
label_DurationOfVisit.place(x=140, y=100)
DurationOfVisit=Combobox(root, width = 15, textvariable = n)
DurationOfVisit['values'] = ('3','7','15')

DurationOfVisit.place(x=400, y=105)
DurationOfVisit.current()

Button(root, text="Search",font=("Times New Roman",13,"bold"), height=1,width=10, bg='blue', fg='white',command=btnAsSearch_clik).place(x=550, y=100)



root.mainloop()




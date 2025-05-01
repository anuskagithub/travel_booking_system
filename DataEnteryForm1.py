from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import mysql.connector

import DataAccess


def btnSaveStudent_Click():
    varRoll=StRoll.get();
    varName=StName.get();
    #varMrks=
    #varAge=
        
    DataAccess.Add_Student(varRoll,varName,95.75,10)
#End of btnSaveStudent_Click    

root = Tk()

#getting screen width and height of display
Wwidth= root.winfo_screenwidth() 
Wheight= root.winfo_screenheight()
#setting tkinter window size
root.geometry("%dx%d" % (Wwidth, Wheight))
root.title("Students Registration Form")
root.config(bg="cadet blue")

# Open the Image File
im = Image.open("D:/Anuska/Travel2021/Daily_Travel_Booking/Travel.jpg","r")
#bg = ImageTk.PhotoImage(file="D:\\Anuska\\Travel2021\\Daily_Travel_Booking\\Travel.jpg")
bg = ImageTk.PhotoImage(im)

# Create a Canvas
canvas = Canvas(root, width=Wwidth, height=Wheight)
canvas.pack(fill=BOTH, expand=True)

# Add Image inside the Canvas
canvas.create_image(0, 0, image=bg, anchor='nw')

#Windw variables
StRoll=StringVar()
StName=StringVar()
#end

label=Label(root, text="Registration Form",bg="cadet blue", font=("bold", 20))
label.place(x=150, y=5)

lblRoll=Label(root, text="Roll No.",bg="blue", fg="black", font=("bold", 12))
lblRoll.place(x=50, y=75)
txtRoll=Entry(root, textvar=StRoll, width=10)
txtRoll.place(x=120, y=75)

lblName=Label(root, text="Name",bg="cadet blue", fg="black", font=("bold", 12))
lblName.place(x=50, y=100)
txtName=Entry(root, textvar=StName, width=30)
txtName.place(x=120, y=100)

btnSaveStudent=Button(text="Save", command=btnSaveStudent_Click, fg = "white", bg = "blue", font = "Time 10 bold")
btnSaveStudent.place(x=230, y=140)


root.mainloop()
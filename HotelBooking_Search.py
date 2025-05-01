from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import mysql.connector

root=Tk()

def btnAsSearch_clik():
    d=Destinationchoosen.get()
    
    if d=='Delhi':
       root.destroy()
       import Hotels_in_Delhi
    if d=='Mumbai':
        root.destroy()
        import Hotels_in_Mumbai
    if d=='Kolkata':
        root.destroy()
        import Hotels_in_Kolkata
    if d=='Chennai':
        root.destroy()
        import Hotels_in_Chennai
    if d=='Darjeeling':
        root.destroy()
        import Hotels_in_Darjeeling
    if d=='Puri':
        root.destroy()
        import Hotels_in_Puri
    if d=='Ladakh':
        root.destroy()
        import Hotels_in_Ladakh
    if d=='Sikkim':
        root.destroy()
        import Hotels_in_Sikkim
    if d=='Varanasi':
        root.destroy()
        import Hotels_in_Varanasi
    if d=='Andaman and Nicobar':
        root.destroy()
        import Hotels_in_Andaman_and_Nicobar_Islands
    if d=='Pondicherry':
        root.destroy()
        import Hotels_in_Pondicherry
    if d=='Rajasthan':
        root.destroy()
        import Hotels_in_Rajasthan
    if d=='Goa':
        root.destroy()
        import Hotels_in_Goa



Wwidth= root.winfo_screenwidth() 
Wheight= root.winfo_screenheight()
root.geometry("%dx%d+%d+%d" % (Wwidth, Wheight,0,0))
root.config(bg="white")
root.title("Hotel Booking")


n=StringVar()
n1=StringVar()

lbl_heading=Label(root, text="HOTEL BOOKINGS",fg="black",bg="light green",font=("Times New Roman",25),relief="ridge",pady=10,border=10).pack(fill='x')

canvas = Canvas(root, width = 1400, height = 272)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("D:/Anuska/Travel2021/Daily_Travel_Booking/Pictures/HotelBookingbg.jpg"))
canvas.create_image(0, 0, anchor=NW, image=img)

label_Destination=Label(root, text="Your Destination:",fg="Black", bg="white", font=("Times New Roman", 18, "bold"))
label_Destination.place(x=240, y=450)
Destinationchoosen=Combobox(root, width = 15, textvariable = n)
Destinationchoosen['values'] = ('Delhi', 'Mumbai','Kolkata','Chennai','Darjeeling','Puri','Ladakh','Sikkim','Varanasi','Andaman and Nicobar','Pondicherry','Rajasthan','Goa')

Destinationchoosen.place(x=440, y=455)
Destinationchoosen.current()



Button(root, text="SEARCH", width=12,height=1, bg='black', fg='white', font=("calibri 15"),command=btnAsSearch_clik).place(x=750, y=450)

Home_Frame=Frame(root,bd=3, relief=RIDGE, bg="cadet blue")
Home_Frame.place(x=0, y=350, width=1365, height=80)    

lbl1=Label(Home_Frame, text="Our software is centered on making travel simple and has been designed to let you look for cheap packages and to complete your bookings in just a few clicks. We are known for providing the \n best travel deals to travelers.We can satisfy all your travel needs.Book your hotels here at a cost-effective price.So,why go anywhere else? Visit us for a memorable travel experience \n in your budget.Travel India your way and get ready for a hassle-free experience with us!", bg="cadet blue",fg="black",font=("Arial 12 italic"))
lbl1.grid(row=0, column=0, padx=0,pady=0, sticky="w")

root.mainloop()



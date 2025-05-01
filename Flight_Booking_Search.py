from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import mysql.connector

root=Tk()

Wwidth= root.winfo_screenwidth() 
Wheight= root.winfo_screenheight()
root.geometry("%dx%d+%d+%d" % (Wwidth, Wheight,0,0))
root.config(bg="white")
root.title("Flight Booking")

def btnAsSearch_clik():
  
    s=SourceCitychoosen.get()
    d=DestinationCitychoosen.get()
    if s=='New Delhi' and d=='Mumbai':
        root.destroy()
        import newdelhimumbai
    

    if s=='Mumbai' and d=='New Delhi':
        root.destroy()
        import mumbainewdelhi
 
    if s=='Chennai' and d=='Kolkata':
        root.destroy()
        import chennaikolkata
    

    if s=='Kolkata' and d=='Chennai':
        root.destroy()
        import kolkatachennai
    
   
    if s=='Kolkata' and d=='Mumbai':
        root.destroy()
        import kolkatamumbai
    
   
    if s=='Mumbai' and d=='Kolkata':
        root.destroy()
        import mumbaikolkata
    
    
    if s=='Chennai' and d=='Mumbai':
        root.destroy()
        import chennaimumbai
    
   
    if s=='Mumbai' and d=='Chennai':
        root.destroy()
        import mumbaichennai
    
  
    if s=='Chennai' and d=='Newdelhi':
        root.destroy()
        import chennainewdelhi
    
    
    if s=='New Delhi' and d=='Chennai':
        root.destroy()
        import newdelhichennai
    
   
    if s=='Kolkata' and d=='New Delhi':
        root.destroy()
        import kolkatanewdelhi
    
   
    if s=='New Delhi' and d=='Kolkata':
        root.destroy()
        import newdelhikolkata
    
  
    if s=='Hyderabad' and d=='Ahmedabad':
        root.destroy()
        import hyderabadahmedabad
    
   
    if s=='Ahmedabad' and d=='Hyderabad':
        root.destroy()
        import ahmedabadhyderabad
    
  
    if s=='Guwahati' and d=='Amritsar':
        root.destroy()
        import guwahatiamritsar
    
    
    if s=='Amritsar' and d=='Guwahati':
        root.destroy()
        import amritsarguwahati
    

    if s=='Srinagar' and d=='Jaipur':
        root.destroy()
        import srinagarjaipur
    
   
    if s=='Jaipur' and d=='Srinagar':
        root.destroy()
        import jaipursrinagar
        
n=StringVar()
n1=StringVar()

lbl_heading=Label(root, text="FLIGHT BOOKINGS",fg="black",bg="light green",font=("Times New Roman",25),relief="ridge",pady=10,border=10).pack(fill='x')

canvas = Canvas(root, width = 4050, height = 272)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("D:/Anuska/Travel2021/Daily_Travel_Booking/Pictures/FlightBookingBg.jpg"))
canvas.create_image(0, 0, anchor=NW, image=img)

label_SourceCity=Label(root, text="SOURCE CITY:",fg="Black", bg="white", font=("Times New Roman", 18, "bold"))
label_SourceCity.place(x=140, y=450)
SourceCitychoosen=Combobox(root, width = 15, textvariable = n)
SourceCitychoosen['values'] = ('New Delhi', 'Mumbai','Kolkata','Chennai','Srinagar','Jaipur','Amritsar','Guwahati','Hyderabad','Ahmedabad')

SourceCitychoosen.place(x=340, y=455)
SourceCitychoosen.current()


label_DestinationCity=Label(root, text="DESTINATION CITY:",fg="Black", bg="white", font=("Times New Roman", 18, "bold"))
label_DestinationCity.place(x=580, y=450)
DestinationCitychoosen=Combobox(root, width = 15, textvariable = n1)
DestinationCitychoosen['values'] = ('New Delhi', 'Mumbai','Kolkata','Chennai','Srinagar','Jaipur','Amritsar','Guwahati','Hyderabad','Ahmedabad')

DestinationCitychoosen.place(x=840, y=455)
DestinationCitychoosen.current()

Button(root, text="SEARCH", width=12,height=1, bg='black', fg='white', font=("calibri 15"),command=btnAsSearch_clik).place(x=1050, y=450)

Home_Frame=Frame(root,bd=3, relief=RIDGE, bg="cadet blue")
Home_Frame.place(x=0, y=350, width=1354, height=80)    

lbl1=Label(Home_Frame, text="Our software is centered on making travel simple and has been designed to let you look for cheap packages and to complete your bookings in just a few clicks. We are known for providing \n the best travel deals to travelers.We can satisfy all your travel needs.Book your flights here at a cost-effective price.So,why go anywhere else? Visit us for a memorable travel experience \n in your budget.Travel India your way and get ready for a hassle-free experience with us!", bg="cadet blue",fg="black",font=("Arial 12 italic"))
lbl1.grid(row=0, column=0, padx=0,pady=0, sticky="w")

root.mainloop()
    

n=StringVar()
n1=StringVar()

lbl_heading=Label(root, text="FLIGHT BOOKINGS",fg="black",bg="light green",font=("Times New Roman",25),relief="ridge",pady=10,border=10).pack(fill='x')

canvas = Canvas(root, width = 4050, height = 272)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("D:/Anuska/Travel2021/Daily_Travel_Booking/Pictures/FlightBookingBg.jpg"))
canvas.create_image(0, 0, anchor=NW, image=img)

label_SourceCity=Label(root, text="SOURCE CITY:",fg="Black", bg="white", font=("Times New Roman", 18, "bold"))
label_SourceCity.place(x=140, y=450)
SourceCitychoosen=Combobox(root, width = 15, textvariable = n)
SourceCitychoosen['values'] = ('New Delhi', 'Mumbai','Kolkata','Chennai','Jaipur','Amritsar','Guwahati','Hyderabad','Ahmedabad')

SourceCitychoosen.place(x=340, y=455)
SourceCitychoosen.current()


label_DestinationCity=Label(root, text="DESTINATION CITY:",fg="Black", bg="white", font=("Times New Roman", 18, "bold"))
label_DestinationCity.place(x=580, y=450)
DestinationCitychoosen=Combobox(root, width = 15, textvariable = n1)
DestinationCitychoosen['values'] = ('New Delhi', 'Mumbai','Kolkata','Chennai','Jaipur','Amritsar','Guwahati','Hyderabad','Ahmedabad')

DestinationCitychoosen.place(x=840, y=455)
DestinationCitychoosen.current()

Button(root, text="SEARCH", width=12,height=1, bg='black', fg='white', font=("calibri 15"),command=btnAsSearch_clik).place(x=1050, y=450)

Home_Frame=Frame(root,bd=3, relief=RIDGE, bg="cadet blue")
Home_Frame.place(x=0, y=350, width=1354, height=80)    

lbl1=Label(Home_Frame, text="Our software is centered on making travel simple and has been designed to let you look for cheap packages and to complete your bookings in just a few clicks. We are known for providing \n the best travel deals to travelers.We can satisfy all your travel needs.Book your flights here at a cost-effectiveprice.So,why go anywhere else? Visit us for a memorable travel experience \n in your budget.Travel India your way and get ready for a hassle-free experience with us!", bg="cadet blue",fg="black",font=("Arial 12 italic"))
lbl1.grid(row=0, column=0, padx=0,pady=0, sticky="w")

root.mainloop()
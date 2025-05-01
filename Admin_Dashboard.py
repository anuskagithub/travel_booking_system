from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import ImageTk, Image
import matplotlib.pyplot as plt

import DataAccess    


def btnAsShowTourBookings_click():
    root.destroy()
    import AdminWin_PackageBooking
    
def btnAsShowHotelBookings_click():
    root.destroy()
    import AdminWin_HotelBooking
    
def btnAsShowFlightBookings_click():
    root.destroy()
    import AdminWin_FlightBooking    
    
def ShowBookingSummary(allBookings,  xPos, yPos):
    tvPBooking = ttk.Treeview(root, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13), show='headings', height=5)
    #tvPBooking.pack()
    tvPBooking.heading(1, text="Year", anchor=CENTER)
    tvPBooking.heading(2, text="January", anchor=CENTER)
    tvPBooking.heading(3, text="February", anchor=CENTER)
    tvPBooking.heading(4, text="March", anchor=CENTER)
    tvPBooking.heading(5, text="April", anchor=CENTER)
    tvPBooking.heading(6, text="May", anchor=CENTER)
    tvPBooking.heading(7, text="June", anchor=CENTER)
    tvPBooking.heading(8, text="July", anchor=CENTER)
    tvPBooking.heading(9, text="August", anchor=CENTER)
    tvPBooking.heading(10, text="September", anchor=CENTER)
    tvPBooking.heading(11, text="October", anchor=CENTER)
    tvPBooking.heading(12, text="November", anchor=CENTER)
    tvPBooking.heading(13, text="December", anchor=CENTER)

    tvPBooking.column(1, width=100, anchor=CENTER)
    tvPBooking.column(2, width=100, anchor=CENTER)
    tvPBooking.column(3, width=100, anchor=CENTER)
    tvPBooking.column(4, width=100, anchor=CENTER)
    tvPBooking.column(5, width=100, anchor=CENTER)
    tvPBooking.column(6, width=100, anchor=CENTER)
    tvPBooking.column(7, width=100, anchor=CENTER)
    tvPBooking.column(8, width=100, anchor=CENTER)
    tvPBooking.column(9, width=100, anchor=CENTER)
    tvPBooking.column(10, width=100, anchor=CENTER)
    tvPBooking.column(11, width=100, anchor=CENTER)
    tvPBooking.column(12, width=100, anchor=CENTER)
    tvPBooking.column(13, width=100, anchor=CENTER)
    #End Tree View
    
    
    lstYear=[2021,2022,2023,2024,2025]
    
    lstBookings=[[2021,0,0,0,0,0,0,0,0,0,0,0,0],
                 [2022,0,0,0,0,0,0,0,0,0,0,0,0],
                 [2023,0,0,0,0,0,0,0,0,0,0,0,0],
                 [2024,0,0,0,0,0,0,0,0,0,0,0,0],
                 [2025,0,0,0,0,0,0,0,0,0,0,0,0]]
    i=0
    for yr in lstYear:
        lstBookings[i][0]=yr
        for m in range(1,13):
            lstBookings[i][m]=GetMonthValue(allBookings, yr,m)
            
        i=i+1

    #print(lstTours)             
    i=0
    for bkn in lstBookings:
        rowType='oddrow'
        if i%2==0:
            rowType='evenrow'            
        tvPBooking.insert(parent='', index=i, iid=i, tags=(rowType,), values=(bkn[0], bkn[1], bkn[2], bkn[3], bkn[4], bkn[5], bkn[6], bkn[7], bkn[8], bkn[9], bkn[10], bkn[11], bkn[12]))
        i=i+1
        
    tvPBooking.pack()
    tvPBooking.tag_configure('oddrow', background='gray')
    tvPBooking.tag_configure('evenrow', background='silver')
     
    tvPBooking.place(x=xPos,y=yPos)
    tvPBooking.focus(1)
    tvPBooking.selection_set(1)
    
def GetMonthValue(bookings, bYear, bMonth):
    totalBookingFoThisMonth='-'
    for booking in bookings:
        if booking[0]==bYear and booking[1]==bMonth:
            totalBookingFoThisMonth=booking[2]
            break
   
    return totalBookingFoThisMonth                 
         
#Window settings
root = Tk()

#getting screen width and height of display
Wwidth= root.winfo_screenwidth() 
Wheight= root.winfo_screenheight()
#setting tkinter window size
root.geometry("%dx%d" % (Wwidth, Wheight))
root.title("Admin Console")
root.config(bg="light blue")

lbl_heading=Label(root, text="Welcome to Admin Dashboard",fg="black",bg="light green",font=("Impact 25"),relief="ridge",pady=10,border=10).pack(fill='x')

allBookings = DataAccess.Get_AllTourBookingMonthWise()
lbl_PBooking=Label(root, text="Package Tour Booking Summary:",fg="black",bg="light blue",font=("Arial 10 bold italic underline"))
lbl_PBooking.place(x=30, y=85)
ShowBookingSummary(allBookings, 30, 105)
lbl_PBooking=Label(root, text="                                                                                                                                                                                                                                                                   ",fg="black",bg="gray",font=("Arial 14"))
lbl_PBooking.place(x=30, y=230)
Button(root, text="Show All Bookings", width=15, bg='dodgerblue', fg='white',command=btnAsShowTourBookings_click).place(x=630, y=230)

allBookings = DataAccess.Get_AllHotelBookingMonthWise()
lbl_PBooking=Label(root, text="Hotel Booking Summary:",fg="black",bg="light blue",font=("Arial 10 bold italic underline"))
lbl_PBooking.place(x=30, y=290)
ShowBookingSummary(allBookings, 30, 310)
lbl_PBooking=Label(root, text="                                                                                                                                                                                                                                                                   ",fg="black",bg="gray",font=("Arial 14"))
lbl_PBooking.place(x=30, y=435)
Button(root, text="Show All Bookings", width=15, bg='dodgerblue', fg='white',command=btnAsShowHotelBookings_click).place(x=630, y=435)

allBookings = DataAccess.Get_AllFlightBookingMonthWise()
lbl_PBooking=Label(root, text="Flight Booking Summary:",fg="black",bg="light blue",font=("Arial 10 bold italic underline"))
lbl_PBooking.place(x=30, y=495)
ShowBookingSummary(allBookings, 30, 515)
lbl_PBooking=Label(root, text="                                                                                                                                                                                                                                                                   ",fg="black",bg="gray",font=("Arial 14"))
lbl_PBooking.place(x=30, y=640)
Button(root, text="Show All Bookings", width=15, bg='dodgerblue', fg='white',command=btnAsShowFlightBookings_click).place(x=630, y=640)
    
root.mainloop()


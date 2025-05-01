from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import ImageTk, Image

import DataAccess    

allBookings = DataAccess.Get_AllHotelBookings()

def ShowAllBookings():
    ClearAllFromTreeView()
    i=0
    for bkn in allBookings:
        tv.insert(parent='', index=i, iid=i, values=(bkn[1], bkn[2], bkn[3], bkn[5], bkn[6], bkn[7], bkn[8], bkn[9], bkn[10], bkn[11]))
        i=i+1
        tv.pack()
        
def ShowAllBookingsBySearch():
    month = monthchoosen.get()
    year = yearchoosen.get()
    location = txtLocation.get()
    
    ShowFilteredData(month,year,location)
        
def ShowFilteredData(month,year,location):
     ClearAllFromTreeView()
     monthIndex=0
     yearIndex=0
     locationIndex=0
     
     i=0
     for bkn in allBookings:
          if month!='':
               monthIndex = bkn[3].find(month)
               
          if year!='':
              yearIndex =  bkn[3].find(year)
              
          if location!='':
              locationIndex = bkn[2].lower().find(location.lower())
              
          if monthIndex>-1 and yearIndex>-1 and locationIndex>-1:
              tv.insert(parent='', index=i, iid=i, values=(bkn[1], bkn[2], bkn[3], bkn[5], bkn[6], bkn[7], bkn[8], bkn[9], bkn[10], bkn[11]))
              i=i+1
              tv.pack()
              
def ClearAllFromTreeView():
   for item in tv.get_children():
       tv.delete(item)
        
#Window settings
root = Tk()

#getting screen width and height of display
Wwidth= root.winfo_screenwidth() 
Wheight= root.winfo_screenheight()
#setting tkinter window size
root.geometry("%dx%d" % (Wwidth, Wheight))
root.title("Admin Console")
root.config(bg="light blue")

lbl_heading=Label(root, text="Hotel Booking Information",fg="black",bg="light green",font=("Impact",25),relief="ridge",pady=10,border=10).pack(fill='x')

label_01=Label(root, text="Select  Month",fg="Black", bg="light green", font=("ARIAL 10 bold"))
label_01.place(x=980, y=17)

monthchoosen=Combobox(root, width = 5)
#monthchoosen['values'] = ('January','February','March','April','May','June','July','August','September','October','November','December')
monthchoosen['values'] = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
monthchoosen.place(x=1070, y=17)
monthchoosen.current()

label_02=Label(root, text="Year",fg="Black", bg="light green", font=("ARIAL 10 bold"))
label_02.place(x=1120, y=17)
yearchoosen=Combobox(root, width = 5)
yearchoosen['values'] = ('2021','2022','2023','2024','2025')
yearchoosen.place(x=1152, y=17)
yearchoosen.current()

label_1=Label(root, text="Location:",fg="Black", bg="light green", font=("ARIAL 10 bold"))
label_1.place(x=983, y=40)
txtLocation=Entry(root, width=22)
txtLocation.place(x=1070, y=40)

Button(root, text="Filter", width=6, bg='light blue', fg='black',command=ShowAllBookingsBySearch).place(x=1210, y=25)
Button(root, text="Show All", width=6, bg='light blue', fg='black',command=ShowAllBookings).place(x=1265, y=25)

tv = ttk.Treeview(root, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), show='headings', height=25)
tv.pack()
#tv.place(x=200,y=1000)

tv.heading(1, text="Hotel Name", anchor=W)
tv.heading(2, text="Location", anchor=CENTER)
tv.heading(3, text="Booking Date", anchor=CENTER)
tv.heading(4, text="Total Room", anchor=CENTER)
tv.heading(5, text="Visitor Name", anchor=W)
tv.heading(6, text="Age", anchor=CENTER)
tv.heading(7, text="Sex", anchor=CENTER)
tv.heading(8, text="Mobie No", anchor=CENTER)
tv.heading(9, text="Email_ID", anchor=W)
tv.heading(10, text="Address", anchor=W)

tv.column(1, width=260)
tv.column(2, width=80, anchor=CENTER)
tv.column(3, width=100, anchor=CENTER)
tv.column(4, width=70, anchor=CENTER)
tv.column(5, width=170)
tv.column(6, width=55, anchor=CENTER)
tv.column(7, width=60, anchor=CENTER)
tv.column(8, width=100, anchor=CENTER)
tv.column(9, width=170)
tv.column(10, width=350)

#bookings = DataAccess.Get_Bookings()
ShowAllBookings()
#ShowAllBookingsByMonthYear(bookings,"Mar","2022")




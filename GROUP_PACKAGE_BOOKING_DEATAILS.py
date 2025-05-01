##GROUP_PACKAGE_BOOKING_DEATAILS(HRISHEETA)##


from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox

import sqlite3
import mysql.connector
def btnAsContinue_click():
    root.destroy()
    import PAYMENT_DETAILS




def AuthenticatePassenger():
    pname=txtMemberName.get()
    pMobileNo=txtMemberMobileNo.get()
    pEmail=txtMemberEmailID.get()
    pAdd=txtMemberrAddress.get()
    pAge=txtMemberAge.get()
    pSex=txtMemberSex.get()
    pDOJ=txtDateOfJourney.get()


#Window settings
root = Tk()

#getting screen width and height of display
root.geometry("%dx%d+%d+%d" % (750,670,200,15))
root.title("Booking Details...")
root.config(bg="light green")

txtMemberName=StringVar()
txtMemberMobileNo=StringVar()
txtMemberEmailID=StringVar()
txtMemberAddress=StringVar()
txtMemberAge=StringVar()
txtMemberSex=StringVar()
txtDateOfJourney=StringVar()

n1=StringVar()
n2=StringVar()
n3=StringVar()
n4=StringVar()
n5=StringVar()
n6=StringVar()
n7=StringVar()
n8=StringVar()

lbl_heading1=Label(root, text="PLEASE ENTER YOUR DETAILS",bg="light green",font=("TimesNewRoman 12 bold"))
lbl_heading1.place(x=20, y=15)

label_0=Label(root, text="Date of Journey:",fg="Black", bg="light green", font=("ARIAL 13 bold"))
label_0.place(x=30, y=50)
datechoosen=Combobox(root, width = 5, textvariable = n1)
datechoosen['values'] = ('1', '2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')

datechoosen.place(x=170, y=53)
datechoosen.current()


label_01=Label(root, text="",fg="Black", bg="light green", font=("ARIAL 13 bold"))
label_01.place(x=30, y=100)
monthchoosen=Combobox(root, width = 10, textvariable = n2)
monthchoosen['values'] = ('January','February','March','April','May','June','July','August','September','October','November','December')

monthchoosen.place(x=250, y=53)
monthchoosen.current()


label_02=Label(root, text="",fg="Black", bg="light green", font=("ARIAL 13 bold"))
label_02.place(x=30, y=200)
yearchoosen=Combobox(root, width = 7, textvariable = n3)
yearchoosen['values'] = ('2021','2022','2023','2024','2025')

yearchoosen.place(x=360, y=53)
yearchoosen.current()


label_1=Label(root, text="Name:",fg="Black", bg="light green", font=("ARIAL 13 bold"))
label_1.place(x=30, y=80)
txtMemberName=Entry(root, textvar=txtMemberName, width=40)
txtMemberName.place(x=140, y=83)

label_2=Label(root, text="Age:",fg="Black", bg="light green", font=("ARIAL 13 bold"))
label_2.place(x=400, y=80)
txtMemberAge=Entry(root, textvar=txtMemberAge, width=10)
txtMemberAge.place(x=450, y=83)

label_3=Label(root, text="Sex:",fg="Black", bg="light green", font=("ARIAL 13 bold"))
label_3.place(x=530, y=80)
sexchoosen=Combobox(root, width = 10, textvariable = n4)
sexchoosen['values'] = ('Male','Female','Others')

sexchoosen.place(x=580, y=83)
sexchoosen.current()


label_4=Label(root, text="Mobile No:", fg="Black", bg="light green", font=("ARIAL 13 bold"))
label_4.place(x=30, y=110)
txtMemberMobileNo=Entry(root, textvar=txtMemberMobileNo, width=40)
txtMemberMobileNo.place(x=140, y=113)

label_5=Label(root, text="Email Id:", fg="Black", bg="light green", font=("ARIAL 13 bold"))
label_5.place(x=400, y=113)
txtMemberEmailID=Entry(root, textvar=txtMemberEmailID, width=30)
txtMemberEmailID.place(x=480, y=113)

label_6=Label(root, text="Address:", fg="Black", bg="light green", font=("ARIAL 13 bold"))
label_6.place(x=30, y=140)
txtMemberAddress=Entry(root, textvar=txtMemberAddress, width=40)
txtMemberAddress.place(x = 140,y = 145,width=525, height=40)


lbl_heading2=Label(root, text="PLEASE ENTER DETAILS FOR OTHER MEMBERS OF THE FAMILY",bg="light green",font=("TimesNewRoman 12 bold"))
lbl_heading2.place(x=20, y=210)

label_7=Label(root, text="Member 1:",fg="Black", bg="light green", font=("ARIAL 13 bold"))
label_7.place(x=30, y=235)

label_8=Label(root, text="Name:",fg="Black", bg="light green", font=("ARIAL 13 bold"))
label_8.place(x=30, y=260)
txtMemberName=Entry(root, textvar=txtMemberName, width=45)
txtMemberName.place(x=100, y=265)

label_9=Label(root, text="Age:",fg="Black", bg="light green", font=("ARIAL 13 bold"))
label_9.place(x=405, y=260)
txtMemberAge=Entry(root, textvar=txtMemberAge, width=10)
txtMemberAge.place(x=452, y=265)

label_10=Label(root, text="Sex:",fg="Black", bg="light green", font=("ARIAL 13 bold"))
label_10.place(x=540, y=260)
sexchoosenp1=Combobox(root, width = 10, textvariable = n5)
sexchoosenp1['values'] = ('Male','Female','Others')

sexchoosenp1.place(x=585, y=265)
sexchoosenp1.current()


label_11=Label(root, text="Member 2:",fg="Black", bg="light green", font=("ARIAL 13 bold"))
label_11.place(x=30, y=295)

label_12=Label(root, text="Name:",fg="Black", bg="light green", font=("ARIAL 13 bold"))
label_12.place(x=30, y=325)
txtMemberName=Entry(root, textvar=txtMemberName, width=45)
txtMemberName.place(x=100, y=330)

label_13=Label(root, text="Age:",fg="Black", bg="light green", font=("ARIAL 13 bold"))
label_13.place(x=405, y=325)
txtMemberAge=Entry(root, textvar=txtMemberAge, width=10)
txtMemberAge.place(x=452, y=330)

label_14=Label(root, text="Sex:",fg="Black", bg="light green", font=("ARIAL 13 bold"))
label_14.place(x=540, y=325)
sexchoosenp2=Combobox(root, width = 10, textvariable = n6)
sexchoosenp2['values'] = ('Male','Female','Others')

sexchoosenp2.place(x=585, y=330)
sexchoosenp2.current()

label_15=Label(root, text="Member 3:",fg="Black", bg="light green", font=("ARIAL 13 bold"))
label_15.place(x=30, y=360)

label_16=Label(root, text="Name:",fg="Black", bg="light green", font=("ARIAL 13 bold"))
label_16.place(x=30, y=385)
txtMemberName=Entry(root, textvar=txtMemberName, width=45)
txtMemberName.place(x=100, y=390)

label_17=Label(root, text="Age:",fg="Black", bg="light green", font=("ARIAL 13 bold"))
label_17.place(x=405, y=385)
txtMemberAge=Entry(root, textvar=txtMemberAge, width=10)
txtMemberAge.place(x=452, y=390)

label_18=Label(root, text="Sex:",fg="Black", bg="light green", font=("ARIAL 13 bold"))
label_18.place(x=540, y=385)
sexchoosenp3=Combobox(root, width = 10, textvariable = n7)
sexchoosenp3['values'] = ('Male','Female','Others')

sexchoosenp3.place(x=585, y=390)
sexchoosenp3.current()

label_19=Label(root, text="Member 4:",fg="Black", bg="light green", font=("ARIAL 13 bold"))
label_19.place(x=30, y=420)

label_20=Label(root, text="Name:",fg="Black", bg="light green", font=("ARIAL 13 bold"))
label_20.place(x=30, y=445)
txtMemberName=Entry(root, textvar=txtMemberName, width=45)
txtMemberName.place(x=100, y=449)

label_21=Label(root, text="Age:",fg="Black", bg="light green", font=("ARIAL 13 bold"))
label_21.place(x=405, y=445)
txtMemberAge=Entry(root, textvar=txtMemberAge, width=10)
txtMemberAge.place(x=452, y=449)

label_22=Label(root, text="Sex:",fg="Black", bg="light green", font=("ARIAL 13 bold"))
label_22.place(x=540, y=445)
sexchoosenp4=Combobox(root, width = 10, textvariable = n8)
sexchoosenp4['values'] = ('Male','Female','Others')

sexchoosenp4.place(x=585, y=449)
sexchoosenp4.current()

label_19=Label(root, text="Member 5:",fg="Black", bg="light green", font=("ARIAL 13 bold"))
label_19.place(x=30, y=480)

label_20=Label(root, text="Name:",fg="Black", bg="light green", font=("ARIAL 13 bold"))
label_20.place(x=30, y=502)
txtMemberName=Entry(root, textvar=txtMemberName, width=45)
txtMemberName.place(x=100, y=507)

label_21=Label(root, text="Age:",fg="Black", bg="light green", font=("ARIAL 13 bold"))
label_21.place(x=405, y=502)
txtMemberAge=Entry(root, textvar=txtMemberAge, width=10)
txtMemberAge.place(x=452, y=507)

label_22=Label(root, text="Sex:",fg="Black", bg="light green", font=("ARIAL 13 bold"))
label_22.place(x=540, y=502)
sexchoosenp4=Combobox(root, width = 10, textvariable = n8)
sexchoosenp4['values'] = ('Male','Female','Others')

sexchoosenp4.place(x=585, y=507)
sexchoosenp4.current()

Button(root, text="Continue", width=12, bg='blue', fg='white', font=("calibri 15"),command=btnAsContinue_click).place(x=100, y=570)
root.mainloop()



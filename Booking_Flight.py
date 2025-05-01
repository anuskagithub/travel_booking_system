from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import mysql.connector
import random
import DataAccess


Flight_Rout=Packgae_Name=DataAccess.get_GlobalVal()[0][0]
Flight_Name=Packgae_Name=DataAccess.get_GlobalVal()[0][1]
  
def doDataValidation():
    dataValidate=True
    if datechoosen.get()=='Day':
        messagebox.showinfo('Data validation error.', 'Day should not be blank!')
        datechoosen.focus()
        dataValidate=False
    elif monthchoosen.get()=='Month':
        messagebox.showinfo('Data validation error.', 'Month should not be blank!')
        monthchoosen.focus()
        dataValidate=False
    elif yearchoosen.get()=='Year':
        messagebox.showinfo('Data validation error.', 'Year should not be blank!')
        yearchoosen.focus()
        dataValidate=False
    elif txtMemberName.get()=='':
        messagebox.showinfo('Data validation error.', 'Visitor\'s name should not be blank!')
        txtMemberName.focus()
        dataValidate=False
    elif txtMemberAge.get()=='':
        messagebox.showinfo('Data validation error.', 'Visitor\'s age should not be blank!')
        txtMemberAge.focus()
        dataValidate=False
    elif sexchoosen.get()=='':
        messagebox.showinfo('Data validation error.', 'Visitor\'s sex should not be blank!')
        sexchoosen.focus()
        dataValidate=False
    elif txtMemberMobileNo.get()=='':
        messagebox.showinfo('Data validation error.', 'Visitor\'s mobile number should not be blank!')
        txtMemberMobileNo.focus()
        dataValidate=False
    elif txtMemberEmailID.get()=='':
        messagebox.showinfo('Data validation error.', 'Visitor\'s email should not be blank!')
        txtMemberEmailID.focus()
        dataValidate=False
    elif txtMemberAddress.get()=='':
        messagebox.showinfo('Data validation error.', 'Visitor\'s address should not be blank!')
        txtMemberAddress.focus()
        dataValidate=False
        
    return dataValidate
 

def btnAsSubmit_clik():
    validate=doDataValidation()
    if validate==False:
        return  
    
    Journey_Date=monthchoosen.get()+" "+datechoosen.get()+" "+yearchoosen.get()
    Visitor_Name=txtMemberName.get()
    Age=int(txtMemberAge.get())
    Sex=sexchoosen.get()
    Mobie_No=int(txtMemberMobileNo.get())
    Email_ID=txtMemberEmailID.get()
    Address=txtMemberAddress.get()
    
    Mem1_Name=txtMember1Name.get()
    if txtMember1Age.get()=='':
        Mem1_Age=0
    else:
        Mem1_Age=int(txtMember1Age.get())
    Mem1_Sex=Member1sexchoosen.get()
    
    Mem2_Name=txtMember2Name.get()
    if txtMember2Age.get()=='':
        Mem2_Age=0
    else:
        Mem2_Age=int(txtMember2Age.get())
    Mem2_Sex=Member2sexchoosen.get()
   
    Mem3_Name=txtMember3Name.get()
    if txtMember3Age.get()=='':
        Mem3_Age=0
    else:
        Mem3_Age=int(txtMember3Age.get())
    Mem3_Sex=Member3sexchoosen.get()
    
    Mem4_Name=txtMember4Name.get()
    if txtMember4Age.get()=='':
        Mem4_Age=0
    else:
        Mem4_Age=int(txtMember4Age.get())
    Mem4_Sex=Member4sexchoosen.get()
       
    Mem5_Name=txtMember5Name.get()
    if txtMember5Age.get()=='':
        Mem5_Age=0
    else:
        Mem5_Age=int(txtMember5Age.get())
    Mem5_Sex=Member5sexchoosen.get()
        
    addrec_Success=DataAccess.Add_BookingFlight(Flight_Rout, Flight_Name, Journey_Date, Visitor_Name, Age, Sex, Mobie_No, Email_ID, Address, Mem1_Name, Mem1_Age, Mem1_Sex, Mem2_Name, Mem2_Age, Mem2_Sex, Mem3_Name, Mem3_Age, Mem3_Sex, Mem4_Name, Mem4_Age, Mem4_Sex, Mem5_Name, Mem5_Age, Mem5_Sex)
    if addrec_Success==True:
        root.destroy()
        import PaymentOptions
    else:
        messagebox.showinfo('Dada Save Error', "Sorry, not able to save the data. Please check your input and try again.")

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
root.geometry("%dx%d+%d+%d" % (700,600,200,15))
root.title("Flight Booking Details...")
root.config(bg="silver")
root.resizable(0,0)

txtMemberName=StringVar()
txtMemberMobileNo=StringVar()
txtMemberEmailID=StringVar()
txtMemberAddress=StringVar()
txtMemberAge=StringVar()
txtMemberSex=StringVar()
txtDateOfJourney=StringVar()

txtMember1Name=StringVar()
txtMember1Age=StringVar()

txtMember2Name=StringVar()
txtMember2Age=StringVar()

txtMember3Name=StringVar()
txtMember3Age=StringVar()

txtMember4Name=StringVar()
txtMember4Age=StringVar()

txtMember5Name=StringVar()
txtMember5Age=StringVar()

n1=StringVar()
n2=StringVar()
n3=StringVar()
n4=StringVar()
n5=StringVar()
n6=StringVar()
n7=StringVar()
n8=StringVar()

canvas = Canvas(root, width = 700, height = 100)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("D:/Anuska/Travel2021/Daily_Travel_Booking/Pictures/FlightBookingForm.jpg"))
canvas.create_image(0, 0, anchor=NW, image=img)  

flightName=Flight_Rout+",  "+Flight_Name
lbl_heading1=Label(root, text="Flight for: ",bg="silver",font=("TimesNewRoman 10 bold"))
lbl_heading1.place(x=1, y=105)
lbl_HotelName=Label(root, text=flightName, bg="white",font=("TimesNewRoman 10 bold"), width=82)
lbl_HotelName.place(x=65, y=105)

lbl_heading2=Label(root, text="Enter your details:",bg="Silver",font=("TimesNewRoman 10 bold italic"))
lbl_heading2.place(x=20, y=150)

label_0=Label(root, text="Journey Date:",fg="Black", bg="silver", font=("ARIAL 10 bold"))
label_0.place(x=30, y=185)
datechoosen=Combobox(root, width = 4)
datechoosen['values'] = ('Day','1', '2','3','4','5','6','7','8','9','10','11','12','10','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
datechoosen.place(x=140, y=185)
datechoosen.current(0)

monthchoosen=Combobox(root, width = 6)
monthchoosen['values'] = ('Month','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
monthchoosen.place(x=190, y=185)
monthchoosen.current(0)

yearchoosen=Combobox(root, width = 7)
yearchoosen['values'] = ('Year','2022','2023','2024','2025')
yearchoosen.place(x=250, y=185)
yearchoosen.current(0)

label_1=Label(root, text="Name:",fg="Black", bg="Silver", font=("ARIAL 10 bold"))
label_1.place(x=30, y=210)
txtMemberName=Entry(root, textvar=txtMemberName, width=40)
txtMemberName.place(x=140, y=210)

label_2=Label(root, text="Age:",fg="Black", bg="Silver", font=("ARIAL 10 bold"))
label_2.place(x=400, y=210)
txtMemberAge=Entry(root, textvar=txtMemberAge, width=10)
txtMemberAge.place(x=450, y=210)

label_3=Label(root, text="Sex:",fg="Black", bg="Silver", font=("ARIAL 10 bold"))
label_3.place(x=530, y=210)
sexchoosen=Combobox(root, width = 10, textvariable = n4)
sexchoosen['values'] = ('Male','Female','Others')
sexchoosen.place(x=580, y=210)
sexchoosen.current()

label_4=Label(root, text="Mobile No:", fg="Black", bg="Silver", font=("ARIAL 10 bold"))
label_4.place(x=30, y=235)
txtMemberMobileNo=Entry(root, textvar=txtMemberMobileNo, width=40)
txtMemberMobileNo.place(x=140, y=235)

label_5=Label(root, text="Email Id:", fg="Black", bg="Silver", font=("ARIAL 10 bold"))
label_5.place(x=400, y=235)
txtMemberEmailID=Entry(root, textvar=txtMemberEmailID, width=30)
txtMemberEmailID.place(x=480, y=235)

label_6=Label(root, text="Address:", fg="Black", bg="Silver", font=("ARIAL 10 bold"))
label_6.place(x=30, y=260)
txtMemberAddress=Entry(root, textvar=txtMemberAddress, width=40)
txtMemberAddress.place(x=140, y=260,width=525, height=40)

lbl_heading2=Label(root, text="Details of the other members",bg="Silver",font=("TimesNewRoman 10 bold italic"))
lbl_heading2.place(x=20, y=320)

#Memeber 1 detauls
label_7=Label(root, text="Member 1:",fg="Black", bg="Silver", font=("ARIAL 10 bold"))
label_7.place(x=20, y=365)

label_8=Label(root, text="Name:",fg="Black", bg="Silver", font=("ARIAL 10 bold"))
label_8.place(x=100, y=345)
txtMember1Name=Entry(root, textvar=txtMember1Name, width=60)
txtMember1Name.place(x=100, y=365)

label_9=Label(root, text="Age:",fg="Black", bg="Silver", font=("ARIAL 10 bold"))
label_9.place(x=495, y=345)
txtMember1Age=Entry(root, textvar=txtMember1Age, width=10)
txtMember1Age.place(x=495, y=365)

label_10=Label(root, text="Sex:",fg="Black", bg="Silver", font=("ARIAL 10 bold"))
label_10.place(x=585, y=345)
Member1sexchoosen=Combobox(root, width = 10, textvariable = n5)
Member1sexchoosen['values'] = ('Male','Female','Others')
Member1sexchoosen.place(x=585, y=365)
Member1sexchoosen.current()

#Memeber 2 detauls
label_11=Label(root, text="Member 2:",fg="Black", bg="Silver", font=("ARIAL 10 bold"))
label_11.place(x=20, y=390)

#label_12=Label(root, text="Name:",fg="Black", bg="Silver", font=("ARIAL 10 bold"))
#label_12.place(x=100, y=280)
txtMember2Name=Entry(root, textvar=txtMember2Name, width=60)
txtMember2Name.place(x=100, y=390)

#label_10=Label(root, text="Age:",fg="Black", bg="Silver", font=("ARIAL 10 bold"))
#label_10.place(x=452, y=280)
txtMember2Age=Entry(root, textvar=txtMember2Age, width=10)
txtMember2Age.place(x=495, y=390)

#label_14=Label(root, text="Sex:",fg="Black", bg="Silver", font=("ARIAL 10 bold"))
#label_14.place(x=585, y=280)
Member2sexchoosen=Combobox(root, width = 10, textvariable = n6)
Member2sexchoosen['values'] = ('Male','Female','Others')
Member2sexchoosen.place(x=585, y=390)
Member2sexchoosen.current()

#Memeber 3 detauls
label_15=Label(root, text="Member 3:",fg="Black", bg="Silver", font=("ARIAL 10 bold"))
label_15.place(x=20, y=415)

#label_16=Label(root, text="Name:",fg="Black", bg="Silver", font=("ARIAL 10 bold"))
#label_16.place(x=30, y=385)
txtMember3Name=Entry(root, textvar=txtMember3Name, width=60)
txtMember3Name.place(x=100, y=415)

#label_17=Label(root, text="Age:",fg="Black", bg="Silver", font=("ARIAL 10 bold"))
#label_17.place(x=405, y=385)
txtMember3Age=Entry(root, textvar=txtMember3Age, width=10)
txtMember3Age.place(x=495, y=415)

#label_18=Label(root, text="Sex:",fg="Black", bg="Silver", font=("ARIAL 10 bold"))
#label_18.place(x=540, y=385)
Member3sexchoosen=Combobox(root, width = 10, textvariable = n7)
Member3sexchoosen['values'] = ('Male','Female','Others')
Member3sexchoosen.place(x=585, y=415)
Member3sexchoosen.current()

#Memeber 4 detauls
label_19=Label(root, text="Member 4:",fg="Black", bg="Silver", font=("ARIAL 10 bold"))
label_19.place(x=20, y=440)

#label_20=Label(root, text="Name:",fg="Black", bg="Silver", font=("ARIAL 10 bold"))
#label_20.place(x=30, y=445)
txtMember4Name=Entry(root, textvar=txtMember4Name, width=60)
txtMember4Name.place(x=100, y=440)

#label_21=Label(root, text="Age:",fg="Black", bg="Silver", font=("ARIAL 10 bold"))
#label_21.place(x=405, y=445)
txtMember4Age=Entry(root, textvar=txtMember4Age, width=10)
txtMember4Age.place(x=495, y=440)

#label_22=Label(root, text="Sex:",fg="Black", bg="Silver", font=("ARIAL 10 bold"))
#label_22.place(x=540, y=445)
Member4sexchoosen=Combobox(root, width = 10, textvariable = n8)
Member4sexchoosen['values'] = ('Male','Female','Others')
Member4sexchoosen.place(x=585, y=440)
Member4sexchoosen.current()

#Memeber 5 detauls
label_19=Label(root, text="Member 5:",fg="Black", bg="Silver", font=("ARIAL 10 bold"))
label_19.place(x=20, y=465)

#label_20=Label(root, text="Name:",fg="Black", bg="Silver", font=("ARIAL 10 bold"))
#label_20.place(x=30, y=502)
txtMember5Name=Entry(root, textvar=txtMember5Name, width=60)
txtMember5Name.place(x=100, y=465)

#label_21=Label(root, text="Age:",fg="Black", bg="Silver", font=("ARIAL 10 bold"))
#label_21.place(x=405, y=502)
txtMember5Age=Entry(root, textvar=txtMember5Age, width=10)
txtMember5Age.place(x=495, y=465)

#label_22=Label(root, text="Sex:",fg="Black", bg="Silver", font=("ARIAL 10 bold"))
#label_22.place(x=540, y=502)
Member5sexchoosen=Combobox(root, width = 10, textvariable = n8)
Member5sexchoosen['values'] = ('Male','Female','Others')
Member5sexchoosen.place(x=585, y=465)
Member5sexchoosen.current()

Button(root, text="Submit", width=12, bg='Silver', fg='black', font=("calibri 15"),command=btnAsSubmit_clik).place(x=100, y=500)

lbl_TourName=Label(root, text="Based on on your submission, the operator will review your details and get back to you at the earliest. Thanks.",  font=("TimesNewRoman 10 bold"), height=2, width=87)
lbl_TourName.place(x=1, y=555)
root.mainloop()



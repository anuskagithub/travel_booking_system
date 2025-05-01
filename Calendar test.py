from tkinter import*
from tkcalendar import*

root=Tk()
root.tite(" Calender")
root.geometry("600*600")

cal=Calendar(root, selectmode="day", year=2020, month=5, day=22)
cal.packk(pady=20)
def grab_date():
    my_label.config(text="")
    
my_button=Button(root,text="get Date", command=grab_date)
my_button.pack(pady=20)

my_label=Label(root, text="")
my_label.pack(pady=20)    


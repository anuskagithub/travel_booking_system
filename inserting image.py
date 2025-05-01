from tkinter import *
from PIL import ImageTk,Image
root = Tk()
canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("D:/Anuska/Travel2021/Daily_Travel_Booking/travel.png"))
#img=img.resize(450,350),ImageANTIALIAS
canvas.create_image(20, 20, anchor="n", image=img)
root.mainloop()



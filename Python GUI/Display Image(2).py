from tkinter import *
from PIL import Image, ImageTk
a=Tk()

a.geometry("230x245")
# For .png images
# Photo=PhotoImage(file="2.png")

# for .jpg images

c=Image.open('2.jpg')
Photo=ImageTk.PhotoImage(c)

b=Label(image=Photo)

b.pack()
d=Label(text="Good Morning! Have a nice day",font="lucida 10 ")
d.pack()

a.mainloop()

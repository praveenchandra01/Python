from tkinter import *
root=Tk()
root.geometry("290x200")
def resize():
    w=width.get()
    h=height.get()
    root.geometry(f"{w}x{h}")

Label(root,text="Window Resizer",font="lucida 15 bold",fg="#25043d",pady=3).grid(column=2)

Label(root,text="Width ",font="lucida 15 bold",pady=4).grid(row=1,column=1)
Label(root,text="Height ",font="lucida 15 bold").grid(row=2,column=1)

width=StringVar()
height=StringVar()

widthentry=Entry(root,textvariable=width,borderwidth=2).grid(row=1,column=2)
heightentry=Entry(root,textvariable=height,borderwidth=2).grid(row=2,column=2)

Button(root,text="Apply",command=resize).grid(column=2)




root.mainloop()
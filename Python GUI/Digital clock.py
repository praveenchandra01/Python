from tkinter import *
# from tkinter.ttk import *
from time import strftime

root=Tk()
root.geometry("500x100")
root.iconbitmap("9.ico")
root.config(bg="black")
root.title("Digi-Clock")


def time():
    S=strftime("%I:%M:%S %p")
    l.config(text=S)
    l.after(1000,time)

l=Label(root,font="ds-digital 80 bold",bg="black",fg="cyan")
l.pack(anchor="center")
time()



root.mainloop()
from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("500x400")

def myfun():
    print("hey!")

def help():
    print("I will help you")
    a=tmsg.showinfo("help","I will help you")
    print(a)

def rate():
    print("Rate us")
    a=tmsg.askquestion("Rate us","Was your experince is good")
    if a=="yes":
        msg="Great, please Rate us on app store"
    else:
        msg="Thanks for your feedback"
    tmsg.showinfo("Experience",msg)


mainmenu=Menu(root)

m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="New",command=myfun)
m1.add_command(label="Save",command=myfun)
m1.add_separator()
m1.add_command(label="Save As",command=myfun)
m1.add_command(label="print",command=myfun)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m1)

m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="Copy",command=myfun)
m2.add_command(label="Paste",command=myfun)
m2.add_separator()
m2.add_command(label="Undo",command=myfun)
m2.add_command(label="Find",command=myfun)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)

m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="Help",command=help)
m3.add_command(label="Rate us",command=rate)

root.config(menu=mainmenu)
mainmenu.add_cascade(label="Help",menu=m3)





root.mainloop()
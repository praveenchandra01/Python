from tkinter import *
root=Tk()
root.geometry("400x300")
root.config(bg="white")

onImg=PhotoImage(file="ON.png")
offImg=PhotoImage(file="OFF.png")

btnstate=False

def switch():
    global btnstate
    if btnstate==True:
        a.config(text="DARK MODE : OFF",bg="white",fg="black")
        root.config(bg="white")
        b.config(image=offImg,bg="white",activebackground="white")
        btnstate=False
    else:
        a.config(text="DARK MODE : ON",bg="#363c45",fg="white")
        root.config(bg="#363c45")
        b.config(image=onImg,bg="#363c45",activebackground="#363c45")
        btnstate=True

a=Label(root,text="DARK MODE : OFF",bg="white",fg="black")
a.pack(side=TOP,anchor='ne')

b=Button(root,image=offImg,command=switch,borderwidth=0,pady=3,bg="white",activebackground="white")
b.pack(side=TOP,anchor='ne')
root.mainloop()
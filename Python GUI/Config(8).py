from tkinter import *
root=Tk()
root.geometry("400x300")

def something():
    a.config(text="how are you?")
    root.config(bg="grey")
    b.config(text="You have been configged",state=DISABLED)

# global a
a=Label(root,text="Hello everyone")
a.pack(pady=10)

b=Button(root,text="click me!",command=something)
b.pack()
root.mainloop()
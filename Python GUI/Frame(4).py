from tkinter import *
root=Tk()
root.geometry("655x355")
f1=Frame(root,bg="grey",borderwidth=1,relief=SUNKEN)
f1.pack(side=LEFT,fill=Y)
f2=Frame(root,bg="black",borderwidth=3,relief=SUNKEN)
f2.pack(side=TOP,fill=X)


l=Label(f1,text="Directories")
l.pack(padx=2)
l=Label(f2,text="Welcome to Sublime text")
l.pack(padx=2)

root.mainloop()
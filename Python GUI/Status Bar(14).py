from tkinter import *
root=Tk()
root.geometry("500x400")

def upload():
    statusvar.set("Busy..")
    sb.update()
    import time
    time.sleep(2)
    statusvar.set("Ready")
statusvar=StringVar()
statusvar.set("ready")

sb=Label(root,textvariable=statusvar,relief=SUNKEN,anchor="e")
sb.pack(side=BOTTOM,fill=X)

Button(root,text="Upload",command=upload).pack()


root.mainloop()
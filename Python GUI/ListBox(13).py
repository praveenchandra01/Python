from tkinter import *
root=Tk()
root.geometry("400x300")

def add():
    global i
    lbx.insert(ACTIVE,i)
    i+=1
i=0
lbx=Listbox(root)
lbx.insert(END,"Whats up!")
lbx.pack()

Button(root,text="Add item",command=add,pady=3).pack()


root.mainloop()
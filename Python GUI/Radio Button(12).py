from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("400x300")

def order():
    tmsg.showinfo("Your order",f"We have recieved your order for {var.get()}. Thanks for ordering")

# var=IntVar()
# var.set(4)
var=StringVar()
var.set("Shawrma")
Label(root,text="What would you have to like sir?",font="Lucida 19 bold").pack()

r=Radiobutton(root,text="Paratha",variable=var,padx=3,value="Paratha").pack(anchor="w")
r=Radiobutton(root,text="Chole Bhature",variable=var,padx=3,value="Chole Bhature").pack(anchor="w")
r=Radiobutton(root,text="Rajma Chawal",variable=var,padx=3,value="Rajma Chawal").pack(anchor="w")
r=Radiobutton(root,text="Shawrma",variable=var,padx=3,value="Shawrma").pack(anchor="w")

Button(root,text="Order now",command=order).pack()

# ItemList = [ 'Pizza', 'Biriyani', 'Fried Rice']
# for i, item in enumerate(ItemList):
#     Radiobutton(root, text= item,padx=14,variable=var, value=item).pack(anchor='w')
#     # Radiobutton(root, text= item,padx=14,variable=var, value=i+1).pack(anchor='w')
#
# Button(root,text="Order now",command=order).pack()

root.mainloop()
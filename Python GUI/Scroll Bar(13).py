from tkinter import *
root=Tk()
root.geometry("500x400")
root.title("Scroll Bar")

# For connecting scrollbar to a widget
# 1. widget(yscrollcommand = scrollbar.set)
# 2.scrollbar.config(command=widget.yview)

scrolbar=Scrollbar(root)
scrolbar.pack(side=RIGHT,fill=Y)

t=Text(root,yscrollcommand=scrolbar.set)
t.pack(fill="both")
scrolbar.config(command=t.yview)

# lbx=Listbox(root, yscrollcommand = scrolbar.set)
# for i in range(22):
#     lbx.insert(END,i)
# lbx.pack()
# scrolbar.config(command=lbx.yview)




root.mainloop()
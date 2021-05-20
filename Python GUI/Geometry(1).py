from tkinter import *
import os
a_root=Tk()
# ("width x height")
a_root.geometry("350x400")
a_root.iconbitmap(os.path.abspath("4.ico"))
a_root.title("MY GUI")# (width,height)
#a_root.config(bg="#433e54")
a_root.minsize(250,250)
a_root.maxsize(1200,900)
b_root=Label(text="Xeption")
# a_root.overrideredirect(1) #Hides title-bar
b_root.pack()

a_root.mainloop()



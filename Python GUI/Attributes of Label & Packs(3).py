from tkinter import *
root=Tk()
root.geometry("650x450")
root.title("My GUI")

# Important Label Options :
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"
# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

a=Label(text='''SPACE X \nSpace Exploration Technologies Corp. is an American aerospace manufacturer and 
             \nspace transportation services company headquartered in Hawthorne, California.
             \n It was founded in 2002 by Elon Musk with the goal of reducing space 
             \ntransportation costs to enable the colonization of Mars)''',
             bg="black",fg="white",padx=53,pady=54,font="comicsansms 11 bold",borderwidth=15,relief=RAISED)

# Important Pack options :
# anchor = "nw",ne,sw,se
# side = top, bottom, left, right
# fill
# padx
# pady

# a.pack(side=TOP,anchor='nw',fill=X)
a.pack(side=LEFT,fill=Y,padx=34,pady=34)


root.mainloop()
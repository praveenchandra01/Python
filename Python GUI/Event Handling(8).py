from tkinter import *
root=Tk()
def f1(event):
    print(f"You clicked the button at {event.x} and {event.y}")

def f2(event):
    x,y=event.x,event.y
    print(f"Position {x} and {y}")

root.geometry("500x500")

widget=Button(root,text="Click")
widget.pack()

# widget.bind('<Button-1>',f1)
widget.bind('<Double-1>',quit)
root.bind('<Motion>',f2)
root.mainloop()
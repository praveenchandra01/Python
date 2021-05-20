from tkinter import *
root=Tk()
root.geometry("655x333")
def hello():
    print("Hello world")
def time():
    print("11 : 11")

def date():
    print("22nd/november/2020")
def weather():
    print("Rainy")


frame=Frame(root,bg="black",relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")

# B1=Button(root,text="Press to start",activebackground="red",bg="black",command=hello)
# B1.pack(side=LEFT,padx=4,pady=2)

B1=Button(frame,text="Press to get Time",fg="black",command=hello)
B1.pack(side=LEFT,padx=4,pady=2)

B2=Button(frame,text="Press to get Time",fg="black",command=time)
B2.pack(side=LEFT,padx=4,pady=2)

B3=Button(frame,text="Press to get Date",fg="black",command=date)
B3.pack(side=LEFT,padx=4,pady=2)

B4=Button(frame,text="Press to get Weather",fg="black",command=weather)
B4.pack(side=LEFT,padx=4,pady=2)

root.mainloop()
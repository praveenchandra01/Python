from tkinter import *
root=Tk()
root.geometry("550x250")
# root.config(bg="#433e54")

def getvalues():
    f=open("File1.txt","a")
    # f=open("File1.csv","a")
    f.write(userentry.get())
    # f.write(",")
    f.write(" ")
    f.write(passentry.get())
    f.write("\n")
    f.close()
    userentry.delete(0,END)
    passentry.delete(0,END)
    # print(uservalue.get())
    # print(passvalue.get())
    print("Values Submited")
user=Label(root,text="Username",font="comicsansms 25 bold",pady=3)
password=Label(root,text="Password",font="comicsansms 25 bold",pady=4)

user.grid(row=0)
password.grid(row=1)

# variable classes in tkinter
# BooleanVar,DoubleVar,IntVar,StringVar

# uservalue=StringVar()
# passvalue=StringVar()

# userentry=Entry(root,textvariable=uservalue,font="comicsansms 25 bold")
# passentry=Entry(root,textvariable=passvalue,font="comicsansms 25 bold")

userentry=Entry(root,font="comicsansms 25 bold")
passentry=Entry(root,font="comicsansms 25 bold")

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text="Submit",command=getvalues).grid(row=3,column=0,pady=9)

root.mainloop()
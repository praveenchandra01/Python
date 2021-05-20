from tkinter import *
root=Tk()
root.geometry("500x300")

def getvals():
    print("Submitting Form")
    print(f"{nameentry.get(),phonevalue.get(),gendervalue.get(),paymentmodvalue.get(),emergencyvalue.get(),foodservicevalues.get()}")

    f=open("File2.txt","a")
    # f=open("File2.csv","a")
    f.write(f'{namevalue.get()},{phonevalue.get()},{gendervalue.get()},{paymentmodvalue.get()},{emergencyvalue.get()},{foodservicevalues.get()}\n')
    f.close()
    nameentry.delete(0,END)
    phoneentry.delete(0,END)
    genderentry.delete(0,END)
    paymententry.delete(0,END)
    emergencyentry.delete(0,END)
    foodservice.deselect()
# Heading
Label(root,text="Welcome to Shiv Travellers",font="comicsansms 19 bold",pady=9).grid(row=0,column=3)

# Text for our form
name=Label(root,text="Name")
phone=Label(root,text="Phone Number")
gender=Label(root,text="Gender")
paymentmode=Label(root,text="Payment Mode")
emergrncy=Label(root,text="Emergency Contact")

# Pack text for our form
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
paymentmode.grid(row=4,column=2)
emergrncy.grid(row=5,column=2)

# Tkinter variables for storing entries
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
paymentmodvalue=StringVar()
emergencyvalue=StringVar()
foodservicevalues=IntVar()

# Entry for our form
nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
paymententry=Entry(root,textvariable=paymentmodvalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)

# Packing the entries
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
paymententry.grid(row=4,column=3)
emergencyentry.grid(row=5,column=3)

# Checkbox
foodservice=Checkbutton(root,text="Want to prebook your meal",variable=foodservicevalues)
foodservice.grid(row=6,column=3,pady=3)

# Submit button
Button(root,text="Submit to Shiv Traverllers",command=getvals).grid(row=7,column=3)

root.mainloop()

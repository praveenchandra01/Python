from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("400x400")
def get_dollar():
    print(f"we have credited {slider.get()} dollars in your account")
    tmsg.showinfo("Amount Credited1",f"we have credited {slider.get()} dollars in your account")

Label(root,text="How many dollars do you want?").pack()
slider=Scale(root,from_=0, to=10 , orient=HORIZONTAL,tickinterval=5)
slider.set(2)
slider.pack()
Button(root,text="Get dollars",command=get_dollar).pack()

root.mainloop()
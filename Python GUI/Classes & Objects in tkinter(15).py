from tkinter import*

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x400")
    def statusbar (self):
        self.var=StringVar()
        self.var.set("Ready")
        self.Stb=Label(self,textvariable=self.var,relief=SUNKEN,anchor="e")
        self.Stb.pack(side=BOTTOM,fill=X)
    def click(self):
        print("Clicked")
    def button(self,a):
        Button(self,text=a,command=self.click).pack()

if __name__ == '__main__':

    MY=GUI()
    MY.statusbar()
    MY.button("Click me")
    MY.mainloop()
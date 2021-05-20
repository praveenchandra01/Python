from tkinter import*
import tkinter.messagebox as tmsg

def click(event=""):
    txt=event.widget.cget("text")
    if txt=="=":
        try:
            exp=E.get()
            res=eval(exp)
            E.delete(0,END)
            E.insert(0,res)
            return

        except Exception as e:
            tmsg.showerror("Error",e)

    E.insert(END,txt)
        
def All_Clear(event):
    E.delete(0,END)

def Backspace(event):
    exp=E.get()
    exp=exp[0:len(exp)-1]
    E.delete(0,END)
    E.insert(0,exp)

def onEnter(event):
    B10.config(bg="#fcac0f")

def onLeave(event):
    B10.config(bg="#a7abb0")

def onEnter_CE(event):
    B1.config(bg="#ff3838")

def onLeave_CE(event):
    B1.config(bg="#b6babf")




if __name__ == '__main__':

    root=Tk()
    root.geometry("280x400")
    root.minsize(280,390)
    root.maxsize(280,400)
    root.title("Calculator")
    root.iconbitmap("img/11.ico")
    


    E=Entry(root,font="Courier 35 bold",justify=RIGHT,bg="#cbd6d6",fg="#283542",borderwidth=0)
    E.pack(padx=3)

    Frame=Frame(root,bg="#b8cccf")
    Frame.pack(side=TOP)


    B1=Button(Frame,text="CE",width=7,height=3,font="lucida",padx=1,borderwidth=0,bg="#b6babf",fg="black",activebackground="#ff3838")
    B1.grid(row=0,column=1)

    x=PhotoImage(file="img/1.png")
    B2=Button(Frame,text="%",image=x,width=69,height=62,font="lucida",padx=2,borderwidth=0,bg="#b6babf",activebackground="#60d4e6")
    B2.grid(row=0,column=2)

    y=PhotoImage(file="img/2.png")
    B3=Button(Frame,text="-",image=y,width=69,height=62,font="lucida",padx=1,borderwidth=0,bg="#b6babf",activebackground="#60d4e6")
    B3.grid(row=0,column=3)

    Img=PhotoImage(file="img/3.png")
    B4=Button(Frame,text="<--",image=Img,width=69,height=62,borderwidth=0,bg="#b6babf",activebackground="#60d4e6")
    B4.grid(row=0,column=4)

    temp=1
    for i in range(1,4):
        for j in range(1,4):
            B=Button(Frame,text=str(temp),width=7,height=3,font="lucida",padx=1,activebackground="#b8cccf",borderwidth=0,bg="#b8cccf",fg="black")
            B.grid(row=i,column=j)
            temp+=1
            B.bind("<Button-1>",click)


    q=PhotoImage(file="img/4.png")
    B5=Button(Frame,text=".",image=q,width=60,height=50,font="lucida",padx=1,activebackground="#b8cccf",borderwidth=0,bg="#b8cccf")
    B5.grid(row=4,column=1)

    B6=Button(Frame,text="0",width=7,height=3,font="lucida",padx=1,activebackground="#b8cccf",borderwidth=0,bg="#b8cccf",fg="black")
    B6.grid(row=4,column=2)

    w=PhotoImage(file="img/5.png")
    B7=Button(Frame,text="/",image=w,width=60,height=60,font="lucida",padx=1,activebackground="#b8cccf",borderwidth=0,bg="#b8cccf")
    B7.grid(row=4,column=3)

    e=PhotoImage(file="img/6.png")
    B8=Button(Frame,text="+",image=e,width=69,height=70,font="lucida ",padx=1,borderwidth=0,bg="#b6babf",activebackground="#60d4e6")
    B8.grid(row=1,column=4)

    r=PhotoImage(file="img/7.png")
    B9=Button(Frame,text="*",image=r,width=69,height=70,font="lucida",padx=1,borderwidth=0,bg="#b6babf",activebackground="#60d4e6")
    B9.grid(row=2,column=4)

    t=PhotoImage(file="img/8.png")
    B10=Button(Frame,text="=",image=t,width=69,height=135,font="lucida",padx=1,borderwidth=0,activebackground="#fcac0f",bg="#a7abb0")
    B10.grid(row=3,column=4,rowspan=2)



    B1.bind("<Button-1>",All_Clear)

    B2.bind("<Button-1>",click)
    
    B3.bind("<Button-1>",click)

    B4.bind("<Button-1>",Backspace)
  

    B5.bind("<Button-1>",click)
    B6.bind("<Button-1>",click)
    B7.bind("<Button-1>",click)
    B8.bind("<Button-1>",click)
    B9.bind("<Button-1>",click)


    B10.bind("<Button-1>",click)
    B10.bind("<Enter>",onEnter)
    B10.bind("<Leave>",onLeave)

    
    B1.bind("<Enter>",onEnter_CE)
    B1.bind("<Leave>",onLeave_CE)


    root.mainloop()
    
from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def NewFile():
    global File
    root.title("Untitled - Notepad")
    File = None
    TextArea.delete(1.0, END)


def OpenFile(event=""):
    global File
    File = askopenfilename(defaultextension=".txt", filetypes=[
                           ("All files", "*.*"), ("Text Documents", "*.txt")])

    if File == "":
        File = None
    else:
        root.title(os.path.basename(File) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(File, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def SaveAsFile():
    global File
    # if File == None:
    File = asksaveasfilename(defaultextension=".txt", filetypes=[
                             ("All files", "*.*"), ("Text Documents", "*.txt")])

    if File == "":
        File = None
    else:
        # Save as a new file
        f = open(File, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
        root.title(os.path.basename(File) + " - Notepad")


def SaveFile(event=""):
    global File
    if File == None:
        File = asksaveasfilename(defaultextension=".txt", filetypes=[
                                 ("All files", "*.*"), ("Text Documents", "*.txt")])

        if File == "":
            File = None
        else:
            # Save as a new file
            f = open(File, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(File) + " - Notepad")
            File = None
    else:
        # save the file
        f = open(File, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
        File = None


def QuitApp():
    root.destroy()


def Cut(event=""):
    TextArea.event_generate("<<Cut>>")


def Copy(event=""):
    TextArea.event_generate(("<<Copy>>"))


def Paste(event=""):
    TextArea.event_generate(("<<Paste>>"))


def About():
    tmsg.showinfo("Notepad", "Created by Xeption")


def DarkMode():
    global var
    # print(f"{var.get()}")
    if var.get() == 0:
        TextArea.config(bg="white", fg="black")
        Statusbar.config(bg="white")
        l1.config(bg="white")
        l2.config(bg="white")

        # var=False
    else:
        TextArea.config(bg="#303742", fg="white")
        Statusbar.config(bg="#283542")
        l1.config(bg="#283542",fg="#90a0b0")
        l2.config(bg="#283542",fg="#90a0b0")
        # var=True


def Rate():

    a = tmsg.askquestion("Rate us", "Was your experince is good")
    if a == "yes":
        msg = "Great, please Rate us on app store"
    else:
        msg = "Thanks for your feedback"
    tmsg.showinfo("Experience", msg)

# def f1(event):
#     x,y=event.x,event.y
#     # print(f"Row :{x}, Column : {y}")
#     Label(Statusbar,text=f"Row :{event.x}, Column : {event.y}").pack()

# return x,y


if __name__ == '__main__':
    root = Tk()
    root.geometry("450x450")
    root.minsize(450,450)
    root.title("Untitled - Notepad")
    root.iconbitmap(os.path.abspath('6.ico'))
   


    TextArea = Text(root, font="Consolas 11", bg="white", fg="black")
    # TextArea.mark_set(INSERT, "%d.%d" % (1,1))
    TextArea.pack(expand=True, fill=BOTH)

    File = None

    Menubar = Menu(root)

    Filemenu = Menu(Menubar, tearoff=0)
    Filemenu.add_command(label="New", command=NewFile)
    Filemenu.add_command(label="Open", command=OpenFile)
    Filemenu.add_command(label="Save", command=SaveFile)
    Filemenu.add_command(label="Save As", command=SaveAsFile)

    Filemenu.add_separator()
    Filemenu.add_command(label="Exit", command=QuitApp)
    Menubar.add_cascade(label="File", menu=Filemenu)

    Editmenu = Menu(Menubar, tearoff=0)
    Editmenu.add_command(label="Cut", command=Cut)
    Editmenu.add_command(label="Copy", command=Copy)
    Editmenu.add_command(label="Paste", command=Paste)
    Menubar.add_cascade(label="Edit", menu=Editmenu)

    var = IntVar()

    Viewmenu = Menu(Menubar, tearoff=0)
    Viewmenu.add_checkbutton(label="Dark Mode", onvalue=1,
                             offvalue=0, variable=var, command=DarkMode)

    Menubar.add_cascade(label="View", menu=Viewmenu)

    Helpmenu = Menu(Menubar)
    Helpmenu.add_command(label="About Notepad", command=About)
    Helpmenu.add_command(label="Rate us", command=Rate)
    Menubar.add_cascade(label="Help", menu=Helpmenu)

    root.config(menu=Menubar)

    root.bind("<Control-o>",OpenFile)
    root.bind("<Control-s>",SaveFile)
    root.bind("<Control-x>",Cut)
    root.bind("<Control-c>",Copy)
    root.bind("<Control-v>",Paste)
    # root.bind("<Motion>",f1)

    Sy = Scrollbar(TextArea, width=15)
    Sy.pack(side=RIGHT, fill=Y)
    # Sx=Scrollbar(TextArea,orient=HORIZONTAL)
    # Sx.pack(side=BOTTOM,fill=X)
    TextArea.config(yscrollcommand=Sy.set)
    # TextArea.config(xscrollcommand=Sx.set,wrap=NONE)
    Sy.config(command=TextArea.yview)
    # Sx.config(command=TextArea.xview)

    Statusbar=Label(root,relief=FLAT,borderwidth=0,bg="white")
    Statusbar.pack(side=BOTTOM,fill=X)

    # f=Frame(Statusbar,borderwidth=1)
    # f.pack(side=RIGHT)

    # f2=Frame(Statusbar,borderwidth=1)
    # f2.pack(side=RIGHT)

    l1=Label(Statusbar,text="UFT-8",relief=FLAT,borderwidth=0,bg="white")
    l1.pack(side=RIGHT)
    l2=Label(Statusbar,text="Windows (CRLF)",relief=FLAT,borderwidth=0,bg="white")
    l2.pack(side=RIGHT)
    
    root.mainloop()
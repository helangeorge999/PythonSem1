from tkinter import *
from tkinter import messagebox
root = Tk()

def popup():
    response = messagebox.askyesno("This is my popup", "hello wrold")
    Label (root,text=response).pack()

    if response == 1:
        Label(root,text="Clicked Yes").pack()
    else:
        Label(root,text="Clicked No").pack()

btn = Button(root,text="Popup", command="popup").pack()
root.mainloop
from tkinter import *
from tkinter import messagebox
root = Tk ()

def popup():
    messagebox.showinfo("This is my Popup", "hello world")

btn = Button(root, text="popup", command = "popup").pack()
root.mainloop()
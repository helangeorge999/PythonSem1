from tkinter import *
window = Tk()
window.maxsize(width=600, height=400)
window.minsize(width=300,height=200)

def func():
    print("You are Logged in")

button = Button(window, text="Login", command=func)
button.pack(side="bottom")
window.mainloop()
from tkinter import *
win = Tk()

win.title('Main Window')
win.geometry("300x300")
win.eval('tk::PlaceWindow . Center')

Label(win, text="First name").grid (row=0)
Label(win, text="Last Name").grid (row=1)

e1= Entry(win)
e2= Entry(win)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

mainloop()
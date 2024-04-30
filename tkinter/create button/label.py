from tkinter import *
win=Tk()

win.eval('tk::PlaceWindow . center')
win.geometry("300x300")

w= Label(win, text='Helan George Adhikari')
w.pack()
win.mainloop()
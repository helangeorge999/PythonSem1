from tkinter import *
win=Tk()

win.title('Softwarica')
win.geometry("300x300")
win.eval('tk::PlaceWindow . center')

win.geometry("300x200")

w = Label(win, text='Softwarica', font='50')
w.pack()

sp= Spinbox(win, from_=0, to = 20)
sp.pack()

win.mainloop()
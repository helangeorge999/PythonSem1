from tkinter import *

win = Tk()
win.title('MainWindow')

#center your window
win.eval('tk::PlaceWindow . Center')

#creating a button in tkinter
button = Button(win, text='Click Button', height=30, width=50,  command=win.destroy)

button.pack()

win.mainloop()
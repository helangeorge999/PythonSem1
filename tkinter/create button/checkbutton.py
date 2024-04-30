from tkinter import*
win = Tk()

win.title('Main Window')
#center your window
win.eval('tk::PlaceWindow . Center')
variable1 = IntVar()
Checkbutton(win, text='male', variable=variable1).grid(row=0, sticky=W)
variable2 = IntVar()
Checkbutton (win, text='female', variable=variable2).grid(row=1, sticky=W)
mainloop()
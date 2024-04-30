from tkinter import *
win=Tk()
win.geometry("300x300")
frame= Frame(win)

frame.pack()

bottomframe= Frame(win)
bottomframe.pack( side = BOTTOM)

redbutton = Button(frame, text='Red', fg='red')
redbutton.pack(side=LEFT)

greenbutton = Button(frame, text='Green', fg='green')
greenbutton.pack(side=LEFT)

bluebutton = Button(frame, text=LEFT, fg='blue')
bluebutton.pack(side=LEFT)

blackbutton =  Button(bottomframe, text=BOTTOM, fg='black')
blackbutton.pack(side=BOTTOM)

win.mainloop()
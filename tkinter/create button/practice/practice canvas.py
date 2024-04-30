from tkinter import *

win = Tk()
win.title('George')

win.eval('tk::PlaceWindow . Center')

c = Canvas (win, bg='Green', height='300', width='300' )
oval = c.create_oval(200, 300, 50, 40, fill='white')
rectangle = c.create_rectangle(200, 90, 180, 50, fill='red')
line = c.create_line(200, 100, 10, 20, fill='black')
arc = c.create_arc(100, 80, 40, 30, fill='blue')

c.pack()
win.mainloop()
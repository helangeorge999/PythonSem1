from tkinter import *
win=Tk()
 
win.eval('tk::PlaceWindow . center')
win.geometry("400x300")

lb =Listbox(win)
lb.insert(1, 'Python')
lb.insert(2, 'Java')
lb.insert(3, 'C++')
lb.insert(4, 'C#')
lb.pack()

win.mainloop()
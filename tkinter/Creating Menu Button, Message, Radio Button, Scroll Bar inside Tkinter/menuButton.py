from tkinter import *

win= Tk()
win.title('Helan George')
win.geometry("300x300")

w = Label(win, text='Menu Setting', font="50")
w.pack()

win.eval('tk::PlaceWindow . center')

menubutton = Menubutton(win, text='Menu')

menubutton.menu = Menu(menubutton)
menubutton["menu"]=menubutton.menu

var1=IntVar()
var2=IntVar()
var3=IntVar()

menubutton.menu.add_checkbutton(label = "Setting", variable=var1)
menubutton.menu.add_checkbutton(label = "Language", variable=var2)
menubutton.menu.add_checkbutton(label = "Controls", variable=var3)

menubutton.pack()
mainloop()
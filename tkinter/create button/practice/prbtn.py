from tkinter import *

def on_button_click():
    print("Why are you gay?")


win= Tk()
win.title('Helan')

win.eval('tk::PlaceWindow . center')

button = Button(win, text="Don't click me !" ,height='30', width='50',  fg='Black', command=on_button_click)

button.pack()
win.mainloop()
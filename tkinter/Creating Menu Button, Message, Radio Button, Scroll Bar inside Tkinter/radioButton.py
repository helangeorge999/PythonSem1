from tkinter import*

def select():
    selection = "You selected the option" + str(var.get())
    label.config(text = selection)

win=Tk()
win.geometry("300x300")
win.eval('tk::PlaceWindow . center')

var = IntVar
R1=Radiobutton(win, text='Option 1', variable=var, value=1, command=select)
R1.pack(anchor=W)

R2=Radiobutton(win, text='Option 2', variable=var, value=2, command=select)
R2.pack(anchor=W)

R3=Radiobutton(win, text='Option 3', variable=var, value=3, command=select)
R3.pack(anchor=W)

label= Label(win)
label.pack()
mainloop()
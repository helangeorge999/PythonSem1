from tkinter import *
win = Tk()

win.geometry("300x300")
win.title('Helan George')
win.eval('tk::PlaceWindow . center')

text = Text(win)
text.insert(INSERT, 'Test')
text.insert(END, ' I m from Softwarica')
text.pack()

text.tag_add("test", "1.0", "1.4")
text.tag_add("test2", "1.14", "1.24")

text.tag_config("test", background='blue', foreground='white')
text.tag_config("test2", background='green', foreground='white')

win.mainloop()
from tkinter import *

win=Tk()
win.title('Message Box')
win.geometry("600x300")

win.eval('tk::PlaceWindow . center')

message = Message(win, text="Write anything you like....")
message.pack()
win.mainloop()
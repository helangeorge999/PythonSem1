from tkinter import*

win=Tk()
win.title('Main Window')
win.geometry("300x300")

win.eval('tk::PlaceWindow . center ')

scrollbar = Scrollbar(win)
scrollbar.pack(side=RIGHT, fill=Y)

mylist= Listbox(win, yscrollcommand=scrollbar.set)

for line in range(21):
    mylist.insert(END, "This is line number" +str(line))

mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview)

mainloop()
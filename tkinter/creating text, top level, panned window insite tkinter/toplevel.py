from tkinter import*

root = Tk()
root.geometry=('200x300')
root.title('Root window')

l= Label(root, text="This is root window")

top = Toplevel()
top.geometry('300x300')
top.title('Top Window')

l2=Label(top, text='This is Top Window')

l.pack()
l2.pack()

root.mainloop()
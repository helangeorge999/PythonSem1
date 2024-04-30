from tkinter import*

# creating a main window
root = Tk()

root.geometry('500x500')

frame = Frame(root)
frame.pack()

leftframe = Frame(root)
leftframe.pack(side = LEFT)

rightframe = Frame(root)
rightframe.pack(side = RIGHT)

#this function helps to show main window until u close
root.mainloop()
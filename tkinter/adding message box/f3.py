from tkinter import*

root = Tk()

root.geometry("400x400")
 
frame = Frame(root)
frame.pack()

leftframe = Frame(root)
leftframe.pack(side = LEFT)

rightframe = Frame(root)
rightframe.pack(side = RIGHT)

btn1 = Button (frame, text=("Button Red"))



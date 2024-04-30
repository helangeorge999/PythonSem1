from tkinter import *

# creating a main window
root = Tk()
root.geometry("400x400")

redButton = Button(root, text = "left", fg = "red")
redButton.pack(side = LEFT)

greenButton = Button(root, text = "right", fg = "green")
greenButton.pack(side = RIGHT)

blueButton = Button(root, text = "top", fg = "blue")
blueButton.pack(side = TOP)

blackButton = Button(root, text = "top", fg = "blue")
blackButton.pack(side = BOTTOM)

root.mainloop()
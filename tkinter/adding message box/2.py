from tkinter import*
from PIL import Image, ImageTk
root = Tk()
def open():
    global my_img
    top = Toplevel()
    my_img = ImageTk.PhotoImage(Image.open("icon.png"))
    my_label.pack = Label(top,image=my_img)
    my_label.pack(pady=10)
    btn.pack()
btnn = Button(root, text ="Open", command=open)
btnn.pack()
root.mainloop()
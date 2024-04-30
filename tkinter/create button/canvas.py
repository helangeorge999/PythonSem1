from tkinter import*
win = Tk()
win.title('Canvas')

#center your window
win.eval('tk::PlaceWindow . Center')
c = Canvas(win, bg="yellow", height=250, width=300)
line = c.create_line(108, 120, 320, 40, fill="green")
arc = c.create_arc(180, 150, 80, 210, start=0, extent=200, fill="red")
oval = c.create_oval(100, 30, 140, 150, fill="blue")

c.pack()
mainloop()

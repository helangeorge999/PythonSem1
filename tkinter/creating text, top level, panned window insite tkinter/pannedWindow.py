from tkinter import*
win=Tk()

win.title('Window')
win.geometry("300x300")
win.eval('tk::PlaceWindow . center')

paned_window=PanedWindow(win, orient=HORIZONTAL)
paned_window.pack(fill=BOTH, expand=True)

left_pane=Label(paned_window, text='Left pane', bg='Light Blue')
paned_window.add(left_pane)

right_pane=Label(paned_window, text='Right pane', bg='Light Green')
paned_window.add(right_pane)

mainloop()
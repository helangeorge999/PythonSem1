import tkinter as tk

def on_button_click():
    print("Suresh is gayyyyyy.....")

window = tk.Tk()
window.title("Button Example")

button = tk.Button(window, text="Who is gay??", command=on_button_click)

button.pack(padx=20, pady=20)

window.mainloop()

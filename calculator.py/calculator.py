# import tkinter as tk

# def on_click(value):
#     current = entry.get()
#     entry.delete(0, tk.END)
#     entry.insert(tk.END, current + str(value))

# def clear_entry():
#     entry.delete(0, tk.END)

# def calculate():
#     try:
#         result = eval(entry.get())
#         entry.delete(0, tk.END)
#         entry.insert(tk.END, str(result))
#     except Exception as e:
#         entry.delete(0, tk.END)
#         entry.insert(tk.END, "Error")

# # Create the main window
# app = tk.Tk()
# app.title("Calculator")

# # Entry widget for display
# entry = tk.Entry(app, width=16, font=("Arial", 20), borderwidth=5)
# entry.grid(row=0, column=0, columnspan=4)

# # Define buttons
# buttons = [
#       '1', '2', '3', '/',
#       '4', '5', '6', '*',
#       '7', '8', '9', '-',
#       '0', '.', '=', '+',
# ]

# # Add buttons to the grid
# row_val = 1
# col_val = 0
# for button in buttons:
#     tk.Button(app, text=button, padx=20, pady=20, font=("Arial", 16),
#               command=lambda b=button: on_click(b) if b != '=' else calculate()).grid(row=row_val, column=col_val)
#     col_val += 1
#     if col_val > 3:
#           col_val = 0
#           row_val += 1

# # Additional button for clearing the entry
# tk.Button(app, text="C", padx=20, pady=20, font=("Arial", 16), command=clear_entry).grid(row=row_val, column=col_val)

# # Run the main loop
# app.mainloop()
    

import tkinter as tk

def calculate(operation):
    num1 = float(entry.get())
    num2 = float(entry.get())
    
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"
    else:
        result = "Invalid operation"

    entry.delete(0, tk.END)
    entry.insert(tk.END, str(result))

# GUI setup
root = tk.Tk()
root.title("Calculator")

# Entry widget for display
entry = tk.Entry(root, width=20, borderwidth=5, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to handle button clicks

def Clear():
    entry.delete(0,tk.END)

def on_button_click(button):
    current_entry = entry.get()

    if button == '=':
        try:
            result = eval(current_entry)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, button)



# Button layout for numbers and operations
tk.Button(root, text='7', width=5, height=2, command=lambda: on_button_click('7')).grid(row=1, column=0, padx=5, pady=5)
tk.Button(root, text='8', width=5, height=2, command=lambda: on_button_click('8')).grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text='9', width=5, height=2, command=lambda: on_button_click('9')).grid(row=1, column=2, padx=5, pady=5)
tk.Button(root, text='/', width=5, height=2, command=lambda: on_button_click('/')).grid(row=1, column=3, padx=5, pady=5)

tk.Button(root, text='4', width=5, height=2, command=lambda: on_button_click('4')).grid(row=2, column=0, padx=5, pady=5)
tk.Button(root, text='5', width=5, height=2, command=lambda: on_button_click('5')).grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text='6', width=5, height=2, command=lambda: on_button_click('6')).grid(row=2, column=2, padx=5, pady=5)
tk.Button(root, text='*', width=5, height=2, command=lambda: on_button_click('*')).grid(row=2, column=3, padx=5, pady=5)

tk.Button(root, text='1', width=5, height=2, command=lambda: on_button_click('1')).grid(row=3, column=0, padx=5, pady=5)
tk.Button(root, text='2', width=5, height=2, command=lambda: on_button_click('2')).grid(row=3, column=1, padx=5, pady=5)
tk.Button(root, text='3', width=5, height=2, command=lambda: on_button_click('3')).grid(row=3, column=2, padx=5, pady=5)
tk.Button(root, text='-', width=5, height=2, command=lambda: on_button_click('-')).grid(row=3, column=3, padx=5, pady=5)

tk.Button(root, text='0', width=5, height=2, command=lambda: on_button_click('0')).grid(row=4, column=0, padx=5, pady=5)
tk.Button(root, text='.', width=5, height=2, command=lambda: on_button_click('.')).grid(row=4, column=1, padx=5, pady=5)
tk.Button(root, text='=', width=5, height=2, command=lambda: on_button_click('=')).grid(row=4, column=2, padx=5, pady=5)
tk.Button(root, text='+', width=5, height=2, command=lambda: on_button_click('+')).grid(row=4, column=3, padx=5, pady=5)
tk.Button(root, text='c', width=5, height=2, command=Clear).grid(row=5, column=4, padx=5, pady=5)
root.mainloop()

import tkinter as tk
from tkinter import messagebox

def login():
    entered_username = entry_username.get()
    entered_password = entry_password.get()

    # Add your authentication logic here (e.g., check credentials in a database)
    # For simplicity, I'll use a basic check
    if entered_username == 'admin' and entered_password == 'password':
        messagebox.showinfo("Login Successful", "Welcome, {}".format(entered_username))
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Login Page")

# Create and place widgets
label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=10)

label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)

login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Start the main loop
root.mainloop()

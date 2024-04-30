import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    feedback = feedback_entry.get("1.0", tk.END)
   

    messagebox.showinfo("Submission", f"Name: {name}\nAge: {age}\nGender: {gender}\nFeedback: {feedback}\nMarried: {married}")

root = tk.Tk()
root.title("Q&A Form")

# Name
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

# Age
age_label = tk.Label(root, text="Age:")
age_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Gender
gender_label = tk.Label(root, text="Gender:")
gender_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
gender_var = tk.StringVar(root)
gender_var.set("Male")
gender_menu = tk.OptionMenu(root, gender_var, "Male", "Female", "Other")
gender_menu.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Feedback
feedback_label = tk.Label(root, text="Feedback:")
feedback_label.grid(row=3, column=0, padx=10, pady=5, sticky="ne")
feedback_entry = tk.Text(root, height=5, width=30)
feedback_entry.grid(row=3, column=1, padx=10, pady=5, sticky="nw")

# #married
# married_label = tk.Label(root, text="Matrial Status:")
# married_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
# married_var = tk.StringVar(root)
# married_var.set("Single")
# married_menu = tk.OptionMenu(root, gender_var, "Married", "Single")
# married_menu.grid(row=2, column=1, padx=10, pady=5, sticky="w")


# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

root.mainloop()

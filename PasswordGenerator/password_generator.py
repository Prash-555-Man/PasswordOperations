import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4 characters.")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

tk.Label(root, text="Enter Password Length:").pack(pady=5)
entry = tk.Entry(root, width=10)
entry.pack(pady=5)

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=5)

root.mainloop()

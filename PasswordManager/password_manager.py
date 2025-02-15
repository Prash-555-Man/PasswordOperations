import tkinter as tk
from tkinter import messagebox, ttk
import random
import string
import os

# Password generator function
def generate_password():
    length = password_length.get()
    if not length.isdigit() or int(length) < 4:
        messagebox.showerror("Error", "Enter a valid password length (min 4)")
        return
    length = int(length)
    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = "".join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, generated_password)

# Save password function
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if not website or not username or not password:
        messagebox.showwarning("Warning", "All fields are required!")
        return

    with open("passwords.txt", "a") as file:
        file.write(f"{website} | {username} | {password}\n")
    
    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Password saved successfully!")

# View stored passwords
def view_passwords():
    if not os.path.exists("passwords.txt"):
        messagebox.showinfo("Info", "No saved passwords found.")
        return

    with open("passwords.txt", "r") as file:
        data = file.read()

    view_window = tk.Toplevel(root)
    view_window.title("Saved Passwords")
    view_window.geometry("400x300")

    text_area = tk.Text(view_window, wrap="word")
    text_area.insert(tk.END, data)
    text_area.config(state=tk.DISABLED)
    text_area.pack(expand=True, fill=tk.BOTH)

# UI Setup
root = tk.Tk()
root.title("Password Manager")
root.geometry("400x300")

# Labels
tk.Label(root, text="Website:").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Username:").grid(row=1, column=0, padx=10, pady=5)
tk.Label(root, text="Password:").grid(row=2, column=0, padx=10, pady=5)

# Entries
website_entry = tk.Entry(root, width=30)
website_entry.grid(row=0, column=1, padx=10, pady=5)

username_entry = tk.Entry(root, width=30)
username_entry.grid(row=1, column=1, padx=10, pady=5)

password_entry = tk.Entry(root, width=30)
password_entry.grid(row=2, column=1, padx=10, pady=5)

# Password Length Entry
tk.Label(root, text="Password Length:").grid(row=3, column=0, padx=10, pady=5)
password_length = tk.Entry(root, width=5)
password_length.grid(row=3, column=1, padx=10, pady=5, sticky="w")

# Buttons
tk.Button(root, text="Generate Password", command=generate_password).grid(row=3, column=1, padx=10, pady=5, sticky="e")
tk.Button(root, text="Save", command=save_password).grid(row=4, column=1, pady=10)
tk.Button(root, text="View Saved Passwords", command=view_passwords).grid(row=5, column=1, pady=10)

root.mainloop()
import tkinter as tk
from tkinter import messagebox, ttk
import random
import string
import os

# Password generator function
def generate_password():
    length = password_length.get()
    if not length.isdigit() or int(length) < 4:
        messagebox.showerror("Error", "Enter a valid password length (min 4)")
        return
    length = int(length)
    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = "".join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, generated_password)

# Save password function
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if not website or not username or not password:
        messagebox.showwarning("Warning", "All fields are required!")
        return

    with open("passwords.txt", "a") as file:
        file.write(f"{website} | {username} | {password}\n")
    
    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Password saved successfully!")

# View stored passwords
def view_passwords():
    if not os.path.exists("passwords.txt"):
        messagebox.showinfo("Info", "No saved passwords found.")
        return

    with open("passwords.txt", "r") as file:
        data = file.read()

    view_window = tk.Toplevel(root)
    view_window.title("Saved Passwords")
    view_window.geometry("400x300")

    text_area = tk.Text(view_window, wrap="word")
    text_area.insert(tk.END, data)
    text_area.config(state=tk.DISABLED)
    text_area.pack(expand=True, fill=tk.BOTH)

# UI Setup
root = tk.Tk()
root.title("Password Manager")
root.geometry("400x300")

# Labels
tk.Label(root, text="Website:").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Username:").grid(row=1, column=0, padx=10, pady=5)
tk.Label(root, text="Password:").grid(row=2, column=0, padx=10, pady=5)

# Entries
website_entry = tk.Entry(root, width=30)
website_entry.grid(row=0, column=1, padx=10, pady=5)

username_entry = tk.Entry(root, width=30)
username_entry.grid(row=1, column=1, padx=10, pady=5)

password_entry = tk.Entry(root, width=30)
password_entry.grid(row=2, column=1, padx=10, pady=5)

# Password Length Entry
tk.Label(root, text="Password Length:").grid(row=3, column=0, padx=10, pady=5)
password_length = tk.Entry(root, width=5)
password_length.grid(row=3, column=1, padx=10, pady=5, sticky="w")

# Buttons
tk.Button(root, text="Generate Password", command=generate_password).grid(row=3, column=1, padx=10, pady=5, sticky="e")
tk.Button(root, text="Save", command=save_password).grid(row=4, column=1, pady=10)
tk.Button(root, text="View Saved Passwords", command=view_passwords).grid(row=5, column=1, pady=10)

root.mainloop()

import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength(password):
    strength_criteria = [
        (r"[a-z]", "Lowercase letter"),
        (r"[A-Z]", "Uppercase letter"),
        (r"\d", "Digit"),
        (r"[@$!%*?&]", "Special character (@$!%*?&)")
    ]
    
    score = sum(1 for pattern, _ in strength_criteria if re.search(pattern, password))
    
    if len(password) < 6:
        return "Very Weak"
    elif score == 1:
        return "Weak"
    elif score == 2:
        return "Moderate"
    elif score == 3:
        return "Strong"
    elif score == 4 and len(password) >= 8:
        return "Very Strong"
    else:
        return "Moderate"

def analyze_password():
    password = entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password!")
        return
    
    strength = check_password_strength(password)
    result_label.config(text=f"Password Strength: {strength}")

# GUI Setup

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x200")
tk.Label(root, text="Enter Password:").pack(pady=5)
entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)
tk.Button(root, text="Check Strength", command=analyze_password).pack(pady=5)
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=5)
root.mainloop()


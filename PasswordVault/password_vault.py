import tkinter as tk
from tkinter import messagebox, simpledialog
import os
import json
from cryptography.fernet import Fernet

# ================================
# 🔑 ENCRYPTION SETUP
# ================================

# Encryption key file
KEY_FILE = "vault_key.key"
DATA_FILE = "vault_data.enc"

# Function to generate or load the encryption key
def load_or_generate_key():
    """Generates a new encryption key if not found, else loads existing one."""
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as key_file:
            return key_file.read()
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    return key

# Load encryption key
key = load_or_generate_key()
cipher = Fernet(key)

# Function to encrypt data
def encrypt_data(data):
    """Encrypts given text data using Fernet encryption."""
    return cipher.encrypt(data.encode()).decode()

# Function to decrypt data
def decrypt_data(data):
    """Decrypts given encrypted text data using Fernet."""
    return cipher.decrypt(data.encode()).decode()

# ================================
# 🔒 PASSWORD VAULT FUNCTIONS
# ================================

# Function to load vault data
def load_vault():
    """Loads encrypted password vault data and decrypts it."""
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "rb") as file:
        encrypted_data = file.read()
        if encrypted_data:
            try:
                return json.loads(decrypt_data(encrypted_data.decode()))
            except:
                return {}
    return {}

# Function to save vault data
def save_vault(data):
    """Encrypts and saves password vault data."""
    encrypted_data = encrypt_data(json.dumps(data))
    with open(DATA_FILE, "wb") as file:
        file.write(encrypted_data.encode())

# ================================
# 🔑 MASTER PASSWORD AUTHENTICATION
# ================================

# Define the master password (Change this for better security)
MASTER_PASSWORD = "admin123"

def authenticate():
    """Asks user for the master password before allowing access."""
    password = simpledialog.askstring("Authentication", "Enter Master Password:", show='*')
    if password != MASTER_PASSWORD:
        messagebox.showerror("Access Denied", "Incorrect Master Password!")
        root.destroy()

# ================================
# 🔐 PASSWORD MANAGEMENT FUNCTIONS
# ================================

def add_password():
    """Adds a new password entry to the vault."""
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if not website or not username or not password:
        messagebox.showwarning("Warning", "All fields are required!")
        return

    vault_data = load_vault()
    vault_data[website] = {"username": username, "password": password}
    save_vault(vault_data)

    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Password saved securely!")

def view_passwords():
    """Displays all saved passwords in a new window."""
    vault_data = load_vault()
    if not vault_data:
        messagebox.showinfo("Info", "No saved passwords found.")
        return

    view_window = tk.Toplevel(root)
    view_window.title("Saved Passwords")
    view_window.geometry("400x300")

    text_area = tk.Text(view_window, wrap="word")
    for site, credentials in vault_data.items():
        text_area.insert(tk.END, f"Website: {site}\nUsername: {credentials['username']}\nPassword: {credentials['password']}\n\n")
    text_area.config(state=tk.DISABLED)
    text_area.pack(expand=True, fill=tk.BOTH)

def search_password():
    """Searches for a stored password by website name."""
    website = website_entry.get()
    if not website:
        messagebox.showwarning("Warning", "Enter a website to search!")
        return

    vault_data = load_vault()
    if website in vault_data:
        credentials = vault_data[website]
        messagebox.showinfo("Password Found", f"Username: {credentials['username']}\nPassword: {credentials['password']}")
    else:
        messagebox.showwarning("Not Found", "No saved password for this website.")

# ================================
# 🖥️ GUI SETUP
# ================================

root = tk.Tk()
root.title("Password Vault")
root.geometry("400x300")

# Authenticate user before showing UI
authenticate()

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

# Buttons
tk.Button(root, text="Add Password", command=add_password).grid(row=3, column=1, pady=10)
tk.Button(root, text="View Saved Passwords", command=view_passwords).grid(row=4, column=1, pady=5)
tk.Button(root, text="Search Password", command=search_password).grid(row=5, column=1, pady=5)

# Run the Tkinter app
root.mainloop()

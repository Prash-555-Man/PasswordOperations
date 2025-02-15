# 🔐 Password Vault

## 📌 Description
The **Password Vault** is a secure password manager built using **Python** and **Tkinter**, with **encryption** provided by the `cryptography` library. It allows users to securely store, retrieve, and manage their passwords using a **master password** for authentication.

## ✨ Features
✅ **Master Password Authentication** – Ensures only authorized users can access the vault  
✅ **Encrypted Storage** – Uses `Fernet` encryption to store passwords securely  
✅ **Add, View, and Search Passwords** – Manage saved credentials easily  
✅ **Tkinter GUI** – Simple and user-friendly interface  

---

## 📥 Installation

### 1️⃣ **Install Python**  
Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### 2️⃣ **Install Dependencies**  
Run the following command to install the required library:  
```sh
pip install cryptography
```

### 3️⃣ **Run the Application**  
Execute the following command:  
```sh
python password_vault.py
```

---

## 🛠️ How It Works

### **🔑 Authentication**
- The app requires a **Master Password** to access the vault.
- You can **change the master password** in the script (`MASTER_PASSWORD` variable).

### **🔒 Secure Storage**
- The **encryption key** is stored in a file (`vault_key.key`).
- Passwords are stored in an **encrypted file** (`vault_data.enc`).

### **📜 Password Management**
1. **Add New Password** – Enter website, username, and password → Click **"Add Password"**  
2. **View Saved Passwords** – Click **"View Saved Passwords"** to see all stored credentials  
3. **Search Password** – Enter a website name and click **"Search Password"**  

---

## 🔐 Security Considerations
✔️ **Do not share the master password**  
✔️ **Use a strong master password** (avoid easy-to-guess words)  
✔️ **Back up the encryption key (`vault_key.key`)** – Without it, data cannot be recovered  
✔️ **Do not manually edit `vault_data.enc`** – It is encrypted  

---

## 🚀 Future Enhancements
🔜 **Biometric Authentication (Fingerprint Support)**  
🔜 **Hashing the Master Password for Added Security**  
🔜 **Cloud Storage for Secure Backup & Syncing**  

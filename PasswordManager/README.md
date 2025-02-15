# Secure Password Manager

## Description
The **Secure Password Manager** is a Python-based application that allows users to **store, retrieve, and manage passwords securely**. It uses **Fernet encryption** from the `cryptography` module to protect stored credentials. The program features a **Tkinter GUI**, making it user-friendly.

---

## Features
✅ **Secure Storage**: Encrypts passwords before saving.  
✅ **Password Generation**: Creates strong passwords.  
✅ **Retrieve Encrypted Passwords**: Decrypts passwords for user access.  
✅ **User-Friendly Interface**: Built using Tkinter.  

---

## 🔐 Encryption Details
- Uses **Fernet encryption** from the `cryptography` library.
- A **secret key (`secret.key`)** is generated for encryption & decryption.
- Passwords are **stored in an encrypted file (`passwords.enc`)**.

---

## Installation
### **1️⃣ Install Dependencies**
Ensure Python is installed, then install `cryptography`:
```sh
pip install cryptography
```

### **2️⃣ Run the Script**
```sh
python password_manager.py
```

---

## Usage
### **1️⃣ Add a New Password**
1. Enter:
   - **Website**
   - **Username**
   - **Password** (or generate one)
2. Click "**Save**" to store the password **securely**.

### **2️⃣ Generate a Password**
1. Enter the **desired password length**.
2. Click "**Generate Password**".
3. The generated password appears in the UI.

### **3️⃣ View Saved Passwords**
1. Click "**View Saved Passwords**".
2. Stored credentials are **decrypted** and displayed.

---

## Example Output
| Website   | Username | Encrypted Password (Stored) |
|-----------|----------|----------------------------|
| google.com | user123  | gAAAAABf@3… (encrypted)   |
| github.com | devuser  | xYzaq1!9R… (encrypted)   |

---

## 🔐 Security Considerations
- **Passwords are encrypted** before storage.
- **Keep the `secret.key` safe**—losing it means **you can't decrypt stored passwords**.
- **Avoid weak passwords** (minimum **8 characters** recommended).

---

## 🚀 Future Improvements
- Add **a master password** to control access.  
- Implement **search functionality** for saved credentials.  
- Create a **cloud sync option** for remote password access.  

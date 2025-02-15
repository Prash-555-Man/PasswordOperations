# 🔐 Secure Password Toolkit

A collection of **Python-based password management tools** with a **Tkinter GUI**:
1. **Password Vault** – Store and encrypt passwords securely  
2. **Password Generator** – Generate strong passwords instantly  
3. **Password Strength Checker** – Analyze password security  

---

# 🔑 1. Password Vault

## 📌 Description
The **Password Vault** is a secure password manager built using **Python** and **Tkinter**, with **encryption** provided by the `cryptography` library. It allows users to securely store, retrieve, and manage their passwords using a **master password** for authentication.

## ✨ Features
✅ **Master Password Authentication** – Ensures only authorized users can access the vault  
✅ **Encrypted Storage** – Uses `Fernet` encryption to store passwords securely  
✅ **Add, View, and Search Passwords** – Manage saved credentials easily  
✅ **Tkinter GUI** – Simple and user-friendly interface  

### 📥 Installation
1️⃣ **Install Python** ([Download Here](https://www.python.org/downloads/))  
2️⃣ **Install Dependencies**  
```sh
pip install cryptography
```
3️⃣ **Run the Application**  
```sh
python password_vault.py
```

### 🛠️ How It Works
- **🔑 Authentication:** Master password required to access the vault  
- **🔒 Secure Storage:** Encrypted passwords stored in `vault_data.enc`  
- **📜 Password Management:** Add, View, and Search saved credentials  

### 🚀 Future Enhancements
🔜 **Biometric Authentication (Fingerprint Support)**  
🔜 **Hashing the Master Password for Added Security**  
🔜 **Cloud Storage for Secure Backup & Syncing**  

---

# 🔑 2. Password Generator

## 📌 Description
The **Password Generator** creates secure and random passwords based on user-defined length. It ensures **strong password generation** by including a mix of uppercase and lowercase letters, digits, and special characters.

## ✨ Features
✅ **Customizable Length** – Choose password length  
✅ **Strong Passwords** – Uses uppercase, lowercase, numbers, and special characters  
✅ **User-Friendly Interface** – Tkinter-based GUI  
✅ **Error Handling** – Prevents invalid input  

### 📥 Installation
No additional dependencies are required beyond Python.

### 🛠️ How It Works
1. **Enter Password Length** – Specify the desired number of characters  
2. **Click "Generate Password"** – A strong password is created instantly  
3. **Copy & Use It Securely**  

### 📜 Example Output
| Input Length | Generated Password |
|-------------|-------------------|
| 8           | aB3$dFgH          |
| 12          | Xy1!z@R4qP9s      |
| 16          | P@2rT5v#Zx8qY!Ms  |

---

# 🔑 3. Password Strength Checker

## 📌 Description
The **Password Strength Checker** analyzes passwords and determines their security level (Weak, Medium, or Strong).

## ✨ Features
✅ **Real-time Password Strength Analysis**  
✅ **Checks for Length, Numbers, Symbols, and Uppercase/Lowercase Mix**  
✅ **Tkinter UI for Easy Input**  

### 🛠️ How It Works
1. **Enter a Password** – Type any password in the input box  
2. **Click "Check Strength"** – The system analyzes security level  
3. **Result is Displayed** – Shows whether the password is Weak, Medium, or Strong  

### 📜 Strength Criteria
✔ **Weak** – Less than 8 characters, lacks numbers/symbols  
✔ **Medium** – At least 8 characters, but missing variety  
✔ **Strong** – 12+ characters, includes numbers, symbols, and mixed-case letters  

---

# 🔐 Security Considerations
✔ **Use a Strong Master Password** – Avoid using common words  
✔ **Backup Your Encryption Key (`vault_key.key`)** – Needed for data recovery  
✔ **Do Not Manually Edit `vault_data.enc`** – It is encrypted  
✔ **Use a Password Manager for Complex Passwords**  

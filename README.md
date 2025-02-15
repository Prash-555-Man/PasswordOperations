# 🔐 Secure Password Toolkit

A collection of **Python-based password security tools** with a **Tkinter GUI**:
1. **Password Vault** – Securely store and encrypt passwords  
2. **Password Generator** – Generate strong passwords instantly  
3. **Password Strength Checker** – Analyze password security  
4. **Password Vulnerability Scanner** – Detect weak or commonly used passwords  

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

# 🔑 4. Password Vulnerability Scanner

## 📌 Description
The **Password Vulnerability Scanner** is a Python-based security tool that evaluates the strength of a password. It checks for **common weaknesses**, such as:  
✔️ Short passwords (less than 8 characters)  
✔️ Use of common weak passwords (e.g., "123456", "password")  
✔️ Lack of character variety (uppercase, lowercase, numbers, special symbols)  

The **Tkinter GUI** makes it easy to enter a password and instantly check its **security level**.

## ✨ Features
✅ **Real-time Password Strength Analysis**  
✅ **Checks for Commonly Used Weak Passwords**  
✅ **Character Variety Analysis** (Uppercase, Lowercase, Numbers, Special Characters)  
✅ **Tkinter UI for User-Friendly Interaction**  
✅ **Security Warnings for Weak Passwords**  

### 📥 Installation
1️⃣ **Install Python** ([Download Here](https://www.python.org/downloads/))  
2️⃣ **Install Dependencies**  
```sh
pip install requests
```
3️⃣ **Run the Application**  
```sh
python password_vulnerability_scanner.py
```

### 🛠️ How It Works
1. **Enter a Password** – Type your password into the input box.  
2. **Click "Check Password"** – The system will analyze its strength.  
3. **Results:**  
   - ✅ **STRONG** – Secure password  
   - ⚠️ **MEDIUM** – Needs improvement  
   - ❌ **WEAK** – Unsafe password  

### 📜 Example Output
| Password Input | Strength Level | Reason |
|---------------|---------------|--------|
| `123456`      | ❌ Weak        | Too common |
| `hello123`    | ❌ Weak        | Lacks uppercase & special characters |
| `P@ssw0rd!`   | ✅ Strong      | Good mix of characters |
| `AbC123!@#`   | ✅ Strong      | Excellent complexity |

---

# 🔐 Security Considerations
✔ **Use a Strong Master Password** – Avoid using common words  
✔ **Backup Your Encryption Key (`vault_key.key`)** – Needed for data recovery  
✔ **Do Not Manually Edit `vault_data.enc`** – It is encrypted  
✔ **Use a Password Manager for Complex Passwords**  

---

# 🚀 Future Enhancements
🔜 **Check passwords against online breached databases (Have I Been Pwned API)**  
🔜 **Suggest stronger password alternatives**  
🔜 **Advanced reporting with entropy analysis**  
🔜 **Biometric Authentication (Fingerprint Support)**  
🔜 **Cloud Storage for Secure Backup & Syncing**  

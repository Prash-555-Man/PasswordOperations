# Password Tools 

## Description
This project includes three essential **password management tools** built with Python and Tkinter:
1. **Password Generator**: Creates strong, random passwords.
2. **Password Strength Checker**: Analyzes password security.
3. **Secure Password Manager**: Stores, retrieves, and manages passwords **with encryption**.

Each tool is designed with a **Tkinter GUI** for ease of use.

---

## 1️⃣ Password Generator
### **Features**
- Generates **random and strong** passwords.
- Allows **customizable length**.
- Uses a mix of:
  - Uppercase & lowercase letters (A-Z, a-z)
  - Numbers (0-9)
  - Special characters (!@#$%^&*())
- Simple **Tkinter-based UI**.

### **Installation & Usage**
1. Run the script:
   ```sh
   python password_generator.py
   ```
2. Enter the **desired password length**.
3. Click "**Generate Password**".
4. The generated password appears in the UI.

### **Example Output**
| Input Length | Generated Password |
|-------------|-------------------|
| 8           | aB3$dFgH          |
| 12          | Xy1!z@R4qP9s      |

---

## 2️⃣ Password Strength Checker
### **Features**
- Analyzes a given password and classifies it as:
  - **Weak** (e.g., short or simple passwords)
  - **Moderate** (contains some complexity)
  - **Strong** (secure with numbers, symbols, and length)
- Provides **feedback for improvement**.
- **Tkinter GUI** for user-friendly interaction.

### **Installation & Usage**
1. Run the script:
   ```sh
   python password_strength_checker.py
   ```
2. Enter your **password** in the input field.
3. Click "**Check Strength**".
4. The app displays the security level of the password.

### **Example Analysis**
| Password   | Strength | Feedback |
|------------|----------|-----------|
| `12345`    | Weak     | Too short & predictable |
| `Abc@123`  | Moderate | Add more length & symbols |
| `Xy1!z@R4qP9s` | Strong | Secure password |

---

## 3️⃣ Secure Password Manager (with Encryption)
### **Features**
- Securely **stores passwords** in an encrypted format.
- **Generates** strong passwords.
- **Retrieves saved passwords** (with decryption).
- Uses **Fernet encryption** from the `cryptography` module.
- **Tkinter GUI** for user-friendly interaction.

### **Encryption Details**
- A **secret key** (`secret.key`) is generated and used to encrypt passwords.
- Encrypted passwords are stored in `passwords.enc` instead of plain text.
- **Fernet symmetric encryption** ensures secure storage.

### **Installation & Usage**
#### **1️⃣ Install Dependencies**
```sh
pip install cryptography
```

#### **2️⃣ Run the Script**
```sh
python password_manager.py
```

#### **3️⃣ Steps to Use**
1. Enter:
   - **Website**
   - **Username**
   - **Password** (or generate one)
2. Click "**Save**" to store credentials **securely**.
3. Click "**View Saved Passwords**" to retrieve **decrypted** credentials.

### **Example Output**
| Website   | Username | Encrypted Password (Stored) |
|-----------|----------|----------------------------|
| google.com | user123  | gAAAAABf@3… (encrypted)   |
| github.com | devuser  | xYzaq1!9R… (encrypted)   |

---

## 🔐 Security Considerations
- **All passwords are encrypted** before storage.
- **Master key (`secret.key`) must be protected** (Do not share it!).
- **Avoid using weak passwords** (minimum **8 characters** recommended).

## 🚀 Future Improvements
- Add **password search functionality**.
- Implement **a master password for extra security**.
- Create a **cloud storage option** for synced password access.

# Password Operation

## Description
This project includes two essential tools for password security:

1. **Password Generator**: A Python-based application that creates strong, random passwords based on user-defined length. It ensures security by including a mix of uppercase and lowercase letters, digits, and special characters. The program features a graphical user interface (GUI) using Tkinter, making it user-friendly and efficient.

2. **Password Strength Checker**: A tool that evaluates the strength of a given password based on various security criteria, such as length, character diversity, and complexity. It helps users create stronger passwords by providing feedback on their password's security level.

## Features
### Password Generator
- **Customizable Length**: Users can specify the desired password length.
- **Strong Password Generation**: The generated password includes:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special characters (!@#$%^&*(), etc.)
- **User-Friendly Interface**: Implements a Tkinter-based GUI.
- **Error Handling**: Provides alerts for invalid inputs, such as non-numeric entries or lengths below a minimum threshold.

### Password Strength Checker
- **Real-Time Analysis**: Checks password strength instantly.
- **Security Criteria**:
  - Length of the password.
  - Inclusion of uppercase, lowercase, numbers, and special characters.
  - Avoidance of common words and patterns.
- **Strength Classification**: Categorizes passwords as Very Weak, Weak, Moderate, Strong, or Very Strong.
- **GUI-Based Input**: Uses Tkinter to provide a simple interface for users.

## Installation
### Prerequisites
Ensure you have Python installed on your system. Tkinter is included in standard Python installations, so no additional installation is required.

### Steps to Install
1. Clone the repository or download the script files.
2. Ensure Python is installed on your system.
3. Run the scripts directly without any additional package installations.

## Usage
### Running the Password Generator
Execute the following command to launch the password generator GUI:
```sh
python password_generator.py
```
1. Enter the desired password length.
2. Click the "Generate Password" button.
3. A secure password will be displayed on the screen.

### Running the Password Strength Checker
Execute the following command to launch the password strength checker GUI:
```sh
python password_checker.py
```
1. Enter a password into the input box.
2. Click the "Check Strength" button.
3. The application will analyze the password and display its strength level.

## Code Explanation
The programs use the `random` and `string` modules to generate passwords and the `re` module to analyze password security.

### Password Generator
- Uses `random.choice()` to create a secure password from a pool of characters.
- Ensures diversity in characters for stronger passwords.

### Password Strength Checker
- Uses regular expressions (`re` module) to check password composition:
  - `[a-z]` for lowercase letters.
  - `[A-Z]` for uppercase letters.
  - `\d` for digits.
  - `[@$!%*?&]` for special characters.
- Assigns a strength level based on the presence of these components and password length.

## Example Output
### Password Generator
| Input Length | Generated Password |
|-------------|-------------------|
| 8           | aB3$dFgH          |
| 12          | Xy1!z@R4qP9s      |
| 16          | P@2rT5v#Zx8qY!Ms  |

### Password Strength Checker
| Password | Strength Level |
|----------|---------------|
| `12345`  | Very Weak     |
| `abcdef` | Weak         |
| `Abc123` | Moderate     |
| `Abc123!`| Strong       |
| `A1b2C3!@` | Very Strong |

## Security Considerations
- Always use strong, unique passwords for different accounts.
- Avoid using common words or predictable patterns.
- Use a password manager to store and manage passwords securely.
- Regularly update passwords to enhance security.

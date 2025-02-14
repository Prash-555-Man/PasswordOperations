# Password Strength Checker

## Overview
The Password Strength Checker is a Python program that evaluates the strength of a given password. It provides a graphical user interface (GUI) using Tkinter to help users assess their password security level.

## Features
- **Password Strength Analysis**: Evaluates passwords based on the following criteria:
  - Presence of lowercase letters
  - Presence of uppercase letters
  - Inclusion of numerical digits
  - Usage of special characters (@$!%*?&)
  - Minimum and recommended length checks
- **Strength Levels**:
  - Very Weak
  - Weak
  - Moderate
  - Strong
  - Very Strong
- **User-Friendly Interface**: Implements a simple GUI with an input field and a button to check password strength.

## Installation
### Prerequisites
Ensure you have Python installed on your system. Tkinter is included in standard Python installations.

### Steps to Install
1. Clone the repository (if applicable) or download the script.
2. Install required dependencies (Tkinter is built-in, so no additional installations are required).

```sh
pip install tk
```

## Usage
### Running the Program
Execute the following command to launch the GUI:
```sh
python password_checker.py
```

### How to Use
1. Enter your password into the text box.
2. Click the "Check Strength" button.
3. The application will analyze the password and display its strength.

## Code Explanation
The program utilizes regular expressions (`re` module) to analyze password composition. It checks for:
- Lowercase letters using `[a-z]`
- Uppercase letters using `[A-Z]`
- Digits using `\d`
- Special characters using `[@$!%*?&]`

A scoring system determines the strength level based on the presence of these elements and the overall length of the password.

## Example Output
| Password | Strength Level |
|----------|---------------|
| `12345`  | Very Weak     |
| `abcdef` | Weak         |
| `Abc123` | Moderate     |
| `Abc123!`| Strong       |
| `A1b2C3!@` | Very Strong |

## License
This project is open-source and available under the MIT License. Feel free to contribute and improve the tool!

# Password Generator Project

## Overview
The **Password Generator Project** is a Python-based tool designed to create secure, random passwords. Users can specify the desired number of letters, symbols, and numbers in their passwords, and the program generates a random combination of these elements to ensure a strong password.

---

## Features
- Generates highly secure passwords with a customizable mix of:
  - **Letters** (both uppercase and lowercase)
  - **Symbols** (e.g., `!`, `#`, `$`)
  - **Numbers** (0-9)
- Randomizes the order of characters to increase password security.
- User-friendly interface for easy customization.

---

## Requirements
This project requires **Python 3.x**. No additional libraries are needed as it uses Python's built-in `random` module.

---

## How to Use
1. Clone or download this repository to your local machine.
2. Open the project in your preferred Python IDE or text editor.
3. Run the script in a terminal or IDE.

### Steps to Generate a Password
1. Launch the program.
2. Enter the number of letters, symbols, and numbers you want in your password when prompted.
3. The program will generate a random password and display it.

---

## Example
```
Welcome to the PyPassword Generator!
How many letters would you like in your password?
6
How many symbols would you like?
2
How many numbers would you like?
3
Here is your password: qA9&cB8*kZ1
```

---

## Code Explanation
Below is a brief explanation of the key sections of the code:

### 1. Importing the `random` Module
The script uses Python's built-in `random` module to randomly select characters from predefined lists.

### 2. Defining Character Lists
The following lists define the pool of characters used to generate the password:
- `let`: Contains all uppercase and lowercase letters.
- `num`: Contains digits from 0 to 9.
- `sym`: Contains common special symbols.

### 3. Collecting User Input
The program prompts the user to specify the number of letters, symbols, and numbers they want in their password.

### 4. Generating Password Components
- **Letters**: A random selection of characters from `let`.
- **Symbols**: A random selection of characters from `sym`.
- **Numbers**: A random selection of characters from `num`.

### 5. Shuffling and Outputting the Password
The selected characters are combined into a list, shuffled to randomize their order, and displayed as the final password.

---

## Contributing
If you'd like to contribute to this project:
1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

---

## Acknowledgments
- Inspired by the need for secure and customizable password generation.
- Built using Python's `random` module for simplicity and efficiency.


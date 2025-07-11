🔐 Password Generator

A simple, customizable password generator written in Python. Choose between weak and strong password types and instantly generate a secure password — with the option to copy it straight to your clipboard!
✨ Features

    ✅ Generates weak (letters & digits only) or strong (includes symbols) passwords

    🚫 Removes confusing characters like l, 1, 0, and O for better readability

    🔒 Password length:

        Weak: 10 characters

        Strong: 20 characters

    📋 Optional clipboard copy with pyperclip

🛠️ Requirements

    Python 3.x

    pyperclip library for clipboard copy (install with: pip install pyperclip)

📦 How to Use

    Run the script:

python3 password_generator.py

Choose the strength:

How strong do you want your password:
weak = short and no punctuation
strong = long with punctuation

(Optional) Copy it to your clipboard:

    Copy to clipboard? (y/n)

🧠 Example Output

How strong do you want your password:
weak = short and no punctuation
strong = long with punctuation
strong
rY#T^eH$bK8=qGfAMV%Z
Copy to clipboard? (y/n): y
Password has been copied

📌 Notes

    The generator avoids ambiguous characters to reduce user confusion.

    Clipboard functionality only works if pyperclip is installed.

📄 License

MIT License — feel free to use, modify, and share!

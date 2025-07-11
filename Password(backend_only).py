import random
import string

chars = string.ascii_letters + string.digits + string.punctuation
chars = chars.replace('l', '')
chars = chars.replace('1', '')
chars = chars.replace('0', '')
chars = chars.replace('0', '')

chars_weak = string.ascii_letters + string.digits
chars_weak = chars_weak.replace('1', '')
chars_weak = chars_weak.replace('l', '')
chars_weak = chars_weak.replace('O', '')
chars_weak = chars_weak.replace('0', '')

while True:
    strength = input (""" 
    How strong do you want your password:
    weak = short and no punctuation
    strong = long with punctuation
    """)
    if strength not in "weak" "strong":
        print("please write weak or strong")
    else:
        break



password = ""
if strength == "weak":
    for letters in range(10):
        password +=  random.choice(chars_weak)
    print(password)
elif strength == "strong":
    for letters in range(20):
        password += random.choice(chars)
    print(password)

copy = input("Copy to clipboard? (y/n): ")
if copy == "y":
    import pyperclip
    pyperclip.copy(password)
    print("Password has been copied")
else:
    ("Have a good day. ")

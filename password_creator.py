import tkinter as tk
import random
import string
import requests

root = tk.Tk()

password_phrase = tk.IntVar()

def checker():
    if len(entry.get()) < 1 and password_phrase.get() == 3:
        result_label.config(text="Please enter a number.")
    else:
        generate_password()

def generate_password():
    if password_phrase.get() == 5:
        length = int(entry.get())
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for i in range(length))
        result_label.config(text=password)
        copy(password)
    elif password_phrase.get() == 4:
        response = requests.get("https://www.mit.edu/~ecprice/wordlist.10000")
        words = response.content.splitlines()
        word_list = [word.decode('utf-8') for word in words]
        password = '-'.join(random.choice(word_list) for i in range(2))
        password += "-"
        password_num = "".join(random.choice(string.digits) for i in range(2))
        password += str(password_num)
        result_label.config(text=password)
        copy(password)

def copy(password):
    root.clipboard_clear()
    root.clipboard_append(password)
    final_label.config(text="Copied to clipboard!")
    root.update()

root.title("CAA SD - Password Generator")
root.geometry("400x350")
#root.configure(bg='white')cd

label = tk.Label(root, text="Enter password length: (Number only)")
label.pack(pady=10)
#abel.configure(fg='black', bg='white')

entry = tk.Entry(root)
entry.pack(pady=10)
#entry.configure(fg="black", bg="white")

passphrase = tk.Radiobutton(root, text="Passphrase", variable=password_phrase, value=4)
passphrase.pack(pady=10)

password = tk.Radiobutton(root, text="Password", variable=password_phrase, value=5)
password.pack(pady=10)

generate_button = tk.Button(root, text="Generate", command=checker)
generate_button.pack(pady=10)
#generate_button.configure(fg="black", bg="white")

copy_button = tk.Button(root, text="Copy to clipboard", command=copy)

result_label = tk.Label(root, text="", wraplength=300, justify="center")
result_label.pack(pady=10)
#result_label.configure(fg="black", bg="white")

final_label = tk.Label(root, text="", justify="center", font=('Helvetica', 18, 'bold'))
final_label.pack(pady=10)

root.mainloop()
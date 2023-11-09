import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    password_label.config(text=password)
    
def on_exit():
    result = messagebox.showinfo("Thank You!", "Thank you for Using Password Generator")
    if result == "ok":
        root.destroy()

# Create the main root
root = tk.Tk()
root.geometry('400x200')
root.configure(bg='lightgray')
root.resizable(False,False)
root.title("Password Generator")

length_label = tk.Label(root, text="Password Length:", font=('Arial',10, 'bold'), background='lightgray')
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=('Arial',10, 'bold'), relief='raised', bg='green',fg='white', cursor='hand2')
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

password_entry = tk.Label(root, text="Generated Password : ", font=('Arial',10, 'bold'), bg='lightgray')
password_entry.grid(row=2, column=0, padx=10, pady=10)

password_label = tk.Label(root, text="",font=('Lucida',10, 'bold'), bg='yellow', relief='groove')
password_label.grid(row=2, column=1, padx=10, pady=10)

exit_button = tk.Button(root, text="Exit", bg='red', fg='black', relief='solid',font="Roboto 10 bold", command=on_exit, cursor='hand2')
exit_button.grid(row=3,column=0, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()

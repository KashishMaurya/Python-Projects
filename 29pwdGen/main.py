from tkinter import *
from tkinter import messagebox
import random
# import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pwd():
    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("0123456789")
    symbols = list("!#$%&()*+")

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if not website or not email or not password:
        messagebox.showerror(title="Error", message="Please fill out all fields.")
        return

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    data.update(new_data)

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    website_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_pwd():
    website = website_entry.get().strip()
    if not website:
        messagebox.showerror("Error", "Please enter a website to search.")
        return

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "No passwords have been saved yet.")
        return
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Error reading the data file.")
        return

    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
    else:
        messagebox.showerror("Not Found", f"No details found for {website}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")
lock_img = PhotoImage(file="image.png")  
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Labels
Label(text="Website:", bg="white").grid(row=1, column=0)
Label(text="Email/Username:", bg="white").grid(row=2, column=0)
Label(text="Password:", bg="white").grid(row=3, column=0)

# Entries
website_entry = Entry(width=27)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=45)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "kashish.social.18@gmail.com")  

password_entry = Entry(width=27)
password_entry.grid(row=3, column=1)

# Buttons
Button(text="Search", width=14, bg="white", command=find_pwd).grid(row=1, column=2)
Button(text="Generate Password", width=14, bg="white", command=generate_pwd).grid(row=3, column=2)
Button(text="Add", width=38, bg="white", command=save_data).grid(row=4, column=1, columnspan=2)

window.mainloop()

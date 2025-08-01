from tkinter import *
from tkinter import messagebox
import random
import pyperclip

#random Password Generator 
def generate_pwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols= [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# function to save data
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if website == "" or email == "" or password == "":
        messagebox.showerror(title="Error", message="Please fill out all fields.")
    else:
        is_ok = messagebox.askokcancel(title="Confirm", message=f"These are the details entered: \nEmail: {email} \nWebsite: {website} \nPassword: {password}\n\nIs it okay to save?")
        
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
            
# UI Setup

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="image.png")
canvas.create_image(100,100, image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ", bg="white")
website_label.grid(row=1, column=0)

website_entry = Entry(width=45)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username: ", bg="white")
email_label.grid(row=2, column=0)

email_entry = Entry(width=45)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "kashish.social.18@gmail.com")

password_label = Label(text="Password: ", bg="white")
password_label.grid(row=3, column=0)

password_entry = Entry(width=27)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", width=14, bg="white", command=generate_pwd)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=38, bg="white", command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
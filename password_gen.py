#   password_gen.py
# GUI allows user to input username/email as well as website and generate random password
# Upon clicking save, all fields are written locally to a .json file

from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    num_list = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = letters_list + symbols_list + num_list

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(f"{password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def create_txt():
    web_data = web_entry.get()
    email_data = email_name_entry.get()
    password_data = password_entry.get()
    new_data = {
        web_data: {
            "email": email_data,
            "password": password_data,
        }
    }
    if len(web_data) == 0 or len(password_data) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        # try to read
        try:
            with open("My_logs_and_passes.json", "r") as data:
                # Reading old data
                data_file = json.load(data)
        # If file not found to be read, write/create new file
        except FileNotFoundError:
            with open("My_logs_and_passes.json", "w") as data:
                # Saving updated data
                json.dump(new_data, data, indent=4)
        # Once the file is read, update
        else:
            # Updating old data with new data
            data_file.update(new_data)

            with open("My_logs_and_passes.json", "w") as data:
                json.dump(data_file, data, indent=4)
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)


# ------------------------------- FIND PASSWORD --------------------------------- #
def find_password():
    web_data = web_entry.get()
    email_data = email_name_entry.get()
    try:
        with open("My_logs_and_passes.json", "r") as data:
            data_file = json.load(data)
            password = data_file[web_data]["password"]
        if web_data in data_file:
            messagebox.showinfo(title=f"{web_data}", message=f"Email: {email_data}\nPassword: {password}")
    except FileNotFoundError:
        messagebox.showerror(title="Oops!", message="No data file found!")
    except KeyError:
        messagebox.showerror(title="No Data Found", message=f"No details for {web_data} exist")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Create logo
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Create website label
website_label = Label(text="Website:", font=("Arial", 13, "normal"))
website_label.grid(column=0, row=1)
# Create Email/Username: label
email_name_label = Label(text="Email/Username:", font=("Arial", 13, "normal"))
email_name_label.grid(column=0, row=2)
# Create Password label
password_label = Label(text="Password:", font=("Arial", 13, "normal"))
password_label.grid(column=0, row=3)

# Create website entry
web_entry = Entry(width=33)  # 35
web_entry.grid(column=1, row=1)
web_entry.focus()
# Create Email/User entry
email_name_entry = Entry(width=52)  # 35
email_name_entry.grid(column=1, row=2, columnspan=2)
email_name_entry.insert(0, "example@email.com")
# Password entry
password_entry = Entry(width=33)  # 21
password_entry.grid(column=1, row=3)

# Generate button
password_button = Button(text="Generate Password", width=15, command=generate_pass)
password_button.grid(column=2, row=3)
# Add button
add_button = Button(text="Save", width=44, command=create_txt)
add_button.grid(column=1, row=4, columnspan=2)
# Search button
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()

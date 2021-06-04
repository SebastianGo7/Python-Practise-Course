from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password_button_clicked():
    """function generates a new password for the user and also adds it to the clipboard"""

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(5, 7)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list = [password_list[char] + random.choice(symbols) for char in range(nr_symbols)]
    password_list = [password_list[char] + random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    """ function takes all the inputs of various fields and adds them to the database """

    website_entered = website_entry.get()
    website_entry.delete(0, END)

    login_name_entered = login_name_entry.get()

    password_name_entered = password_entry.get()
    password_entry.delete(0, END)

    if len(password_name_entered) == 0 or len(login_name_entered) == 0:
        # Check if password or website is left blank
        messagebox.showinfo(title="Error", message="Please fill in all the fields")

    else:

        # Asks user to confirm the login and password entered
        is_ok = messagebox.askokcancel(title="website_entered",
                                       message=f" These are the details entered: \nEmail: {login_name_entered} \n"
                                               f"Password:{password_name_entered}\nIs it ok to save?")

        if is_ok:
            with open("database.txt", "a") as data_file:
                data_file.write(f"{website_entered} | {login_name_entered} | {password_name_entered}\n")


# ---------------------------- UI SETUP ------------------------------- #


# Creation of Window
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# Creation of the canvas image background
canvas = Canvas(width=200, height=200)

lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Creating the labels, buttons and entries needed
# the parameter column span allows to have wider cells without disturbing the grid

# Creating the labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

login_name_label = Label(text="Email/Username:")
login_name_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Creating the buttons
generate_password_button = Button(text="Generate Password", command=generate_password_button_clicked)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", command=save, width=36)
add_button.grid(column=1, row=4, columnspan=2)

# Creating the entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

login_name_entry = Entry(width=35)
login_name_entry.grid(column=1, row=2, columnspan=2)
login_name_entry.insert(0, "maxmustermann@gmail.com")

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

window.mainloop()

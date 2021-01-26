# Imports
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# Constants
FONT = ("Arial", 20, "italic")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# generate password function
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    # using list comprehensio for the same code as above
    password_list += [random.choice(letters) for _ in range(nr_letters)]

    # print(password_list)
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    # implementing the above code using .join() method
    password = "".join(password_list)
    pwd_entry.insert(END, password)

    # using pyperclip to copy generated password into your clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# Creating a fucntion for Add buttoon
# 6
def fun_add():
    web = web_entry.get()
    email = email_entry.get()
    pwd = pwd_entry.get()

    # validation for empty values in entry
    if len(web) == 0 or len(pwd) == 0:
        messagebox.showinfo(title="OOPS", message="Please make sure you havent left any fields empty")
    else:
        # giving a popup/Messagebox
        # messagebox.showinfo(title="Title",message="Message")
        is_ok = messagebox.askokcancel(title=web, message=f"These are the deatils entered : \n Email: {email}"
                                                          f"\nPassword :{pwd} \n Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                data = f"\n{web} | {email} | {pwd}"
                file.write(data)
                web_entry.delete(0, END)
                pwd_entry.delete(0, END)


# def add_fun():
#     fun_add(web_entry.get(),email_entry.get(),pwd_entry.get())
#     web_entry.delete(0, END)
#     web_entry.insert(0, "")
#     email_entry.delete(0, END)
#     email_entry.insert(0, "")
#     pwd_entry.delete(0, END)
#     pwd_entry.insert(0, "")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
# Image Widget
logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=1)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)
# using Column Span
# canvas.grid(row=2,col=0,columnspan=2)

# Adding Input labels

# 1.1 Website Label
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

# 1.1 Website input
web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2)

# Get the coursor to this entry
web_entry.focus()

# 2.1 Email Label
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

# 2.1 Email Input
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)

# Adding default email in to the email_entry
email_entry.insert(0, "askvyas@gmail.com")

# 3.1 Password Label
pwd_label = Label(text="Password:  ")
pwd_label.grid(column=0, row=3)

# 3.2 Password input
pwd_entry = Entry(width=21)
pwd_entry.grid(column=1, row=3)

# 4 Generate Password Button
gen_pwd = Button(text="Generate Password", command=gen_password)
gen_pwd.grid(column=2, row=3)

# 5 AddButton
add_but = Button(text="Add", width=36, command=fun_add)
add_but.grid(column=1, row=4, columnspan=2)

window.mainloop()

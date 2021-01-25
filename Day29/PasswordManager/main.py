# Imports
from tkinter import *

# Constants
FONT = ("Arial", 20, "italic")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
# Creating a fucntion for Add buttoon
def fun_add(web,email,pwd):
    if web!="" and email !="" and pwd!="":
        with open("data.txt","w+"):
            data=f"{web} | {email} | {pwd}"
        
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
# Adding defaulot email in to the email_entry
email_entry.insert(END,text="askvyas@gmail.com")
# 3.1 Password Label
pwd_label = Label(text="Password:  ")
pwd_label.grid(column=0, row=3)
# 3.2 Password input
pwd_entry = Entry(width=21)
pwd_entry.grid(column=1, row=3)

# 4 Generate Password Button
gen_pwd=Button(text="Generate Password")
gen_pwd.grid(column=2,row=3)

# 5 AddButton
add_but=Button(text="Add",width=36)
add_but.grid(column=1,row=4,columnspan=2)

window.mainloop()

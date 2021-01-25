# Imports
from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)
# Image Widget
logo_img=PhotoImage(file="logo.png")
canvas=Canvas(width=200,height=200,highlightthickness=1)
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=1)
# using Column Span
# canvas.grid(row=2,col=0,columnspan=2)

#

window.mainloop()

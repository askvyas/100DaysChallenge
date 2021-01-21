# Tkinter GUI Programming
import tkinter
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)

# Label
my_label= tkinter.Label(text="I am a label",font=("Arial",24,"bold"))
my_label.pack()
my_label["text"]="New Text"
my_label.config(text="New Text2")

# Button
# def button_click():
#     my_label.config(text="Button got clicked")
# button = tkinter.Button(text="click me",command=button_click)
# button.pack(side="bottom")

# Entry
input=tkinter.Entry(width=10)
input.pack()
print(input.get())

def button_click():
    my_label.config(text=input.get())
button = tkinter.Button(text="click me",command=button_click)
button.pack(side="bottom")




window.mainloop()
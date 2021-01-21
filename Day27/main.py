# Tkinter GUI Programming
import tkinter
def button_click():
    my_label.config(text=input.get())
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)
# adding padding
window.config(padx=200,pady=20)
# Label
my_label= tkinter.Label(text="I am a label",font=("Arial",24,"bold"))

my_label["text"]="New Text"
my_label.config(text="New Text2")
# my_label.pack()
# Button
# def button_click():
#     my_label.config(text="Button got clicked")
# button = tkinter.Button(text="click me",command=button_click)
# button.pack(side="bottom")

# Entry
input=tkinter.Entry(width=10)
print(input.get())
#input.pack()


button = tkinter.Button(text="click me",command=button_click)
#button.pack(side="bottom")

# place layout manager in tkinter
# my_label.place(x=0,y=0)

# grid and pack cannot be mixed
# grid layout manager
my_label.grid(column=0,row=0)
button.grid(column=1,row=1)
input.grid(column=3,row=3)

button_n=tkinter.Button(text="Submit")
button_n.grid(column=2,row=0)
window.mainloop()
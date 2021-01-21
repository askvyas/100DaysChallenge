# Tkinter GUI Programming
import tkinter
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)

# Label
my_label= tkinter.Label(text="I am a label",font=("Arial",24,"bold"))
my_label.pack(side="left")



# use unlimited Arguments known as unlimited position arguments
def add(*args):
    sum=0
    for n in args:
        sum=sum+n
    print(sum)
add(1,2,3,4,5,6,7,8,10,11,1)
add(1,9)








window.mainloop()
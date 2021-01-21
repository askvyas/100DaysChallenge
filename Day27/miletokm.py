from tkinter import *

window=Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=200)
window.config(padx=20,pady=20)

label = Label(text="is equal to")
label.grid(column=1,row=2)
label.config(padx=10,pady=10)

minp=Entry(width=7)
minp.grid(column=3,row=1)

labelm = Label(text="Miles")
labelm.grid(column=4,row=1)



mink=Entry(width=7)
mink.grid(column=3, row=2)

labelk = Label(text="Kilometers")
labelk.grid(column=4,row=2)


def convert():
    n=int(minp.get())*1.6
    #mink.insert(END,n)
    mink.config(text=f"{n}")

sub=Button(text="Calculate",command=convert)
sub.grid(column=3,row=3)



window.mainloop()

from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

head_label=Label(text="Timer",font=(FONT_NAME, 50, "italic"))
head_label.config(bg=YELLOW,fg=GREEN,highlightthickness=0)
head_label.grid(column=1,row=0)

canvas=Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)

btn_strt = Button(text="Start",highlightthickness=0)
btn_strt.grid(column=0,row=2)


btn_rst = Button(text="Reset",highlightthickness=0)
btn_rst.grid(column=2,row=2)


tick_label=Label(text="✔")
tick_label.config(bg=YELLOW,fg=GREEN,highlightthickness=0)
tick_label.grid(column=1,row=3)
window.mainloop()
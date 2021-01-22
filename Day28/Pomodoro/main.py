from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_time():

    window.after_cancel(timer)
    head_label.config(text="Pomodoro")
    canvas.itemconfig(timer_text,text="00:00")
    tick_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_time():
    global reps
    reps+=1

    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    if reps%2 != 0:
        countdown(work_sec)
        head_label.config(text="Work", fg=GREEN)


    elif reps==8:
        countdown(long_break_sec)
        head_label.config(text="Break", fg=RED)
    elif reps%2==0 and reps!=8:
        countdown(short_break_sec)
        head_label.config(text="Break", fg=PINK)







# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    # format time in seconds to "00:00"
    global reps
    min = math.floor(count/60)
    sec=count%60
    if sec<=9:
        sec="0"+str(sec) # Dynamic typing
    canvas.itemconfig(timer_text,text=f"{min}:{sec}")

    if (count > 0):
        global timer
        timer=window.after(1000, countdown, count - 1)
    else:
        start_time()
        marks=""
        for _ in range(math.floor(reps/2)):
            marks+="✔"
        tick_label.config(text=marks)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


head_label = Label(text="Timer", font=(FONT_NAME, 50, "italic"))
head_label.config(bg=YELLOW, fg=GREEN, highlightthickness=0)
head_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text=canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



btn_strt = Button(text="Start", highlightthickness=0,command=start_time)
btn_strt.grid(column=0, row=2)

btn_rst = Button(text="Reset", highlightthickness=0,command=reset_time)
btn_rst.grid(column=2, row=2)

tick_label = Label(fg=GREEN,bg=YELLOW)
tick_label.grid(column=1, row=3)
window.mainloop()

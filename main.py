from tkinter import *
import math
import sv_ttk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
timer_label_text = "Timer"
timer_time_text = "00:00"


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=timer_time_text)
    timer_label.config(text=timer_label_text, foreground=GREEN)
    check_label.config(text="")
    start_button["state"] = "normal"
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_time():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1

    start_button["state"] = "disabled"

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        timer_label.config(text="Timer", foreground=GREEN)
        count_down(work_sec)
    elif reps == 2 or reps == 4 or reps == 6:
        timer_label.config(text="Break", foreground=PINK)
        count_down(short_break_sec)
    elif reps == 8:
        timer_label.config(text="Break", foreground=RED)
        count_down(long_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global check_mark

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_time()
        check_mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            check_mark += "✔"
        check_label.config(text=check_mark)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize(width=500, height=500)
window.maxsize(width=500, height=500)
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

photo = PhotoImage(file="tomato.png")

timer_label = Label(text=timer_label_text, foreground=GREEN, background=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224)
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text=timer_time_text, fill="white", font=(FONT_NAME, 30, "bold"))
canvas.config(background=YELLOW, highlightthickness=0)
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_time)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=3)

check_label = Label(text="", foreground=GREEN, background=YELLOW)
check_label.grid(column=1, row=4)

sv_ttk.set_theme("dark")
window.mainloop()
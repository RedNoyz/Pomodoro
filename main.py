from tkinter import *
import time
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

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_time():
    count_down(5)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize(width=500, height=500)
window.maxsize(width=500, height=500)
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

photo = PhotoImage(file="tomato.png")

timer_label = Label(text="Timer", foreground=GREEN, background=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224)
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.config(background=YELLOW, highlightthickness=0)
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_time)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset")
reset_button.grid(column=2, row=3)

check_label = Label(text="✔", foreground=GREEN, background=YELLOW)
check_label.grid(column=1, row=4)

random_button = Button(text="random button")
random_button.grid(column=1, row=5)


sv_ttk.set_theme("dark")
window.mainloop()
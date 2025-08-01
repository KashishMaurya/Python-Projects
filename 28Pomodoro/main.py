from tkinter import *
import math
import winsound  # Windows-only for beeping sound

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#43a85c"
YELLOW = "#fff47c"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# Reset the timer
def reset_timer():
    global timer, reps
    if timer is not None:
        window.after_cancel(timer)
        timer = None
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", fg=GREEN)
    tick_label.config(text="")
    reps = 0

# Start the timer
def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)
    else:
        label.config(text="Work", fg=GREEN)
        count_down(work_sec)

# Countdown mechanism
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    formatted_time = f"{count_min:02d}:{count_sec:02d}"
    canvas.itemconfig(timer_text, text=formatted_time)

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        # Play beep sound based on session
        try:
            if reps % 8 == 0:
                winsound.Beep(600, 700)  # Long break beep
            elif reps % 2 == 0:
                winsound.Beep(1000, 300)  # Short break beep
            else:
                winsound.Beep(1200, 500)  # Work session end beep
        except:
            pass  # In case sound fails (e.g., non-Windows)

        start_timer()
        marks = "🔪" * (reps // 2)
        tick_label.config(text=marks)

# UI Setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
label.grid(row=0, column=1)

canvas = Canvas(width=200, height=250, bg=YELLOW, highlightthickness=0)
try:
    tomato_img = PhotoImage(file="tomato.png")
    canvas.create_image(100, 125, image=tomato_img)
except Exception:
    pass  # If image is missing, skip
timer_text = canvas.create_text(103, 145, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

st_btn = Button(text="Start", highlightthickness=0, fg=GREEN, font=(FONT_NAME, 12, "bold"), command=start_timer)
st_btn.grid(row=2, column=0)

rt_btn = Button(text="Reset", highlightthickness=0, fg=GREEN, font=(FONT_NAME, 12, "bold"), command=reset_timer)
rt_btn.grid(row=2, column=2)

tick_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
tick_label.grid(row=3, column=1)

window.mainloop()

from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
all_checks = ""
reps = 0
timer = None


def reset_clicked():
    # This method stops the calling mechanism, resets the reps to 0 and deletes the checks
    global reps
    reps = 0
    global all_checks
    all_checks = ""
    checks_label.config(text="")
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text=f"00:00")
    window.after_cancel(timer)


def start_clicked():
    # This method starts the timer, it counts the reps of work successfully done adding checks to the gui
    # Depending on the current reps, it calculates whether there is a work or a break session now
    # And the main label is changed accordingly
    # This method keeps calling the method count_down(count) to keep the program running calling itself

    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Test seconds:
    # work_sec = 5
    # short_break_sec = 3
    # long_break_sec = 10

    global all_checks
    if reps > 2 and reps % 8 == 0:
        current_session = long_break_sec
        timer_label.config(text="Break", fg=RED)

        if reps > 1:
            all_checks += "✔"
            checks_label.config(text=all_checks)

    elif reps > 1 and reps % 2 == 0:
        current_session = short_break_sec
        timer_label.config(text="Break", fg=PINK)

        if reps > 1:
            all_checks += "✔"
            checks_label.config(text=all_checks)

    else:
        current_session = work_sec
        timer_label.config(text="Work", fg=GREEN)

    count_down(current_session)


def count_down(count):
    # Method takes seconds as an input, and transforms it to minutes:seconds
    # This Method calls the Functions count_down and start_clicked
    # This is one of the parts which keeps the program calling itself

    minutes_remaining = math.floor(count / 60)
    seconds_remaining = count % 60

    if seconds_remaining < 10:
        seconds_remaining = f"0{seconds_remaining}"

    canvas.itemconfig(timer_text, text=f"{minutes_remaining}:{seconds_remaining}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    elif count == 0:
        global reps
        start_clicked()


# Tkinter GUI creation:
# Creation of window
window = Tk()
window.title("Pomodoro technique")
window.config(padx=100, pady=50, bg=YELLOW)

# Creation of the tomato image background
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Creation of the labels and buttons needed
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 36, "normal"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", bg=YELLOW, command=start_clicked, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=YELLOW, command=reset_clicked, highlightthickness=0)
reset_button.grid(column=2, row=2)

checks_label = Label(text="", bg=YELLOW, fg=GREEN)
checks_label.grid(column=1, row=3)


window.mainloop()

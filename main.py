from tkinter import *
import math

# Variables
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# UI Setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW) # Configure the size and color of the window

title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
title_label.grid(column=1, row=0)

# Create a box called canvas inside the window to diplay the tomato image and the time text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) 
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(104, 112, image=tomato_img)
canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, bg=YELLOW)
start_button.grid(column=0, row=2)

# Display the reset button whcih resets the timer
reset_button = Button(text="Reset", highlightthickness=0, bg=YELLOW)
reset_button.grid(column=2, row=2)

check_marks = Label(text="✔", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=2)

window.mainloop()

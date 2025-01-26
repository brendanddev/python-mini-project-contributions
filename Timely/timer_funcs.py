""" 
"""

# Imports
import tkinter as tk
from tkinter import messagebox


is_running = False

# Starts the timer
def start_timer(input_entry, start_button, stop_button, timer_label):
    global is_running
    try:
        time_rem = int(input_entry.get()) # Retrieve user input
        start_button.config(state=tk.DISABLED) # Disable start button
        stop_button.config(state=tk.NORMAL) # Enable stop button
        is_running = True
        countdown(time_rem, timer_label, input_entry, start_button, stop_button)
    except Exception as e:
        print(e)
        messagebox.showwarning("Warning", "Please enter a valid integer number.")

# Stops the timer
def stop_timer(input_entry, start_button, stop_button, timer_label):
    global is_running
    start_button.config(state=tk.NORMAL) # Enable the start button
    stop_button.config(state=tk.DISABLED) # Disable stop button
    input_entry.delete(0, tk.END) # Clear the input entry
    is_running = False 
    timer_label.config(text="")

# Handles logic for decrementing and displaying time remaining
def countdown(time_rem, timer_label, input_entry, start_button, stop_button):
    if is_running and time_rem > 0:
        update_timer(time_rem, timer_label)
        timer_label.after(1000, countdown, time_rem - 1, timer_label, input_entry, start_button, stop_button) # Call function again after 1 second (1000 millis)
    elif time_rem == 0:
        if is_running:
            messagebox.showinfo("Done", "Time's up!")
            stop_timer(input_entry, start_button, stop_button, timer_label)


def update_timer(time_rem, timer_label):
    timer_label.config(text=f"{time_rem}")
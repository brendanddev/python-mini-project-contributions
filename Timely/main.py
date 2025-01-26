
""" 
"""

# Imports
import os
import tkinter as tk
from tkinter import messagebox
from display import setup_gui
from timer_funcs import start_timer, stop_timer, countdown, update_timer


# Root window
root = tk.Tk() 
root.title("Timer App")
root.geometry("300x200")

timer_label, input_entry, start_button, stop_button = setup_gui(root)


# Start button command
start_button.config(command=lambda: start_timer(input_entry, start_button, stop_button, timer_label))

# Stop button command
stop_button.config(command=lambda: stop_timer(input_entry, start_button, stop_button, timer_label))

root.mainloop()

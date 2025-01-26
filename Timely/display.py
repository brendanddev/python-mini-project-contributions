""" 

"""

# Imports
import os
import tkinter as tk
from tkextrafont import Font



def setup_gui(root):
    # Custom timer font
    path = os.path.join(os.getcwd(), "assets", "Technology-Bold.ttf")
    timer_font = Font(file=path, family="Technology", size=25)
    # Main label
    main_label = tk.Label(root, text="Timely", font=("Georgia", 25, "italic"))
    main_label.pack(pady=5)
    # Input entry
    input_entry = tk.Entry(root, width=10, font=timer_font)
    input_entry.pack(pady=5)
    # Frame for buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=5)
    # Start button
    start_button = tk.Button(button_frame, text="Start", font=("Georgia", 12), width=7, height=1,
                            bg="green", fg="white")
    start_button.pack(pady=5, side=tk.LEFT, padx=10)
    # Stop button
    stop_button = tk.Button(button_frame, text="Stop", font=("Georgia", 12), width=7, height=1,
                            bg="red", fg="white", state=tk.DISABLED) # Disabled by default
    stop_button.pack(pady=5, side=tk.RIGHT, padx=10)
    # Timer label
    timer_label = tk.Label(root, text=f"s", font=timer_font)
    timer_label.pack(pady=2)
    
    return timer_label, input_entry, start_button, stop_button
        

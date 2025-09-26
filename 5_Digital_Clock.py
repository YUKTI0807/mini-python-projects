# 5. Digital Clock
# Concepts: Tkinter GUI, time module
# What to build:
# Create a small window
# Show live time (HH:MM:SS)
# Extra challenge: Add date & AM/PM indicator.

import tkinter as tk
import time
from time import strftime

root = tk.Tk()	
root.title("Digital Clock with Date")

label_t = tk.Label(root, font=("Arial", 50), fg="blue")
label_t.pack()

label_d = tk.Label(root, font=("Arial", 40), fg="green")
label_d.pack()


def timexyz():
	c_time = time.strftime("%H : %M : %S %p")
	c_date = time.strftime("%d-%m-%Y")

	label_t.config(text = c_time)
	label_d.config(text = c_date)
	
	root.after(1000, timexyz)

timexyz()
root.mainloop()

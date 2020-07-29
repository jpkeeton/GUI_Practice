import tkinter as tk
from tkinter import *

# Import of Tkinter module

window = tk.Tk()

# Creates the window from the imported Tkinter module
window.geometry("600x400")

# Creates the size of the window

window.title('antherTkinterTry.py')
# Adds a title to the Windows GUI for the window

# greeting won't show up cuz i've not placed it, only created it here...
greeting = tk.Label(text="Hello, Tkinter")

window.mainloop()
# Loops the window to prevent the window from just "flashing once"

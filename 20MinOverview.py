# Going thru this one - https://www.youtube.com/watch?v=_lSNIrR1nZU

from tkinter import *


# Add the click option
def click():
    """grab the entered text function"""
    entered_text = textBox.get()
    output.delete(0.0, END)
    try:
        definition = terms[entered_text]
    except:
        definition = "sorry, not finding that"
    output.insert(END, definition)


# Create the window
window = Tk()
window.geometry("500x500")
# Add a window title
window.title("Software Testing Glossary Test")

# CREATE THE WINDOW
# Configure the window
window.configure(background='light grey')

# PHOTO
# Create a photo variable
photo1 = PhotoImage(file="C:/Users/jpkee/Pictures/SoftwareBug.png")
# pack(anchor='center')
# Add the photo to the window, and use the grid bit to set the location
Label(window, image=photo1, bg="black").grid(row=1, column=0, sticky=E)
# .resize(30,30)

# Add some text
Label(window, text="Welcome to the Software Test").grid(row=0, column=0, sticky=N)

# Create a text entry box
textBox = Entry(window, width=30, bg="white")
textBox.grid(row=3, column=0, sticky=W)

# Add a submit button
Button(window, text="Check ", width=4, command=click).grid(row=4, column=0, sticky=W)
# don't forget to add the click bit, see above


# Print out the definition
Label(window, text="Definition:", bg='light gray', fg='green', font='none 12 bold').grid(row=5, column=0, sticky=W)

# Create a text box for the definition
output = Text(window, width=75, height=6, wrap=WORD, bg="white")
# I created above, now place it below
output.grid(row=6, column=0, sticky=W)

# Create the dictionary
terms = {'test case': 'the actual steps needed to verify a piece of functionality',
         'bug': 'a problem',
         'test plan': 'the document outlining your process'}

# close the window closing label
# Label(window, text="Exit", bg='light gray', fg='green', font='none 12 bold').grid(row=6, column=0, sticky=W)


# Close the Window function
def close_window():
    window.destroy()
    exit()

# close the window button
Button(window, text='Quit', width=10, command=close_window).grid(row=7, column=0, sticky=W)








# MAINLOOP
window.mainloop()

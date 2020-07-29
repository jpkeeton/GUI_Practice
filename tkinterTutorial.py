# https://www.youtube.com/watch?v=YXPyB4XeYLA

# for Python 3.x it's imported as ‘tkinter’
from tkinter import *

window = Tk()
window.geometry("500x500")


# Add a window title
# window.title("Software Testing Glossary Test")
# create a label widget
# Everything is a widget!


# Create a click function
def myClick1():
    myLabel = Label(window, text='this just got clicked!', command=myClick1)
    myLabel.pack()


# myLabel = Label(window,
#                 text="Software Testing Quiz", command=click)
#
# # create a button
# myButton = Button(window, text="Click me!")
# # put the button in the window
# myButton.pack()

# add a state, such as disabled
# myButton2 = Button(window, text="don't click me", state=DISABLED)


# try out the padx and pady
# myButton2 = Button(window, text="testing out the padding",
#                    state=DISABLED,
#                    padx=50,
#                    pady=50)
# add the buttons to the window

# myButton2.pack()
# # myButton3.pack()

def myClick2():
    myLabel2 = Label(window, text='this is the 2nd click')
    myLabel2.pack()


myButton5 = Button(window, text='this is button 5', command=myClick2)
myButton5.pack()

# mainloop is used to run the application
# waits for events
# processes the event when they occur
# ... as long as the window is not closed of course
window.mainloop()

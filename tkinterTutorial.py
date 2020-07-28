# https://www.youtube.com/watch?v=YXPyB4XeYLA

# for Python 3.x it's imported as ‘tkinter’
from tkinter import *

root = Tk()

# create a label widget
# Everything is a widget!
myLabel = Label(root,
                text="Software Testing QuizSoftware Testing QuizSoftware Testing QuizSoftwa\n re Testing QuizSoftware "
                     "Testing QuizSoftware Testing QuizSoftware Testing Quiz")

# there are 3 main geometry manager classes
# 1. Pack
# 2. Grid
# 3. Place


myLabel.pack()

# mainloop is used to run the application
# waits for events
# processes the event when they occur
# ... as long as the window is not closed of course
root.mainloop()

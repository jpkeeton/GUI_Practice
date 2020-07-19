from tkinter import *

master = Tk()
# myLabel1= Label(master, text="Welcome to the Quiz").grid(row=0)
# myLabel2= Label(master, text="My name is JeremyPK").grid(row=1)
# Label(master, text="First Name").grid(row=2)
# Label(master, text="Last Name").grid(row=3)
#
# #
# e1 = Entry(master)
# e2 = Entry(master)
#
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)



# creating a function for the button
def hierKlicken():
    newButtonLabel = Label(master, text ="For Today's #100DaysOfCode I learned more tkinter, \n the pack and grid methods\n and working with buttons. \n Super fun stuff!")
    newButtonLabel.pack()


# Buttons, which like everything else in tkinter are also widgets
# create the button
# a disabled button
# myButton = Button(master, text="click here!", state=DISABLED)
# changing the button size with padx and pady
# myButton = Button(master, text="click here!", padx=50, pady=30)

newButton = Button(master, text = "What's did you code today?", command=hierKlicken)
newButton.pack()


#learn how to change the default window size upon open

    




newButton.pack()


mainloop()
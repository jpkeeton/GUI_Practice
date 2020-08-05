# https://pysimplegui.readthedocs.io/en/latest/

import PySimpleGUI as sg

# layout = [[sg.Combo(['choice 1', 'choice 2', 'choice 3'], enable_events=True, key='combo')],
#           [sg.Button('Test'), sg.Exit()]
#           ]
#
# window = sg.Window('combo test', layout)
#
# while True:
#     event, values = window.Read()
#     if event is None or event == 'Exit':
#         break
#
#     if event == 'Test':
#         combo = values['combo']  # use the combo key
#         print(combo)
#
# window.Close()

#
# layout = [
#     sg.Combo
#     [sg.Text('Please enter your Name, Address, Phone')],
#     [sg.Text('Name', size=(15, 1)), sg.InputText()],
#     [sg.Text('Address', size=(15, 1)), sg.InputText()],
#     [sg.Text('Phone', size=(15, 1)), sg.InputText()],
#     [sg.Submit(), sg.Cancel()]
# ]
#
# window = sg.Window('Simple data entry window', layout)
# event, values = window.read()
# window.close()
# print(event, values[0], values[1], values[2])
#


# <>>
import PySimpleGUI as sg

# create a tuple of choices
choices = ('Software Problem', 'Food Opportunity!', 'A Feature')

# here is a layout definition
# layout = [  [sg.Text('What is your favorite color?')],
# create a layout
layout = [[sg.Text('What is a bug?')],
          [sg.Listbox(choices, size=(29, len(choices)), key='-COLOR-')],
          [sg.Button('This is button')]]

# Create a window
# window = sg.Window('Choose your answer wisely', layout)
window2= sg.Window('this is the 2nd window', layout)

# so this looks like the mainloop from tkinter
while True:  # the event loop
    event, values = window2.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Ok':
        if values['-COLOR-']:  # if something is highlighted in the list
            sg.popup(f"You chose {values['-COLOR-'][0]}")

window2.close()

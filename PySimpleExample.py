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

choices = ('Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple', 'Chartreuse')

layout = [[sg.Text('What is your favorite color?')],
          [sg.Listbox(choices, size=(15, len(choices)), key='-COLOR-')],
          [sg.Button('Ok')]]

window = sg.Window('Pick a color', layout)

while True:  # the event loop
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Ok':
        if values['-COLOR-']:  # if something is highlighted in the list
            sg.popup(f"Your favorite color is {values['-COLOR-'][0]}")
window.close()

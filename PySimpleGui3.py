# create your import
import PySimpleGUI as sg

# create a tuple to fill into the list box

# create the layout with some text, an input box and a button
layout = [[sg.Text('OK?')],
          [sg.Input(key='-INPUT-')],
          [sg.Button('OK'), sg.Button('Just.. NOT ok')]
          ]
sg.theme('light')


# create a window in which to stick the layout
window = sg.Window('Persistent Window', layout)

# create a loop to actually display the window
# calling window.read displays the window on the screen if it's not been displayed
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break

# close the window
window.close()





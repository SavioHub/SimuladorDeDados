import PySimpleGUI as sg

# Define the window's contents
layout = [
    [sg.Text("Jogar dado?")],
    [sg.Text(size=(40, 1), key='-OUTPUT-')],
    [sg.Button('sim'), sg.Button('não')]
]

# Create the window
window = sg.Window('Simulador de dado', layout)

# Display and interact with the Window using an Event Loop
while True:
    event = values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] +
                              "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()

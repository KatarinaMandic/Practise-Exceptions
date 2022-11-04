import PySimpleGUI as sg

sg.theme('DarkAmber')   
layout = [  
    [sg.Text('Name', size=(15,1)),
    sg.InputText()],
    [sg.Text('Year of birth', size=(15,1)), 
    sg.InputText()],
    [sg.Text('E-mail', size=(15,1)), 
    sg.InputText()],
    [sg.Text('Password', size=(15,1)), 
    sg.InputText()],
    [sg.Text('Confirm password', size=(15,1)),
    sg.InputText()],
    [sg.Text('', size=(15,1)), 
    sg.Button('Registration')],
]


window = sg.Window('Registration Form', layout, font = ('Arial', 16))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED : 
        break
    

window.close()
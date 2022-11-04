import PySimpleGUI as sg
from registration.Validation import Validation

sg.theme('DarkAmber')   
layout = [  
    [sg.Text('Name', size=(15,1)),
    sg.InputText(key = '_NAME_')],
    [sg.Text('Year of birth', size=(15,1)), 
    sg.InputText(key = '_YEAR_')],
    [sg.Text('E-mail', size=(15,1)), 
    sg.InputText(key = '_EMAIL_')],
    [sg.Text('Password', size=(15,1)), 
    sg.InputText(key = '_PASSWORD_')],
    [sg.Text('Confirm password', size=(15,1)),
    sg.InputText(key = '_CONFIRMEDPASSWORD_')],
    [sg.Text('', size=(15,1)), 
    sg.Button('Registration')],
]


window = sg.Window('Registration Form', layout, font = ('Arial', 16))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED : 
        break
    if event == 'Registration':
        try:
            # Data validation
            Validation.check_password(values['_PASSWORD_'], values['_CONFIRMEDPASSWORD_'])
            Validation.check_year(values['_YEAR_'])
            # Code for registration
            sg.popup('Successful Registration', font = ('Arial', 16))
        except Exception as ex:
            sg.popup_error(str(ex), title='Error', font = ('Arial', 16))
    

window.close()
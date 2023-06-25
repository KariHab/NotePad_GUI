import PySimpleGUI as sg


sg.theme('DarkTanBlue')
# All the stuff inside your window.

tasks = []
list_tasks = sg.Listbox(tasks, size=(50, 4), font=('Arial Bold', 12), expand_y=True, enable_events=True, key='-LIST-')
layout = [[sg.Input(size=(20, 1), font=('Arial Bold', 12), expand_x=True, key='-INPUT-', do_not_clear=False)],
    [list_tasks],
    [sg.Button('Add'), sg.Button('Remove'), sg.Button('Save'), sg.Button('Exit')],
    [sg.Text("", key='-MSG-', font=('Arial Bold', 12), justification='center')]
]


window = sg.Window('Empty your mind', layout, finalize=True, size=(600, 400))
window['-INPUT-'].bind('<Return>', "_Enter")
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': 
        break
    elif event == '-INPUT-' + "_Enter":
        tasks.append(values['-INPUT-'])
        window['-LIST-'].update(tasks)
    elif event == 'Add':
        tasks.append(values['-INPUT-'])
        window['-LIST-'].update(tasks)
    elif event == 'Remove':
        item = list_tasks.get()[0]
        tasks.remove(item)
        window['-LIST-'].update(tasks)
        msg = "Task removed : {}".format(item)
        window['-MSG-'].update(msg)
window.close()

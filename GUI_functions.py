import PySimpleGUI as sg
import os
import pickle

script_path = os.path.dirname(__file__)
sg.theme('DarkTanBlue')
# All the stuff inside your window.

tasks = []
list_tasks = sg.Listbox(tasks, size=(50, 4), font=('Arial Bold', 12), expand_y=True, enable_events=True, key='-LIST-')
layout = [[sg.Input(size=(20, 1), font=('Arial Bold', 12), expand_x=True, key='-INPUT-', do_not_clear=False)],
    [list_tasks],
    # [sg.FileBrowse(file_types=(("TXT Files", "*.txt"), ("ALL Files", "*.*")))],
    [sg.Button('Add'), sg.Button('Remove'), sg.Button('Save'), sg.Button('Load'), sg.Button('Exit')],
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
    # elif event == 'Save':
    #     d = window['-FILE-'].get()
    #     filename = sg.popup_get_file('', save_as=True, no_window=True, file_types=(("Text File", "*.txt"), ("All Files", "*.*")), initial_folder=script_path, default_path = d)
    #     window.SaveToDisk(filename)
    #     # window['-SAVE_AS-'].update(visible=False)
    #     window['-INPUT-'].update(visible=True)
    # # elif event == 'Load':
    # #     file_name = sg.popup_get_file('Load', no_window=True)
    # #     window.LoadFromDisk(file_name)
        
window.close()

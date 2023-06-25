import PySimpleGUI as sg
import os

script_path = os.path.dirname(__file__)
sg.theme('Black')



t1 = sg.Input(visible=False, enable_events=True, key='-T1-', font=('Arial Bold', 10), expand_x=True)
t2 = sg.Input(visible=False, enable_events=True, key='-T2-', font=('Arial Bold', 10), expand_x=True)
t3 = sg.Multiline("", enable_events=True, key='-INPUT-',
 expand_x=True, expand_y=True, justification='left')
tasks = []
list_tasks = sg.Listbox(tasks, size=(50, 4), font=('Arial Bold', 12), expand_y=True, enable_events=True, key='-LIST-')
layout = [[sg.Input(size=(20, 1), font=('Arial Bold', 12), expand_x=True, key='-INPUT-', do_not_clear=False)],
    [list_tasks],
    [sg.Button('Add'), sg.Button('Remove'),sg.Button('Exit')],
    [[t1, sg.FilesBrowse(file_types=(("Text Files", "*.txt"),))],[t2, sg.FileSaveAs(file_types=(("Text Files", "*.txt"),))]],
    [sg.Text("", key='-MSG-', font=('Arial Bold', 12), justification='center')],
    [t3]
]


window = sg.Window('Empty your mind', layout, finalize=True, size=(600, 400))
window['-INPUT-'].bind('<Return>', "_Enter")
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
        #for loading almost okay
    if event == '-T1-':
        file = open(t1.get())
        txt = file.read()
        print(txt)
        window['-LIST-'].Update(values=[txt])
        #to save
    if event == '-T2-':
      file = open(t2.get(), "w")
      file.write(t3.get())
      file.close()
      
      
      
    # elif event == 'Save':
    #     d = window['-FILE-'].get()
    #     filename = sg.popup_get_file('', save_as=True, no_window=True, file_types=(("Python Files", "*.py"), ("All Files", "*.*")), initial_folder=script_path, default_path = d)
    #     window.SaveToDisk(filename)
    #     window['-INPUT-'].update(visible=True)
    # elif event == 'Load':
    #     filename = sg.popup_get_file('File Name:',  title='Open', no_window=True)
    #     window.LoadFromDisk(filename)
    #     window['-LIST-'].update(tasks)
    #     print(filename)
    #     print(tasks)
        # if file not in (None,''):
        #     with open(file,'rb') as f:
        #         file_text = f.read()
        #     window['-LIST-'].update(tasks)

   
        
window.close()

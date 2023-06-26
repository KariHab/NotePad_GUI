# A notepad that allows you to drops ideas, tasks or things to do and save it as a text file
# You can load any text file and modify it 
# Karima H - June 2023

import PySimpleGUI as sg

sg.theme('Black')
image = 'ToDo_list\TO-DO-list---List-Checker\icon.ico'
t1 = sg.Input(visible=False, enable_events=True, key='-T1-', font=('Arial', 10), expand_x=True)
t2 = sg.Input(visible=False, enable_events=True, key='-T2-', font=('Arial', 10), expand_x=True)
t3 = sg.Multiline("", enable_events=True, key='-INPUT-', expand_x=True, expand_y=True, justification='left')
layout = [[sg.Text("Drop your ideas below", font=('Arial Bold', 10))],
    [t3],
    [[t1, sg.FilesBrowse(file_types=(("Text Files", "*.txt"),)),t2, sg.FileSaveAs(file_types=(("Text Files", "*.txt"),))]], 
]


window = sg.Window('NotePad', layout, size=(600, 400), location=(0,625), icon = 'icon.png')
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: 
        break
#for loading text file
    if event == '-T1-':
        file = open(t1.get())
        txt = file.read()
        window['-INPUT-'].Update(value=txt)
#for saving in a text file
    if event == '-T2-':
      file = open(t2.get(), "w")
      file.write(t3.get())
      file.close()
window.close()

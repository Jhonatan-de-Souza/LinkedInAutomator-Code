import PySimpleGUI as sg
from threading import Thread
from app import iniciar_automacao

sg.theme('reddit')

layout = [
    [sg.Text('Qual profissão deseja buscar')],
    [sg.Input(size=(50,1),key='palavra_chave')],
    [sg.Button('Iniciar Automação',key='iniciar_automacao')],
    [sg.Output(size=(50,30))]
]

window = sg.Window('Linked Automator',layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'iniciar_automacao':
        palavra_chave = values['palavra_chave']
        window['iniciar_automacao'].update(disabled=True)
        thread = Thread(target=iniciar_automacao,daemon=True,args=(palavra_chave,window))
        thread.start()

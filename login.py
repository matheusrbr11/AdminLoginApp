from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'),sg.Input(key='usuario', size=(20,1))],
    [sg.Text('Senha'),sg.Input(key='senha',password_char='*', size=(20,1))],
    [sg.Button('Entrar')]
]

janela = sg.Window('Tela de Login', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'matheus' and valores['senha'] == '1234': print('Bem Vindo!')
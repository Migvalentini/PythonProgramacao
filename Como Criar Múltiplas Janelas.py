import PySimpleGUI as sg

def criar_janela1():
    layout = [
                [sg.Button('Cadastro de Alunos')],
                [sg.Button('Cadastro de Matérias')],
                [sg.Button('Inserção de Notas')],
                [sg.Button('Emissão de Boletins')],
                [sg.Button('Sair')],
             ]
    return sg.Window('Facilitando a Escola', layout, finalize=True)

def criar_janela2():
    layout = [
                [sg.Text('Cadastro de Alunos')],
                [],
                [sg.Text('Matrícula do Aluno:'), sg.Input(key='matricula')],
                [sg.Text('Nome do Aluno:'), sg.Input(key='nome')],
                [sg.Button('Salvar'), sg.Button('Sair')],
             ]
    return sg.Window('Alunos', layout, finalize=True)


janela1, janela2 = criar_janela1(), None

while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 and event in (sg.WIN_CLOSED, 'Sair'):
        break

    if window == janela1:
        if event == 'Cadastro de Alunos':
            janela1.hide()
            janela2 = criar_janela2()

    if window == janela2:
        if event == 'Salvar':
            janela2['matricula'].update('')
            janela2['nome'].update('')
        elif event in (sg.WIN_CLOSED, 'Sair'):         
            janela2.close()
            janela1.un_hide()
    

window.close()
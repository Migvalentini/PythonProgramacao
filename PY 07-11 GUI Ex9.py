import PySimpleGUI as sg
from random import choice, shuffle

sg.theme("DarkBlue")

layout = [
    [sg.Text("Informe o nome do 1° aluno")],
    [sg.InputText(key="aluno1")],
    [sg.Text("Informe o nome do 2° aluno")],
    [sg.InputText(key="aluno2")],
    [sg.Text("Informe o nome do 3° aluno")],
    [sg.InputText(key="aluno3")],
    [sg.Text("Informe o nome do 4° aluno")],
    [sg.InputText(key="aluno4")],
    [sg.Button("Sortear"),sg.Button("Ordenar"),sg.Button("Cancelar")],
    [sg.Text("Aqui será mostrado o aluno sorteado",key="sorteado")],
]

janela = sg.Window("Aluno Sorteado e Alunos Ordenados",layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        print("A janela foi fechada")
        break
    if evento == "Sortear":
        print("Cálculo Realizado")
        aluno1 = str(valores["aluno1"])
        aluno2 = str(valores["aluno2"])
        aluno3 = str(valores["aluno3"])
        aluno4 = str(valores["aluno4"])
        lista = [aluno1,aluno2,aluno3,aluno4]
        sorteado = choice(lista)

        janela["sorteado"].update(f"O azarado foi: {sorteado}")

    if evento == "Ordenar":
        print("Cálculo Realizado")
        aluno1 = str(valores["aluno1"])
        aluno2 = str(valores["aluno2"])
        aluno3 = str(valores["aluno3"])
        aluno4 = str(valores["aluno4"])
        lista = [aluno1,aluno2,aluno3,aluno4]
        shuffle(lista)

        janela["sorteado"].update(f"A ordem sorteada foi: {lista}")
        
janela.close()
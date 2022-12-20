import PySimpleGUI as sg

layout = [
    [sg.Text("Informe um valor")],
    [sg.InputText(key="numero")],
    [sg.Button("Ant/Suc"),sg.Button("Cancelar")],
    [sg.Text("Aqui sera mostrado o antecessor",key="antecessor")],
    [sg.Text("Aqui sera mostrado o sucessor",key="sucessor")],
]

janela = sg.Window("Antecessor e Sucessor",layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        print("A janela foi fechada")
        break
    if evento == "Ant/Suc":
        print("Cálculo Realizado")
        numero = int(valores["numero"])
        ant = numero - 1
        suc = numero + 1
        janela["antecessor"].update(f"Antecessor: {ant}")
        janela["sucessor"].update(f"Sucessor: {suc}")

janela.close()
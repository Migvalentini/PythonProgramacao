import PySimpleGUI as sg

layout = [
    [sg.Text("Informe um valor em metros")],
    [sg.InputText(key="numero")],
    [sg.Button("Ant/Suc"),sg.Button("Cancelar")],
    [sg.Text("Aqui será mostrado o valor em centímetros",key="centímetros")],
    [sg.Text("Aqui será mostrado o valor em milímetros",key="milímetros")],
]

janela = sg.Window("Centímetros e Milímetros",layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        print("A janela foi fechada")
        break
    if evento == "Ant/Suc":
        print("Cálculo Realizado")
        numero = int(valores["numero"])
        cen = numero * 100
        mil = numero * 1000
        janela["centímetros"].update(f"Centímetros: {cen}")
        janela["milímetros"].update(f"Milímetros: {mil}")

janela.close()
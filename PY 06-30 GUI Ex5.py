import PySimpleGUI as sg

layout = [
    [sg.Text("Informe um valor em Graus Celsius")],
    [sg.InputText(key="numero")],
    [sg.Button("Fahrenheit"),sg.Button("Cancelar")],
    [sg.Text("Aqui sera mostrado o valor convertido em Fahrenheit",key="Fahrenheit")],
]

janela = sg.Window("Graus Celsius e Fahrenheit",layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        print("A janela foi fechada")
        break
    if evento == "Fahrenheit":
        print("Cálculo Realizado")
        numero = int(valores["numero"])
        ant = numero - 1

        janela["antecessor"].update(f"Antecessor: {ant}")


janela.close()
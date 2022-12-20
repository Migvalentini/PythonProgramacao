import PySimpleGUI as sg

layout = [
    [sg.Text("Informe quantos reais você tem na carteira: ")],
    [sg.InputText(key="reais")],
    [sg.Button("Dólares"),sg.Button("Cancelar")],
    [sg.Text("Aqui será mostrado o valor convertido em dólares",key="dólares")],
    [sg.Image(r'C:\Users\Sandro\Documents\TRABALHOS DO MIGUEL\dolar3.png')],
]

janela = sg.Window("Reais e Dólares",layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        print("A janela foi fechada")
        break
    if evento == "Dólares":
        print("Cálculo Realizado")
        reais = int(valores["reais"])
        dolares = round(reais / 4.95,2)
        janela["dólares"].update(f"Você tem {dolares} dólares")
    
    

janela.close()
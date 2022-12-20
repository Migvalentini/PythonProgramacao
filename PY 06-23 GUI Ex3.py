import PySimpleGUI as sg

layout = [
    [sg.Text("Informe o valor em reais:")],
    [sg.InputText(key="valor")],
    [sg.Button("Decompor"),sg.Button("Cancelar")],
    [sg.Text("Aqui será mostrado as notas de 100",key="n100")],
    [sg.Text("Aqui será mostrado as notas de 50",key="n50")],    
    [sg.Text("Aqui será mostrado as notas de 20",key="n20")],
    [sg.Text("Aqui será mostrado as notas de 10",key="n10")],
    [sg.Text("Aqui será mostrado as notas de 5",key="n5")],
    [sg.Text("Aqui será mostrado as notas de 2",key="n2")],
    [sg.Text("Aqui será mostrado as notas de 1",key="n1")],
]

janela = sg.Window("Decomposição de Notas",layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        print("A janela foi fechada")
        break
    if evento == "Decompor":
        print("Cálculo Realizado")
        valor = int(valores["valor"])
        notas100 = valor // 100
        resto50 = valor % 100
        notas50 = resto50 // 50
        resto20 = resto50 % 50
        notas20 = resto20 // 20
        resto10 = resto20 % 20
        notas10 = resto10 // 10
        resto5 = resto10 % 10
        notas5 = resto5 // 5
        resto2 = resto5 % 5
        notas2 = resto2 // 2
        resto1 = resto2 % 2
        notas1 = resto1 // 1
        janela["n100"].update(f"Notas 100: {notas100}")
        janela["n50"].update(f"Notas 50: {notas50}")
        janela["n20"].update(f"Notas 20: {notas20}")
        janela["n10"].update(f"Notas 10: {notas10}")
        janela["n5"].update(f"Notas 5: {notas5}")
        janela["n2"].update(f"Notas 2: {notas2}")
        janela["n1"].update(f"Notas 1: {notas1}")

janela.close()
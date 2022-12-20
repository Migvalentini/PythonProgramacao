import PySimpleGUI as sg
from math import trunc

sg.theme("DarkBlue")

layout = [
    [sg.Text("Informe o nome do 1° produto:")],
    [sg.InputText(key="produto1")],
    [sg.Text("Informe o nome do 2° produto:")],
    [sg.InputText(key="produto2")],
    [sg.Text("Informe a quantidade em kg do 1° produto:")],
    [sg.InputText(key="quantidade1")],
    [sg.Text("Informe a quantidade em kg do 2° produto:")],
    [sg.InputText(key="quantidade2")],
    [sg.Text("Informe o valor do desconto:")],
    [sg.InputText(key="desconto")],
    [sg.Button("Calcular",button_color="Blue"),sg.Button("Cancelar",button_color="Blue")],
    [sg.Text("Aqui sera mostrado o valor total a pagar pelo 1° produto",key="valor1")],
    [sg.Text("Aqui sera mostrado o valor total a pagar pelo 2° produto",key="valor2")],
    [sg.Text("Aqui sera mostrado o valor total a pagar",key="valor_total")],
]

janela = sg.Window("Produtos, Quantidades e Valor",layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        print("A janela foi fechada")
        break
    if evento == "Calcular":
        print("Cálculo Realizado")
        produto1 = str(valores["produto1"])
        produto2 = str(valores["produto2"])
        quantidade1 = int(valores["quantidade1"])
        quantidade2 = int(valores["quantidade2"])
        desconto = int(valores["desconto"])

        if quantidade1 <= 5:
            valor_produto1 = 2.5 * quantidade1
        elif quantidade1 > 5:
            valor_produto1 = 2.2 * quantidade1
        if quantidade2 <= 5:
            valor_produto2 = 1.8 * quantidade2       
        elif quantidade2 > 5:
            valor_produto2 = 1.5 * quantidade2
        quantidade_total = quantidade1 + quantidade2
        valor_total = valor_produto1 + valor_produto2
        valor_a_pagar = valor_produto1 + valor_produto2
        if quantidade_total > 8 or valor_total > 25:
            valor_a_pagar = trunc(valor_total - desconto)

        janela["valor1"].update(f"O valor a ser pago pelos(as) {produto1} é de: {valor_produto1} reais")
        janela["valor2"].update(f"O valor a ser pago pelos(as) {produto2} é de: {valor_produto2} reais")
        janela["valor_total"].update(f"O valor total a ser pago é de {valor_a_pagar} reais")


janela.close()
import PySimpleGUI as sg

sg.theme("DarkBlue")

layout = [
    [sg.Text("Informe o número de horas trabalhadas pelo usuário:")],
    [sg.InputText(key="horas",text_color="Black")],
    [sg.Text("Informe o valor por horas trabalhadas:")],
    [sg.InputText(key="valor_hora",text_color="Black")],
    [sg.Text("Informe o percentual de aumento do salário:")],
    [sg.InputText(key="percentual",text_color="Black")],
    [sg.Button("Calcular"),sg.Button("Cancelar")],
    [sg.Text("Aqui será mostrado o salário inicial",key="salario")],
    [sg.Text("Aqui será mostrado o salário atualizado",key="salario_atualizado")],
]

janela = sg.Window("Horas Trabalhadas e Salário",layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        print("A janela foi fechada")
        break
    if evento == "Calcular":
        print("Cálculo Realizado")
        horas = int(valores["horas"])
        valor_hora = int(valores["valor_hora"])
        aumento = int(valores["percentual"])

        salario_inicial = horas * valor_hora
        salario_atualizado = salario_inicial + salario_inicial / 100 * aumento

        janela["salario"].update(f"Salário Inicial: R${salario_inicial}")
        janela["salario_atualizado"].update(f"Salário com Aumento: R${salario_atualizado}")

janela.close()
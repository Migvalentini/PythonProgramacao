from fileinput import filename
import PySimpleGUI as sg
import os #biblioteca do sistema operacional

sg.theme("DarkBlue")

dir_atual = os.getcwd() #pega o diretorio onde esta o programa do python

dir = os.path.join(dir_atual,'Imagens')
#junta esse diretorio com uma pasta chamada img (dentro da pasta onde está o programa) onde você deve colocar as fotos dos carros, fica mais organizado

lista_veiculos = ["Compacto","Econômico","Sedan","Minivan","SUV","Executivo","Prime","Pick-up"]

layout = [
    [sg.Text("Escolha a categoria do carro desejada:   "),
    #Utiliza Combo aqui por que é um componente melhor quando a escolha é por uma única opção, o list é quando eu posso escolher mais que um
    sg.Combo(lista_veiculos,font="oi",key="carros",enable_events=(True))],
    #Esse é um campo texto que vai servir só pra mostrar o valor associado à escolha do usuário pelo combo e você atualiza ele conforme muda a opção no combo
    #Por isso só um Text é suficiente
    [sg.Text("Taxa fixa por dia:                                ",key="taxa_dia",)],   
    [sg.Text("Informe o percentual de desconto:          "),sg.InputText(key="percentual_desconto",size=(10,10))],
    [sg.Text("Informe a taxa por Km rodado (em reais):"),sg.InputText(key="taxa_km",size=(10,10))],
    [sg.Text("Informe o número de dias:                      "),sg.InputText(key="dias",size=(10,10))],
    [sg.Text("Informe o número de km:                       "),sg.InputText(key="km",size=(10,10))],
    [sg.Text("Aqui será mostrado o valor total do aluguel:",key="valor_total")],
    [sg.Text("Aqui será mostrado o percentual de desconto:",key="desconto")],
    [sg.Text("Aqui será mostrado o valor do desconto em reais:",key="desconto_valor")],
    [sg.Text("Aqui será mostrado o número de dias:",key="numero_dias")],
    [sg.Text("Aqui será mostrado o número de quilômetros:",key="numero_km")], 
    #aqui tem que ser um componente imagem que vai começar sem nenhum arquivo de imagem vinculado
    [sg.Image(key="imagem")],
    [sg.Button("Calcular"),sg.Button("Cancelar")],
   
]

janela = sg.Window("Locadora de Carros",layout)

while True:
    evento, valores = janela.read()

    #O teste aqui fica fora do botão de calculo e usa as mudanças pra atualizar o campo da taxa dia na tela, 
    #alem da variavel que vai ser usada pro calculo
    #faz o teste pra cada tipo de carro e tem que usar a variavel valores aqui
    if valores["carros"] == "Compacto":
        taxa_dias = 10
        janela["taxa_dia"].update(f"Taxa fixa por dia:                                     R${taxa_dias}")
    if valores["carros"] == "Econômico":
        taxa_dias = 20
        janela["taxa_dia"].update(f"Taxa fixa por dia:                                     R${taxa_dias}")
    if valores["carros"] == "Sedan":
        taxa_dias = 30
        janela["taxa_dia"].update(f"Taxa fixa por dia:                                     R${taxa_dias}")
    if valores["carros"] == "Minivan":
        taxa_dias = 35
        janela["taxa_dia"].update(f"Taxa fixa por dia:                                     R${taxa_dias}")
    if valores["carros"] == "SUV":
        taxa_dias = 40
        janela["taxa_dia"].update(f"Taxa fixa por dia:                                     R${taxa_dias}")
    if valores["carros"] == "Executivo":
        taxa_dias = 50
        janela["taxa_dia"].update(f"Taxa fixa por dia:                                     R${taxa_dias}")
    if valores["carros"] == "Prime":
        taxa_dias = 100
        janela["taxa_dia"].update(f"Taxa fixa por dia:                                     R${taxa_dias}")
    if valores["carros"] == "Pick-up":
        taxa_dias = 45   
        janela["taxa_dia"].update(f"Taxa fixa por dia:                                     R${taxa_dias}")

    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        print("A janela foi fechada")
        break

    if evento == "Calcular":   
        desconto = float(valores["percentual_desconto"])
        taxa_km = float(valores["taxa_km"])
        dias = int(valores["dias"]) 
        km = int(valores["km"])

        valor_desconto = taxa_dias - (taxa_dias/100*desconto)
        valor_total = (taxa_dias-valor_desconto) * dias + taxa_km * km
                
        janela["valor_total"].update(f"Valor Total: R${valor_total}")
        janela["desconto"].update(f"Percentual de Desconto: {desconto}%")
        janela["desconto_valor"].update(f"Valor do Desconto: R${valor_desconto}")
        janela["numero_dias"].update(f"Número de Dias: {dias}")
        janela["numero_km"].update(f"Quilômetros Rodados: {km}")

        if valores["carros"] == "Compacto":
            janela["imagem"].update(filename=os.path.join(dir,'compacto.png'))
            
        if valores["carros"] == "Económico":
            janela["imagem"].update(filename=os.path.join(dir,'economico.png'))
        if valores["carros"] == "Sedan":
            janela["imagem"].update(filename=os.path.join(dir,'sedan.png'))
        if valores["carros"] == "Minivan":
            janela["imagem"].update(filename=os.path.join(dir,'minivan.png'))
        if valores["carros"] == "SUV":
            janela["imagem"].update(filename=os.path.join(dir,'SUV.png'))
        if valores["carros"] == "Executivo":
            janela["imagem"].update(filename=os.path.join(dir,'executivo.png'))
        if valores["carros"] == "Prime":
            janela["imagem"].update(filename=os.path.join(dir,'prime.png'))
        if valores["carros"] == "Pick-up":
            janela["imagem"].update(filename=os.path.join(dir,'pickup.png'))
        
janela.close()
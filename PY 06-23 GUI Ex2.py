import PySimpleGUI as sg

layout = [
    [sg.Text("Informe o valor da altura da parede em metros:")],
    [sg.InputText(key="altura")],
    [sg.Text('Informe o valor da largura da parede em metros')],
    [sg.InputText(key="largura")],
    [sg.Button("Metros Quadrados"),sg.Button("Cancelar")],
    [sg.Text("Escolha a cor desejada para pintar a parede:")],
    [sg.Listbox(["Black","White","Blue"],key="Cor")],
    [sg.Text("Aqui será mostrado o tamanho da parede em metros quadrados",key="Metros quadrados")],
    [sg.Text("Aqui será mostrado a quantidade de tinta necessária",key="Tinta Necessária")],
    [sg.Graph(canvas_size=(400, 400), graph_bottom_left=(0, 0), graph_top_right=(400, 400), background_color='gray', enable_events=True, key='graph')],

]

janela = sg.Window("Altura, Largura, Área e Tinta",layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        print("A janela foi fechada")
        break
    if evento == "Metros Quadrados":
        print("Cálculo Realizado")
        altura = int(valores["altura"])
        largura = int(valores["largura"])
        metros2 = altura * largura
        tinta = metros2 / 2
        cor = valores["Cor"]
        graph = janela['graph'] 
        janela["Metros quadrados"].update(f"Área: {metros2} metros quadrados")
        janela["Tinta Necessária"].update(f"Quantidade de tinta necessária: {tinta} litros")
        print(valores)
        if cor == ['Black']:
            print("Escolheu Preto")
            rectangle = graph.draw_rectangle((250, 250), (altura, largura), fill_color='black')
        elif cor == ['White']:
            print("Escolheu Branco")
            rectangle = graph.draw_rectangle((250, 250), (altura, largura), fill_color='white')
        elif cor == ['Blue']:
            print("Escolheu Azul")
            rectangle = graph.draw_rectangle((250, 250), (altura, largura), fill_color='blue')
    

janela.close()

'''Utilizando uma interface gráfica, desenvolva uma aplicação que leia os códigos e os nomes dos 5 candidatos da eleição para presidente. 
Grave essas informações em um arquivo.

Em outra tela seu programa deve mostrar os 5 candidatos e leia as votações de cada candidato no 1o turno.

Seu programa deve então calcular e escrever, para cada candidato, seu código e seu percentual de votos.

Se a eleição foi decidida no 1o turno, i.e., um candidato obteve 50% dos votos válidos + 1, o programa deve escrever o código e o
percentual de votos do eleito. 
Em caso contrário, deve escrever os códigos e os percentuais de votos dos dois candidatos que disputarão o segundo turno.'''

import PySimpleGUI as sg

def criar_janela1():
    layout = [
                [sg.Text("Escolha os códigos e os nomes de 5 candidatos da eleição para presidência:")],
                [sg.Text("Código do candidato 1: "),sg.InputText(key="codigo1",size=(4,4)),sg.Text("Nome do candidato 1: "),sg.InputText(key="nome1",size=(10,10))],
                [sg.Text("Código do candidato 2: "),sg.InputText(key="codigo2",size=(4,4)),sg.Text("Nome do candidato 2: "),sg.InputText(key="nome2",size=(10,10))],
                [sg.Text("Código do candidato 3: "),sg.InputText(key="codigo3",size=(4,4)),sg.Text("Nome do candidato 3: "),sg.InputText(key="nome3",size=(10,10))],
                [sg.Text("Código do candidato 4: "),sg.InputText(key="codigo4",size=(4,4)),sg.Text("Nome do candidato 4: "),sg.InputText(key="nome4",size=(10,10))],
                [sg.Text("Código do candidato 5: "),sg.InputText(key="codigo5",size=(4,4)),sg.Text("Nome do candidato 5: "),sg.InputText(key="nome5",size=(10,10))],
                [sg.Button('Avançar'),sg.Button('Sair')],
             ]
    return sg.Window('Eleição Presidencial', layout, finalize=True)

def criar_janela2():
    layout = [
                [sg.Text('Informe quantos votos o candidato 1 recebeu: '),sg.Input(key="votos_candidato1",s=(8))],
                [sg.Text('Informe quantos votos o candidato 2 recebeu: '),sg.Input(key="votos_candidato2",s=(8))],
                [sg.Text('Informe quantos votos o candidato 3 recebeu: '),sg.Input(key="votos_candidato3",s=(8))],
                [sg.Text('Informe quantos votos o candidato 4 recebeu: '),sg.Input(key="votos_candidato4",s=(8))],
                [sg.Text('Informe quantos votos o candidato 5 recebeu: '),sg.Input(key="votos_candidato5",s=(8))],
                [sg.Button('Avançar'),sg.Button('Voltar'),sg.Button('Sair')],
             ]
    return sg.Window('Votos por Candidato', layout, finalize=True)

def criar_janela3():
    layout = [
                [sg.Text("Aqui será mostrado o número de votos do candidato 1",key="candidato1")],
                [sg.Text("Aqui será mostrado o número de votos do candidato 2",key="candidato2")],
                [sg.Text("Aqui será mostrado o número de votos do candidato 3",key="candidato3")],
                [sg.Text("Aqui será mostrado o número de votos do candidato 4",key="candidato4")],
                [sg.Text("Aqui será mostrado o número de votos do candidato 5",key="candidato5")],
                [sg.Text("Aqui será mostrado o resultado das eleições",key="resultado")],
                [sg.Button("Mostrar Dados"),sg.Button("Voltar"),sg.Button("Sair")],
            ]
    return sg.Window("Número de Votos", layout, finalize=True)

janela1, janela2, janela3 = criar_janela1(), None, None

while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 and event in (sg.WIN_CLOSED, 'Sair'):
        break

    if window == janela1:
        if event == 'Avançar':
            codigo_candidato1 = float(values["codigo1"])
            codigo_candidato2 = float(values["codigo2"])
            codigo_candidato3 = float(values["codigo3"])
            codigo_candidato4 = float(values["codigo4"])
            codigo_candidato5 = float(values["codigo5"])
            nome_candidato1 = str(values["nome1"])
            nome_candidato2 = str(values["nome2"])
            nome_candidato3 = str(values["nome3"])
            nome_candidato4 = str(values["nome4"])
            nome_candidato5 = str(values["nome5"])
            janela1.hide()
            janela2 = criar_janela2()
            
        
    if window == janela2:
        votos_candidato1 = float(values["votos_candidato1"])
        votos_candidato2 = float(values["votos_candidato2"])
        votos_candidato3 = float(values["votos_candidato3"])
        votos_candidato4 = float(values["votos_candidato4"])
        votos_candidato5 = float(values["votos_candidato5"])
        if event == 'Avançar':
            janela2.hide()
            janela3 = criar_janela3()
        elif event == 'Voltar':
            janela2.hide()
            janela1.un_hide()
        elif event == 'Sair':
            break
        elif event in (sg.WIN_CLOSED, 'Sair'):         
            janela2.close()
            janela1.un_hide()
    
    if window == janela3:
        if event == "Mostrar Dados":
            total_votos = votos_candidato1+votos_candidato2+votos_candidato3+votos_candidato4+votos_candidato5
            votos_validos = total_votos/2
            lista_candidatos = [votos_candidato1,votos_candidato2,votos_candidato3,votos_candidato4,votos_candidato5]
            lista_candidatos.sort()
            maior=lista_candidatos[-1]
            segundo_maior=lista_candidatos[-2]

            percentual1 = round((votos_candidato1*100)/total_votos,2)
            percentual2 = round((votos_candidato2*100)/total_votos,2)
            percentual3 = round((votos_candidato3*100)/total_votos,2)
            percentual4 = round((votos_candidato4*100)/total_votos,2)
            percentual5 = round((votos_candidato5*100)/total_votos,2)
            janela3["candidato1"].update(f"O Número de Votos do Candidato {nome_candidato1} foi de {votos_candidato1} e o seu percentual de votos foi {percentual1}%")
            janela3["candidato2"].update(f"O Número de Votos do Candidato {nome_candidato2} foi de {votos_candidato2} e o seu percentual de votos foi {percentual2}%")
            janela3["candidato3"].update(f"O Número de Votos do Candidato {nome_candidato3} foi de {votos_candidato3} e o seu percentual de votos foi {percentual3}%")
            janela3["candidato4"].update(f"O Número de Votos do Candidato {nome_candidato4} foi de {votos_candidato4} e o seu percentual de votos foi {percentual4}%")
            janela3["candidato5"].update(f"O Número de Votos do Candidato {nome_candidato5} foi de {votos_candidato5} e o seu percentual de votos foi {percentual5}%")
            if votos_candidato1>votos_validos:
                janela3["resultado"].update(f"O Candidato {nome_candidato1}, com código {codigo_candidato1} ganhou a eleição no 1° turno com {percentual1}% dos votos")
            elif votos_candidato2>votos_validos:
                janela3["resultado"].update(f"O Candidato {nome_candidato2}, com código {codigo_candidato2} ganhou a eleição no 1° turno com {percentual2}% dos votos")
            elif votos_candidato3>votos_validos:
                janela3["resultado"].update(f"O Candidato {nome_candidato3}, com código {codigo_candidato3} ganhou a eleição no 1° turno com {percentual3}% dos votos")
            elif votos_candidato4>votos_validos:
                janela3["resultado"].update(f"O Candidato {nome_candidato4}, com código {codigo_candidato4} ganhou a eleição no 1° turno com {percentual4}% dos votos")
            elif votos_candidato5>votos_validos:
                janela3["resultado"].update(f"O Candidato {nome_candidato5}, com código {codigo_candidato5} ganhou a eleição no 1° turno com {percentual5}% dos votos")
            else:
                janela3["resultado"].update(f"Os Candidatos que Disputarão o 2° Turno são: {maior} e {segundo_maior}")
        elif event == "Voltar":
            janela3.hide()
            janela2.un_hide()
        elif event in (sg.WIN_CLOSED,"Sair"):
            break
    

window.close()
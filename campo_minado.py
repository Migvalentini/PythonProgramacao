import PySimpleGUI as sg
from random import randint
from fileinput import filename
import os
import time

sg.theme("GreenMono")

dir_atual = os.getcwd() 
dir = os.path.join(dir_atual,'Imagens')
sz=(5,2)
cor = "Gray"

sg.SetOptions(element_padding=(0, 0))

def criar_menu():
    layout = [
                [sg.Text("Nome: Miguel Valentini")],
                [sg.Text("Data: 01/12")],
                [sg.Text("Turma: Beta 2")],
                [sg.Text("Disciplina: Programação")],[sg.Text(" ")],
                [sg.Image(filename=os.path.join(dir,'Campo-minado.png'),subsample=2)],[sg.Text(" ")],
                [sg.Text("Selecione a Dificuldade Desejada:")],[sg.Text(" ")],
                [sg.Listbox(["Iniciante","Intermediário","Avançado"],size=(15,0),key="Listbox Dificuldade",no_scrollbar = True, background_color="LightGray", highlight_background_color="#6E6E6E")],[sg.Text(" ")],
                [sg.Text("Iniciante: 10 bombas")],
                [sg.Text("Intermediário: 20 bombas")],
                [sg.Text("Avançado: 30 bombas")],[sg.Text(" ")],
                [sg.Button("Sair"),sg.Text(" "),sg.Button('Começar')],
             ]
    return sg.Window('Seja Bem-Vindo ao Jogo', layout, finalize=True)

def criar_janela_jogo():
    layout = [
                [sg.Text(key="cabeçalho"), sg.Text("                                                                 "), sg.Text(key="cronometro")],
                [sg.Button('?',size=sz, button_color = cor, key=(0,0)),sg.Button('?',size=sz, button_color = cor, key=(0,1)),sg.Button('?',size=sz, button_color = cor, key=(0,2)),sg.Button('?',size=sz, button_color = cor, key=(0,3)),sg.Button('?',size=sz, button_color = cor, key=(0,4)),sg.Button('?',size=sz, button_color = cor, key=(0,5)),sg.Button('?',size=sz, button_color = cor, key=(0,6)),sg.Button('?',size=sz, button_color = cor, key=(0,7)),sg.Button('?',size=sz, button_color = cor, key=(0,8)),sg.Button('?',size=sz, button_color = cor, key=(0,9))],
                [sg.Button('?',size=sz, button_color = cor, key=(1,0)),sg.Button('?',size=sz, button_color = cor, key=(1,1)),sg.Button('?',size=sz, button_color = cor, key=(1,2)),sg.Button('?',size=sz, button_color = cor, key=(1,3)),sg.Button('?',size=sz, button_color = cor, key=(1,4)),sg.Button('?',size=sz, button_color = cor, key=(1,5)),sg.Button('?',size=sz, button_color = cor, key=(1,6)),sg.Button('?',size=sz, button_color = cor, key=(1,7)),sg.Button('?',size=sz, button_color = cor, key=(1,8)),sg.Button('?',size=sz, button_color = cor, key=(1,9))],
                [sg.Button('?',size=sz, button_color = cor, key=(2,0)),sg.Button('?',size=sz, button_color = cor, key=(2,1)),sg.Button('?',size=sz, button_color = cor, key=(2,2)),sg.Button('?',size=sz, button_color = cor, key=(2,3)),sg.Button('?',size=sz, button_color = cor, key=(2,4)),sg.Button('?',size=sz, button_color = cor, key=(2,5)),sg.Button('?',size=sz, button_color = cor, key=(2,6)),sg.Button('?',size=sz, button_color = cor, key=(2,7)),sg.Button('?',size=sz, button_color = cor, key=(2,8)),sg.Button('?',size=sz, button_color = cor, key=(2,9))],
                [sg.Button('?',size=sz, button_color = cor, key=(3,0)),sg.Button('?',size=sz, button_color = cor, key=(3,1)),sg.Button('?',size=sz, button_color = cor, key=(3,2)),sg.Button('?',size=sz, button_color = cor, key=(3,3)),sg.Button('?',size=sz, button_color = cor, key=(3,4)),sg.Button('?',size=sz, button_color = cor, key=(3,5)),sg.Button('?',size=sz, button_color = cor, key=(3,6)),sg.Button('?',size=sz, button_color = cor, key=(3,7)),sg.Button('?',size=sz, button_color = cor, key=(3,8)),sg.Button('?',size=sz, button_color = cor, key=(3,9))],
                [sg.Button('?',size=sz, button_color = cor, key=(4,0)),sg.Button('?',size=sz, button_color = cor, key=(4,1)),sg.Button('?',size=sz, button_color = cor, key=(4,2)),sg.Button('?',size=sz, button_color = cor, key=(4,3)),sg.Button('?',size=sz, button_color = cor, key=(4,4)),sg.Button('?',size=sz, button_color = cor, key=(4,5)),sg.Button('?',size=sz, button_color = cor, key=(4,6)),sg.Button('?',size=sz, button_color = cor, key=(4,7)),sg.Button('?',size=sz, button_color = cor, key=(4,8)),sg.Button('?',size=sz, button_color = cor, key=(4,9))],
                [sg.Button('?',size=sz, button_color = cor, key=(5,0)),sg.Button('?',size=sz, button_color = cor, key=(5,1)),sg.Button('?',size=sz, button_color = cor, key=(5,2)),sg.Button('?',size=sz, button_color = cor, key=(5,3)),sg.Button('?',size=sz, button_color = cor, key=(5,4)),sg.Button('?',size=sz, button_color = cor, key=(5,5)),sg.Button('?',size=sz, button_color = cor, key=(5,6)),sg.Button('?',size=sz, button_color = cor, key=(5,7)),sg.Button('?',size=sz, button_color = cor, key=(5,8)),sg.Button('?',size=sz, button_color = cor, key=(5,9))],
                [sg.Button('?',size=sz, button_color = cor, key=(6,0)),sg.Button('?',size=sz, button_color = cor, key=(6,1)),sg.Button('?',size=sz, button_color = cor, key=(6,2)),sg.Button('?',size=sz, button_color = cor, key=(6,3)),sg.Button('?',size=sz, button_color = cor, key=(6,4)),sg.Button('?',size=sz, button_color = cor, key=(6,5)),sg.Button('?',size=sz, button_color = cor, key=(6,6)),sg.Button('?',size=sz, button_color = cor, key=(6,7)),sg.Button('?',size=sz, button_color = cor, key=(6,8)),sg.Button('?',size=sz, button_color = cor, key=(6,9))],
                [sg.Button('?',size=sz, button_color = cor, key=(7,0)),sg.Button('?',size=sz, button_color = cor, key=(7,1)),sg.Button('?',size=sz, button_color = cor, key=(7,2)),sg.Button('?',size=sz, button_color = cor, key=(7,3)),sg.Button('?',size=sz, button_color = cor, key=(7,4)),sg.Button('?',size=sz, button_color = cor, key=(7,5)),sg.Button('?',size=sz, button_color = cor, key=(7,6)),sg.Button('?',size=sz, button_color = cor, key=(7,7)),sg.Button('?',size=sz, button_color = cor, key=(7,8)),sg.Button('?',size=sz, button_color = cor, key=(7,9))],
                [sg.Button('?',size=sz, button_color = cor, key=(8,0)),sg.Button('?',size=sz, button_color = cor, key=(8,1)),sg.Button('?',size=sz, button_color = cor, key=(8,2)),sg.Button('?',size=sz, button_color = cor, key=(8,3)),sg.Button('?',size=sz, button_color = cor, key=(8,4)),sg.Button('?',size=sz, button_color = cor, key=(8,5)),sg.Button('?',size=sz, button_color = cor, key=(8,6)),sg.Button('?',size=sz, button_color = cor, key=(8,7)),sg.Button('?',size=sz, button_color = cor, key=(8,8)),sg.Button('?',size=sz, button_color = cor, key=(8,9))],
                [sg.Button('?',size=sz, button_color = cor, key=(9,0)),sg.Button('?',size=sz, button_color = cor, key=(9,1)),sg.Button('?',size=sz, button_color = cor, key=(9,2)),sg.Button('?',size=sz, button_color = cor, key=(9,3)),sg.Button('?',size=sz, button_color = cor, key=(9,4)),sg.Button('?',size=sz, button_color = cor, key=(9,5)),sg.Button('?',size=sz, button_color = cor, key=(9,6)),sg.Button('?',size=sz, button_color = cor, key=(9,7)),sg.Button('?',size=sz, button_color = cor, key=(9,8)),sg.Button('?',size=sz, button_color = cor, key=(9,9))],
                [sg.Text(" ")],
                [sg.Button("Sair"),sg.Text(" "),sg.Button("Voltar")],            
             ]
    return sg.Window('Jogo', layout, finalize=True)

game_layout = [ [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0]]

janela_menu, janela_jogo = criar_menu(), None
controlador = "sim"
numero_bombas = 10
current_time = 0
start_time = int(round(time.time() * 100))
botoes_clicados = []

while True:
    window, event, values = sg.read_all_windows()
    
    if window == janela_menu and event in (sg.WIN_CLOSED, 'Sair'):
        break

    if window == janela_menu:
        if event == 'Começar':
            janela_menu.hide()
            janela_jogo = criar_janela_jogo()
            dificuldade = values["Listbox Dificuldade"]
            if dificuldade == ["Iniciante"]:
                numero_bombas = 10
            elif dificuldade == ["Intermediário"]:
                numero_bombas = 20
            elif dificuldade == ["Avançado"]:
                numero_bombas = 30
            espaços_vazios = 100 - numero_bombas
            #Sorteio de bombas

            if controlador == "sim":
                for bomba in range(numero_bombas):
                    linha = randint(1,10)
                    coluna = randint(1,10)
                    if game_layout[linha][coluna] == 0:
                        game_layout[linha][coluna] = 1
                for x in range(1, 11):
                    for y in range(1, 11):
                        print(game_layout[x][y],end=" ")
                    print()
                controlador = "nao"

    if window == janela_jogo:
        current_time = int(round(time.time() * 100)) - start_time
        janela_jogo["cabeçalho"].update(f"Número de Bombas: {str(numero_bombas)}")
        janela_jogo["cronometro"].update('{:02d}:{:02d}.{:02d}'.format((current_time // 100) // 60,(current_time // 100) % 60,current_time % 100))

        if event == "Voltar":
            janela_jogo.close()
            janela_menu.un_hide()
            
        elif event in (sg.WIN_CLOSED, 'Sair'):         
            janela_jogo.close()
        

        #Se não for bomba

        elif game_layout[event[0]+1][event[1]+1] == 0:
            if event not in botoes_clicados:
                botoes_clicados.append(event)
                espaços_vazios -= 1
            lin = event[0] + 1
            col = event[1] + 1
            conta_bombas = 0
            if game_layout[lin-1][col-1] == 1:
                conta_bombas += 1
            if game_layout[lin-1][col] == 1:
                conta_bombas += 1
            if game_layout[lin-1][col+1] == 1:
                conta_bombas += 1
            if game_layout[lin][col-1] == 1:
                conta_bombas += 1
            if game_layout[lin][col+1] == 1:
                conta_bombas += 1
            if game_layout[lin+1][col-1] == 1:
                conta_bombas += 1
            if game_layout[lin+1][col] == 1:
                conta_bombas += 1
            if game_layout[lin+1][col+1] == 1:
                conta_bombas += 1
            
            janela_jogo[event].update(conta_bombas, button_color =("Black","DarkGray"))
            
            if espaços_vazios == 0:
                sg.popup("Parabéns, Você Venceu!")
                
        #Se for bomba    

        elif game_layout[event[0]+1][event[1]+1] == 1: 
            janela_jogo[event].update(" ", button_color="Black")
            sg.popup("VOCÊ PERDEU!")
            break
        
window.close()

print("\033[0;34mObrigado pela Jogatina!\033[m")
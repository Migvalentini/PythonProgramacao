import PySimpleGUI as sg
from fileinput import filename
import os
from random import choice

sg.theme("DarkBlue")

dir_atual = os.getcwd() 
dir = os.path.join(dir_atual,'Imagens')

peitoral = ["Supino Low Incline com Halteres","Supino Inclinado com Barra","Supino Reto Articulado",
            "Supino com Halteres","Crucifixo no Aparelho","Crucifixo Reto com Halteres","Flexão",
            "Cross Over Polia Alta","Cross Over Polia Baixa","Paralelas na Máquina","Supino Reto com Barra",
            "Supino com Pegada Neutra","Crucifixo Inclinado com Cabo","Supino Declinado com Barra","Pull Over com Halteres"]
costas = ["Puxada Aberta no Pulley","Barra Fixa Pegada Fechada","Barra Fixa com Pegada Aberta",
          "Remada Curvada Pegada Pronada com Barra","Remada Curvada Pegada Supinada com Barra",
          "Remada Unilateral com Halter","Pullover com Halter","Pullover com Barra","Remada Cavalinho",
          "Remada no Banco Inclinado com Halteres","Remada no Smith","Pulley Frente com Triângulo",
          "Remada no Cross","Puxada Invertida no Cross"]
biceps = ["Rosca Direta com Barra","Rosca Direta com Halteres","Rosca Martelo com Halteres","Rosca Direta com Barra W",
          "Rosca com Corda na Polia Baixa","Rosca com Halteres no Banco Inclinado","Rosca Martelo no Banco Inclinado com Halteres",
          "Rosca no banco Scott com a Barra W","Rosca Concentrada Unilateral com Halter"]
triceps = ["Tríceps Testa com Barra","Supino Fechado","Mergulho no Banco","Tríceps Banco","Tríceps Francês com Halter","Tríceps na Máquina",
           "Extensão de Tríceps no Cabo sob a Cabeça com Corda","Tríceps na Polia Alta com Barra Reta","Tríceps na Polia Alta com Corda"]
ombro = ["Desenvolvimento com Halteres","Desenvolvimento com Barra","Desenvolvimento Arnold","Elevação Lateral com Halteres",
         "Crucifixo Invertido com Halteres","Remada Alta com Halteres","Remada Alta no Cabo","Remada Alta no Smith",
         "Voador Invertido na Máquina"]
abdominal = ["Abdominal Invertido","Abdominal Invertido Unilateral","Abdominal Clássico","Abdominal com Apoio","Abdominal com Carga",
        "Abdominal com as Pernas Elevadas","Abdominal Supra","Abdominal Infra","Abdominal Grupado na Bola","Abdominal Invertido com Bola",
        "Abdominal com Rotação"]
quadriceps = ["Agachamento Livre com Barra","Agachamento com Halteres","Afundo","Avanço","Leg press","Agachamento Frontal","Agachamento Búlgaro",
        "Cadeira extensora","Agachamento Taça","Agachamento com Salto"]
posterior = ["Stiff","Levantamento Terra","Flexão Nórdica","Mesa Flexora","Elevação de Quadril","Agachamento Sumô",
             "Bom Dia","Mesa Flexora","Cadeira Flexora"]
gluteo = ["Chute na Polia","Elevação Pélvica","Levantamento Terra Romeno","Glúteos Máquina","Elevação de Pernas com Caneleira"]
panturrilha = ["Elevação de Panturrilha em pé no Smith","Elevação de Panturrilha Sentado no Smith","Elevação de Panturrilha no Leg Press",
               "Elevação de Panturrilha em pé","Elevação de Panturrilha em pé Unilateral"]

def criar_janela1():
    layout = [
                [sg.Text("Seja Bem-Vindo a Montagem de Treino Personalizada:")],
                [sg.Image(filename=os.path.join(dir,'Muzy.png'))],
                [sg.Button("Montar Meu Treino",key="montar"),sg.Button("Fechar",key="Fechar")],
             ]
    return sg.Window('Menu', layout, finalize=True)

def criar_janela2():
    layout = [
                [sg.Text("Escolha o seu Gênero:                                  "),sg.Combo(["Masculino","Feminino"],key="sexo")],
                [sg.Text("Escolha quantos dias você irá na academia por semana:"),sg.Combo(["1","2","3","4","5","6","7"],key="dia")],
                [sg.Button("Montar Treino",key="montagem"),sg.Button("Voltar ao Menu",key="Voltar_menu")],
             ]
    return sg.Window('Escolha de Gênero e Freqência na Academia', layout, finalize=True)

def criar_1_dia(): #A
    layout = [
                [sg.Text("",key="Divisão_treino_A")],
                [sg.Text("Exercícios:")],
                [sg.Text("",key="1° exercícioA")],
                [sg.Text("",key="2° exercícioA")],
                [sg.Text("",key="3° exercícioA")],
                [sg.Text("",key="4° exercícioA")],
                [sg.Text("",key="5° exercícioA")],
                [sg.Text("",key="6° exercícioA")],
                [sg.Text("",key="7° exercícioA")],
                [sg.Text("Obs: Realizar 3 séries de 12 repetições em cada exercício")],  
                [sg.Button("Voltar",key="Voltar1"),sg.Button("Fechar",key="Fechar1")],              
                
            ]
    return sg.Window("Treino Full Body", layout, finalize=True)

def criar_2_dia(): #A - B
    layout = [
                [sg.Text("",key="Divisão_treino_B")],
                [sg.Text("Exercícios:")],
                [sg.Text("",key="1° exercícioB")],
                [sg.Text("",key="2° exercícioB")],
                [sg.Text("",key="3° exercícioB")],
                [sg.Text("",key="4° exercícioB")],
                [sg.Text("",key="5° exercícioB")],
                [sg.Text("",key="6° exercícioB")],
                [sg.Text("",key="Divisão_treino_C")],
                [sg.Text("Exercícios:")],
                [sg.Text("",key="1° exercícioC")],
                [sg.Text("",key="2° exercícioC")],
                [sg.Text("",key="3° exercícioC")],
                [sg.Text("",key="4° exercícioC")],
                [sg.Text("",key="5° exercícioC")],
                [sg.Text("",key="6° exercícioC")],
                [sg.Text("Obs: Realizar 3 séries de 12 repetições em cada exercício")],  
                [sg.Button("Voltar",key="Voltar2"),sg.Button("Fechar",key="Fechar2")],                  
            ]
    return sg.Window("Treino A - B", layout, finalize=True)

def criar_3_dia(): #A - B - C
    layout = [
                [sg.Text("",key="Divisão_treino_D")],
                [sg.Text("Exercícios:")],
                [sg.Text("",key="1° exercícioD")],
                [sg.Text("",key="2° exercícioD")],
                [sg.Text("",key="3° exercícioD")],
                [sg.Text("",key="4° exercícioD")],
                [sg.Text("",key="5° exercícioD")],
                [sg.Text("",key="6° exercícioD")],
                [sg.Text("",key="Divisão_treino_E")],
                [sg.Text("Exercícios:")],
                [sg.Text("",key="1° exercícioE")],
                [sg.Text("",key="2° exercícioE")],
                [sg.Text("",key="3° exercícioE")],
                [sg.Text("",key="4° exercícioE")],
                [sg.Text("",key="5° exercícioE")],
                [sg.Text("",key="6° exercícioE")],
                [sg.Text("",key="Divisão_treino_F")],
                [sg.Text("Exercícios:")],
                [sg.Text("",key="1° exercícioF")],
                [sg.Text("",key="2° exercícioF")],
                [sg.Text("",key="3° exercícioF")],
                [sg.Text("",key="4° exercícioF")],
                [sg.Text("",key="5° exercícioF")],
                [sg.Text("",key="6° exercícioF")],
                [sg.Text("Obs: Realizar 3 séries de 12 repetições em cada exercício")],       
                [sg.Button("Voltar",key="Voltar3"),sg.Button("Fechar",key="Fechar3")],       
            ]
    return sg.Window("Treino A - B - C", layout, finalize=True)

def criar_4_dia(): #A - B - C - D
    
    layout = [
                [sg.Text("",key="Divisão_treino_G"),sg.Text("",key="Divisão_treino_I")],
                [sg.Text("Exercícios:"),sg.Text("Exercícios:")],
                [sg.Text("",key="1° exercícioG",size=70),sg.Text("",key="1° exercícioI",size=70)],
                [sg.Text("",key="2° exercícioG",size=70),sg.Text("",key="2° exercícioI",size=70)],
                [sg.Text("",key="3° exercícidG",size=70),sg.Text("",key="3° exercícidI",size=70)],
                [sg.Text("",key="4° exercícidG",size=70),sg.Text("",key="4° exercícidI",size=70)],
                [sg.Text("",key="5° exercícidG",size=70),sg.Text("",key="5° exercícidI",size=70)],
                [sg.Text("",key="6° exercícioG,size=70"),sg.Text("",key="6° exercícioI",size=70)],   
                [sg.Text("",key="Divisão_treino_H",size=70),sg.Text("",key="Divisão_treino_J",size=70)],
                [sg.Text("Exercícios:",size=70),sg.Text("Exercícios:",size=70)],
                [sg.Text("",key="1° exercícioH",size=70),sg.Text("",key="1° exercícioJ",size=70)],
                [sg.Text("",key="2° exercícioH",size=70),sg.Text("",key="2° exercícioJ",size=70)],
                [sg.Text("",key="3° exercícioH",size=70),sg.Text("",key="3° exercícioJ",size=70)],
                [sg.Text("",key="4° exercícioH",size=70),sg.Text("",key="4° exercícioJ",size=70)],
                [sg.Text("",key="5° exercícioH",size=70),sg.Text("",key="5° exercícioJ",size=70)],
                [sg.Text("",key="6° exercícioH",size=70),sg.Text("",key="6° exercícioJ",size=70)],            
                [sg.Text("Obs: Realizar 3 séries de 12 repetições em cada exercício")],       
                [sg.Button("Voltar",key="Voltar4"),sg.Button("Fechar",key="Fechar4")],                    
            ]
    return sg.Window("Treino A - B - C - D", layout, finalize=True)

def criar_5_dia(): #A - B - C - D - E
    layout = [[sg.Text("",key="Divisão_treino_K",size=70),sg.Text("",key="Divisão_treino_N",size=70)],
                [sg.Text("Exercícios:",size=70),sg.Text("Exercícios:",size=70)],
                [sg.Text("",key="1° exercícioK",size=70),sg.Text("",key="1° exercícioN",size=70)],
                [sg.Text("",key="2° exercícioK",size=70),sg.Text("",key="2° exercícioN",size=70)],
                [sg.Text("",key="3° exercícioK",size=70),sg.Text("",key="3° exercícioN",size=70)],
                [sg.Text("",key="4° exercícioK",size=70),sg.Text("",key="4° exercícioN",size=70)],
                [sg.Text("",key="5° exercícioK",size=70),sg.Text("",key="5° exercícioN",size=70)],
                [sg.Text("",key="6° exercícioK",size=70),sg.Text("",key="6° exercícioN",size=70)],
                [sg.Text("",key="Divisão_treino_L",size=70),sg.Text("",key="Divisão_treino_O")],
                [sg.Text("Exercícios:",size=70),sg.Text("Exercícios:")],
                [sg.Text("",key="1° exercícioL",size=70),sg.Text("",key="1° exercícioO",size=70)],
                [sg.Text("",key="2° exercícioL",size=70),sg.Text("",key="2° exercícioO",size=70)],
                [sg.Text("",key="3° exercícioL",size=70),sg.Text("",key="3° exercícioO",size=70)],
                [sg.Text("",key="4° exercícioL",size=70),sg.Text("",key="4° exercícioO",size=70)],
                [sg.Text("",key="5° exercícioL",size=70),sg.Text("",key="5° exercícioO",size=70)],
                [sg.Text("",key="6° exercícioL",size=70),sg.Text("",key="6° exercícioO",size=70)],
                [sg.Text("",key="Divisão_treino_M")],
                [sg.Text("Exercícios:")],
                [sg.Text("",key="1° exercícioM")],
                [sg.Text("",key="2° exercícioM")],
                [sg.Text("",key="3° exercícioM")],
                [sg.Text("",key="4° exercícioM")],
                [sg.Text("",key="5° exercícioM")],
                [sg.Text("",key="6° exercícioM")],   
                [sg.Text("Obs: Realizar 3 séries de 12 repetições em cada exercício")], 
                [sg.Button("Voltar",key="Voltar4"),sg.Button("Fechar",key="Fechar4")],                          
            ]
    return sg.Window("Treino A - B - C - D - E", layout, finalize=True)

def criar_6_dia(): #A - B - C - D - A - B - C
    layout = [
                [sg.Text("",key="Divisão_treino_P",size=70),sg.Text("",key="Divisão_treino_S")],
                [sg.Text("Exercícios:",size=70),sg.Text("Exercícios:",size=70)],
                [sg.Text("",key="1° exercícioP",size=70),sg.Text("",key="1° exercícioS",size=70)],
                [sg.Text("",key="2° exercícioP",size=70),sg.Text("",key="2° exercícioS",size=70)],
                [sg.Text("",key="3° exercícioP",size=70),sg.Text("",key="3° exercícioS",size=70)],
                [sg.Text("",key="4° exercícioP",size=70),sg.Text("",key="4° exercícioS",size=70)],
                [sg.Text("",key="5° exercícioP",size=70),sg.Text("",key="5° exercícioS",size=70)],
                [sg.Text("",key="6° exercícioP",size=70),sg.Text("",key="6° exercícioS",size=70)],
                [sg.Text("",key="Divisão_treino_Q",size=70),sg.Text("",key="Divisão_treino_T",size=70)],
                [sg.Text("Exercícios:",size=70),sg.Text("Exercícios:",size=70)],
                [sg.Text("",key="1° exercícioQ",size=70),sg.Text("",key="1° exercícioT",size=70)],
                [sg.Text("",key="2° exercícioQ",size=70),sg.Text("",key="2° exercícioT",size=70)],
                [sg.Text("",key="3° exercícioQ",size=70),sg.Text("",key="3° exercícioT",size=70)],
                [sg.Text("",key="4° exercícioQ",size=70),sg.Text("",key="4° exercícioT",size=70)],
                [sg.Text("",key="5° exercícioQ",size=70),sg.Text("",key="5° exercícioT",size=70)],
                [sg.Text("",key="6° exercícioQ",size=70),sg.Text("",key="6° exercícioT",size=70)],
                [sg.Text("",key="Divisão_treino_R",size=70),sg.Text("",key="Divisão_treino_U",size=70)],
                [sg.Text("Exercícios:",size=70),sg.Text("Exercícios:",size=70)],
                [sg.Text("",key="1° exercícioR",size=70),sg.Text("",key="1° exercícioU",size=70)],
                [sg.Text("",key="2° exercícioR",size=70),sg.Text("",key="2° exercícioU",size=70)],
                [sg.Text("",key="3° exercícioR",size=70),sg.Text("",key="3° exercícioU",size=70)],
                [sg.Text("",key="4° exercícioR",size=70),sg.Text("",key="4° exercícioU",size=70)],
                [sg.Text("",key="5° exercícioR",size=70),sg.Text("",key="5° exercícioU",size=70)],
                [sg.Text("",key="6° exercícioR",size=70),sg.Text("",key="6° exercícioU",size=70)], 
                [sg.Text("Obs: Realizar 3 séries de 12 repetições em cada exercício")],   
                [sg.Button("Voltar",key="Voltar6"),sg.Button("Fechar",key="Fechar6")],                      
            ]
    return sg.Window("Treino A - B - C - A - B - C", layout, finalize=True)

def criar_7_dia(): #A - B - C - D - A - B - C - Descanso
    layout = [
                [sg.Text("",key="Divisão_treino_V",size=70),sg.Text("",key="Divisão_treino_Y",size=70)],
                [sg.Text("Exercícios:",size=70),sg.Text("Exercícios:",size=70)],
                [sg.Text("",key="1° exercícioV",size=70),sg.Text("",key="1° exercícioY",size=70)],
                [sg.Text("",key="2° exercícioV",size=70),sg.Text("",key="2° exercícioY",size=70)],
                [sg.Text("",key="3° exercícioV",size=70),sg.Text("",key="3° exercícioY",size=70)],
                [sg.Text("",key="4° exercícioV",size=70),sg.Text("",key="4° exercícioY",size=70)],
                [sg.Text("",key="5° exercícioV",size=70),sg.Text("",key="5° exercícioY",size=70)],
                [sg.Text("",key="6° exercícioV",size=70),sg.Text("",key="6° exercícioY",size=70)],
                [sg.Text("",key="Divisão_treino_W",size=70),sg.Text("",key="Divisão_treino_Z",size=70)],
                [sg.Text("Exercícios:",size=70),sg.Text("Exercícios:",size=70)],
                [sg.Text("",key="1° exercícioW",size=70),sg.Text("",key="1° exercícioZ",size=70)],
                [sg.Text("",key="2° exercícioW",size=70),sg.Text("",key="2° exercícioZ",size=70)],
                [sg.Text("",key="3° exercícioW",size=70),sg.Text("",key="3° exercícioZ",size=70)],
                [sg.Text("",key="4° exercícioW",size=70),sg.Text("",key="4° exercícioZ",size=70)],
                [sg.Text("",key="5° exercícioW",size=70),sg.Text("",key="5° exercícioZ",size=70)],
                [sg.Text("",key="6° exercícioW",size=70),sg.Text("",key="6° exercícioZ",size=70)],
                [sg.Text("",key="Divisão_treino_X",size=70),sg.Text("",key="Divisão_treino_Z1",size=70)],
                [sg.Text("Exercícios:",size=70),sg.Text("Exercícios:",size=70)],
                [sg.Text("",key="1° exercícioX",size=70),sg.Text("",key="1° exercícioZ1",size=70)],
                [sg.Text("",key="2° exercícioX",size=70),sg.Text("",key="2° exercícioZ1",size=70)],
                [sg.Text("",key="3° exercícioX",size=70),sg.Text("",key="3° exercícioZ1",size=70)],
                [sg.Text("",key="4° exercícioX",size=70),sg.Text("",key="4° exercícioZ1",size=70)],
                [sg.Text("",key="5° exercícioX",size=70),sg.Text("",key="5° exercícioZ1",size=70)],
                [sg.Text("",key="6° exercícioX",size=70),sg.Text("",key="6° exercícioZ1",size=70)], 
                [sg.Text("Obs: Realizar 3 séries de 12 repetições em cada exercício")],
                [sg.Text("7° dia: Descanso")],                
                [sg.Button("Voltar",key="Voltar7"),sg.Button("Fechar",key="Fechar7")],
                ]
    return sg.Window("Treino A - B - C - A - B - C", layout, finalize=True)

janela1 = criar_janela1()
janela2 = None
janela_1_dia = None
janela_2_dia = None
janela_3_dia = None
janela_4_dia = None
janela_5_dia = None
janela_6_dia = None
janela_7_dia = None

while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 and event in (sg.WIN_CLOSED, 'Sair'):
        break

    if window == janela1:
        if event == 'montar':
            janela1.hide()
            janela2 = criar_janela2()       
        if event == "Fechar":
            break

    if window == janela2:
        if window == janela2 and event in (sg.WIN_CLOSED, 'Sair'):
            break
        if event == 'Voltar_menu':
            janela2.hide()
            janela1 = criar_janela1()  
                  
        if event == 'montagem' and values["dia"]=="1" and values["sexo"]=="Masculino":
            janela2.hide()
            janela_1_dia = criar_1_dia()
            janela_1_dia["Divisão_treino_A"].update("Treino Full Body")
            janela_1_dia["1° exercícioA"].update("- "+choice(peitoral))
            janela_1_dia["2° exercícioA"].update("- "+choice(costas))
            janela_1_dia["3° exercícioA"].update("- "+choice(biceps))
            janela_1_dia["4° exercícioA"].update("- "+choice(triceps))
            janela_1_dia["5° exercícioA"].update("- "+choice(quadriceps))
            janela_1_dia["6° exercícioA"].update("- "+choice(posterior))
            janela_1_dia["7° exercícioA"].update("- "+choice(abdominal))
            if event == "Voltar1":                
                janela_1_dia.hide()
                janela2.un_hide()
            elif event == "Fechar1":
                break          
            elif event in (sg.WIN_CLOSED, 'Fechar1'):
                break
            
        if event == 'montagem' and values["dia"]=="2" and values["sexo"]=="Masculino":
            janela2.hide()
            janela_2_dia = criar_2_dia()
            janela_2_dia["Divisão_treino_B"].update("Treino 1: Superiores")
            janela_2_dia["1° exercícioB"].update("- "+choice(peitoral))
            janela_2_dia["2° exercícioB"].update("- "+choice(costas))
            janela_2_dia["3° exercícioB"].update("- "+choice(triceps))
            janela_2_dia["4° exercícioB"].update("- "+choice(biceps))
            janela_2_dia["5° exercícioB"].update("- "+choice(ombro))
            janela_2_dia["6° exercícioB"].update("- "+choice(abdominal))
            janela_2_dia["Divisão_treino_C"].update("Treino 2: Inferiores")
            janela_2_dia["1° exercícioC"].update("- "+choice(quadriceps))
            janela_2_dia["2° exercícioC"].update("- "+choice(quadriceps))
            janela_2_dia["3° exercícioC"].update("- "+choice(posterior))
            janela_2_dia["4° exercícioC"].update("- "+choice(posterior))
            janela_2_dia["5° exercícioC"].update("- "+choice(panturrilha))
            janela_2_dia["6° exercícioC"].update("- "+choice(panturrilha))
            if event == "Voltar2":                
                janela_2_dia.hide()
                janela2.un_hide()
            elif event == "Fechar2":
                break          
            elif event in (sg.WIN_CLOSED, 'Fechar2'):
                break
            
        if event == 'montagem' and values["dia"]=="3" and values["sexo"]=="Masculino":
            janela2.hide()
            janela_3_dia = criar_3_dia()
            janela_3_dia["Divisão_treino_D"].update("Treino 1: Peito, Tríceps e Ombro")
            janela_3_dia["1° exercícioD"].update("- "+choice(peitoral))
            janela_3_dia["2° exercícioD"].update("- "+choice(peitoral))
            janela_3_dia["3° exercícioD"].update("- "+choice(triceps))
            janela_3_dia["4° exercícioD"].update("- "+choice(triceps))
            janela_3_dia["5° exercícioD"].update("- "+choice(ombro))
            janela_3_dia["6° exercícioD"].update("- "+choice(ombro))
            janela_3_dia["Divisão_treino_E"].update("Treino 2: Costas, Bíceps e Ombro")
            janela_3_dia["1° exercícioE"].update("- "+choice(costas))
            janela_3_dia["2° exercícioE"].update("- "+choice(costas))
            janela_3_dia["3° exercícioE"].update("- "+choice(costas))
            janela_3_dia["4° exercícioE"].update("- "+choice(biceps))
            janela_3_dia["5° exercícioE"].update("- "+choice(biceps))
            janela_3_dia["6° exercícioE"].update("- "+choice(abdominal))
            janela_3_dia["Divisão_treino_F"].update("Treino 3: Inferiores")
            janela_3_dia["1° exercícioF"].update("- "+choice(quadriceps))
            janela_3_dia["2° exercícioF"].update("- "+choice(quadriceps))
            janela_3_dia["3° exercícioF"].update("- "+choice(posterior))
            janela_3_dia["4° exercícioF"].update("- "+choice(posterior))
            janela_3_dia["5° exercícioF"].update("- "+choice(panturrilha))
            janela_3_dia["6° exercícioF"].update("- "+choice(panturrilha))
            if event == "Voltar3":                
                janela_3_dia.hide()
                janela2.un_hide()
            elif event == "Fechar3":
                break          
            elif event in (sg.WIN_CLOSED, 'Fechar3'):
                break
            
        if event == 'montagem' and values["dia"]=="4" and values["sexo"]=="Masculino":
            janela2.hide()
            janela_4_dia = criar_4_dia()
            janela_4_dia["Divisão_treino_G"].update("Treino 1: Peito, Tríceps e Ombro")
            janela_4_dia["1° exercícioG"].update("- "+choice(peitoral))
            janela_4_dia["2° exercícioG"].update("- "+choice(peitoral))
            janela_4_dia["3° exercícioG"].update("- "+choice(triceps))
            janela_4_dia["4° exercícioG"].update("- "+choice(triceps))
            janela_4_dia["5° exercícioG"].update("- "+choice(ombro))
            janela_4_dia["6° exercícioG"].update("- "+choice(ombro))
            janela_4_dia["Divisão_treino_H"].update("Treino 2: Quadríceps e Panturrilha")
            janela_4_dia["1° exercícioH"].update("- "+choice(quadriceps))
            janela_4_dia["2° exercícioH"].update("- "+choice(quadriceps))
            janela_4_dia["3° exercícioH"].update("- "+choice(quadriceps))
            janela_4_dia["4° exercícioH"].update("- "+choice(quadriceps))
            janela_4_dia["5° exercícioH"].update("- "+choice(panturrilha))
            janela_4_dia["6° exercícioH"].update("- "+choice(panturrilha))
            janela_4_dia["Divisão_treino_I"].update("Treino 3: Costas, Bíceps e Abdominal")
            janela_4_dia["1° exercícioI"].update("- "+choice(costas))
            janela_4_dia["2° exercícioI"].update("- "+choice(costas))
            janela_4_dia["3° exercícioI"].update("- "+choice(costas))
            janela_4_dia["4° exercícioI"].update("- "+choice(biceps))
            janela_4_dia["5° exercícioI"].update("- "+choice(biceps))
            janela_4_dia["6° exercícioI"].update("- "+choice(abdominal))    
            janela_4_dia["Divisão_treino_J"].update("Treino 4: Posterior de Coxa e Panturrilha")
            janela_4_dia["1° exercícioJ"].update("- "+choice(posterior))
            janela_4_dia["2° exercícioJ"].update("- "+choice(posterior))
            janela_4_dia["3° exercícioJ"].update("- "+choice(posterior))
            janela_4_dia["4° exercícioJ"].update("- "+choice(posterior))
            janela_4_dia["5° exercícioJ"].update("- "+choice(panturrilha))
            janela_4_dia["6° exercícioJ"].update("- "+choice(panturrilha)) 
            if event == "Voltar4":                
                janela_4_dia.hide()
                janela2.un_hide()
            elif event == "Fechar4":
                break          
            elif event in (sg.WIN_CLOSED, 'Fechar4'):
                break
            
        if event == 'montagem' and values["dia"]=="5" and values["sexo"]=="Masculino":
            janela2.hide()
            janela_5_dia = criar_5_dia()
            janela_5_dia["Divisão_treino_K"].update("Treino 1: Peito e Ombro")
            janela_5_dia["1° exercícioK"].update("- "+choice(peitoral))
            janela_5_dia["2° exercícioK"].update("- "+choice(peitoral))
            janela_5_dia["3° exercícioK"].update("- "+choice(peitoral))
            janela_5_dia["4° exercícioK"].update("- "+choice(peitoral))
            janela_5_dia["5° exercícioK"].update("- "+choice(ombro))
            janela_5_dia["6° exercícioK"].update("- "+choice(ombro))
            janela_5_dia["Divisão_treino_L"].update("Treino 2: Quadríceps e Panturrilha")
            janela_5_dia["1° exercícioL"].update("- "+choice(quadriceps))
            janela_5_dia["2° exercícioL"].update("- "+choice(quadriceps))
            janela_5_dia["3° exercícioL"].update("- "+choice(quadriceps))
            janela_5_dia["4° exercícioL"].update("- "+choice(quadriceps))
            janela_5_dia["5° exercícioL"].update("- "+choice(panturrilha))
            janela_5_dia["6° exercícioL"].update("- "+choice(panturrilha))
            janela_5_dia["Divisão_treino_M"].update("Treino 3: Costas e Abdominal")
            janela_5_dia["1° exercícioM"].update("- "+choice(costas))
            janela_5_dia["2° exercícioM"].update("- "+choice(costas))
            janela_5_dia["3° exercícioM"].update("- "+choice(costas))
            janela_5_dia["4° exercícioM"].update("- "+choice(costas))
            janela_5_dia["5° exercícioM"].update("- "+choice(abdominal))
            janela_5_dia["6° exercícioM"].update("- "+choice(abdominal))    
            janela_5_dia["Divisão_treino_N"].update("Treino 4: Posterior de Coxa e Panturrilha")
            janela_5_dia["1° exercícioN"].update("- "+choice(posterior))
            janela_5_dia["2° exercícioN"].update("- "+choice(posterior))
            janela_5_dia["3° exercícioN"].update("- "+choice(posterior))
            janela_5_dia["4° exercícioN"].update("- "+choice(posterior))
            janela_5_dia["5° exercícioN"].update("- "+choice(panturrilha))
            janela_5_dia["6° exercícioN"].update("- "+choice(panturrilha))
            janela_5_dia["Divisão_treino_O"].update("Treino 5: Tríceps e Bíceps")
            janela_5_dia["1° exercícioO"].update("- "+choice(triceps))
            janela_5_dia["2° exercícioO"].update("- "+choice(triceps))
            janela_5_dia["3° exercícioO"].update("- "+choice(triceps))
            janela_5_dia["4° exercícioO"].update("- "+choice(biceps))
            janela_5_dia["5° exercícioO"].update("- "+choice(biceps))
            janela_5_dia["6° exercícioO"].update("- "+choice(biceps))
            if event == "Voltar5":                
                janela_5_dia.hide()
                janela2.un_hide()
            elif event == "Fechar5":
                break          
            elif event in (sg.WIN_CLOSED, 'Fechar5'):
                break
            
        if event == 'montagem' and values["dia"]=="6" and values["sexo"]=="Masculino":
            janela2.hide()
            janela_6_dia = criar_6_dia()
            janela_6_dia["Divisão_treino_P"].update("Treino 1: Peito, Tríceps e Ombro")
            janela_6_dia["1° exercícioP"].update("- "+choice(peitoral))
            janela_6_dia["2° exercícioP"].update("- "+choice(peitoral))
            janela_6_dia["3° exercícioP"].update("- "+choice(triceps))
            janela_6_dia["4° exercícioP"].update("- "+choice(triceps))
            janela_6_dia["5° exercícioP"].update("- "+choice(ombro))
            janela_6_dia["6° exercícioP"].update("- "+choice(ombro))
            janela_6_dia["Divisão_treino_Q"].update("Treino 2: Costas, Bíceps e Abdominal")
            janela_6_dia["1° exercícioQ"].update("- "+choice(costas))
            janela_6_dia["2° exercícioQ"].update("- "+choice(costas))
            janela_6_dia["3° exercícioQ"].update("- "+choice(costas))
            janela_6_dia["4° exercícioQ"].update("- "+choice(biceps))
            janela_6_dia["5° exercícioQ"].update("- "+choice(biceps))
            janela_6_dia["6° exercícioQ"].update("- "+choice(abdominal))
            janela_6_dia["Divisão_treino_R"].update("Treino 3: Inferiores")
            janela_6_dia["1° exercícioR"].update("- "+choice(quadriceps))
            janela_6_dia["2° exercícioR"].update("- "+choice(quadriceps))
            janela_6_dia["3° exercícioR"].update("- "+choice(posterior))
            janela_6_dia["4° exercícioR"].update("- "+choice(posterior))
            janela_6_dia["5° exercícioR"].update("- "+choice(panturrilha))
            janela_6_dia["6° exercícioR"].update("- "+choice(panturrilha))
            janela_6_dia["Divisão_treino_S"].update("Treino 4: Peito, Tríceps e Ombro")
            janela_6_dia["1° exercícioS"].update("- "+choice(peitoral))
            janela_6_dia["2° exercícioS"].update("- "+choice(peitoral))
            janela_6_dia["3° exercícioS"].update("- "+choice(triceps))
            janela_6_dia["4° exercícioS"].update("- "+choice(triceps))
            janela_6_dia["5° exercícioS"].update("- "+choice(ombro))
            janela_6_dia["6° exercícioS"].update("- "+choice(ombro))
            janela_6_dia["Divisão_treino_T"].update("Treino 5: Costas, Bíceps e Abdominal")
            janela_6_dia["1° exercícioT"].update("- "+choice(costas))
            janela_6_dia["2° exercícioT"].update("- "+choice(costas))
            janela_6_dia["3° exercícioT"].update("- "+choice(costas))
            janela_6_dia["4° exercícioT"].update("- "+choice(biceps))
            janela_6_dia["5° exercícioT"].update("- "+choice(biceps))
            janela_6_dia["6° exercícioT"].update("- "+choice(abdominal))
            janela_6_dia["Divisão_treino_U"].update("Treino 6: Inferiores")
            janela_6_dia["1° exercícioU"].update("- "+choice(quadriceps))
            janela_6_dia["2° exercícioU"].update("- "+choice(quadriceps))
            janela_6_dia["3° exercícioU"].update("- "+choice(posterior))
            janela_6_dia["4° exercícioU"].update("- "+choice(posterior))
            janela_6_dia["5° exercícioU"].update("- "+choice(panturrilha))
            janela_6_dia["6° exercícioU"].update("- "+choice(panturrilha))
            if event == "Voltar6":                
                janela_6_dia.hide()
                janela2.un_hide()
            elif event == "Fechar6":
                break          
            elif event in (sg.WIN_CLOSED, 'Fechar6'):
                break
            
        if event == 'montagem' and values["dia"]=="7" and values["sexo"]=="Masculino":
            janela2.hide()
            janela_7_dia = criar_7_dia()
            janela_7_dia["Divisão_treino_V"].update("Treino 1: Peito, Tríceps e Ombro")
            janela_7_dia["1° exercícioV"].update("- "+choice(peitoral))
            janela_7_dia["2° exercícioV"].update("- "+choice(peitoral))
            janela_7_dia["3° exercícioV"].update("- "+choice(triceps))
            janela_7_dia["4° exercícioV"].update("- "+choice(triceps))
            janela_7_dia["5° exercícioV"].update("- "+choice(ombro))
            janela_7_dia["6° exercícioV"].update("- "+choice(ombro))
            janela_7_dia["Divisão_treino_W"].update("Treino 2: Costas, Bíceps e Abdominal")
            janela_7_dia["1° exercícioW"].update("- "+choice(costas))
            janela_7_dia["2° exercícioW"].update("- "+choice(costas))
            janela_7_dia["3° exercícioW"].update("- "+choice(costas))
            janela_7_dia["4° exercícioW"].update("- "+choice(biceps))
            janela_7_dia["5° exercícioW"].update("- "+choice(biceps))
            janela_7_dia["6° exercícioW"].update("- "+choice(abdominal))
            janela_7_dia["Divisão_treino_X"].update("Treino 3: Inferiores")
            janela_7_dia["1° exercícioX"].update("- "+choice(quadriceps))
            janela_7_dia["2° exercícioX"].update("- "+choice(quadriceps))
            janela_7_dia["3° exercícioX"].update("- "+choice(posterior))
            janela_7_dia["4° exercícioX"].update("- "+choice(posterior))
            janela_7_dia["5° exercícioX"].update("- "+choice(panturrilha))
            janela_7_dia["6° exercícioX"].update("- "+choice(panturrilha))
            janela_7_dia["Divisão_treino_Y"].update("Treino 4: Peito, Tríceps e Ombro")
            janela_7_dia["1° exercícioY"].update("- "+choice(peitoral))
            janela_7_dia["2° exercícioY"].update("- "+choice(peitoral))
            janela_7_dia["3° exercícioY"].update("- "+choice(triceps))
            janela_7_dia["4° exercícioY"].update("- "+choice(triceps))
            janela_7_dia["5° exercícioY"].update("- "+choice(ombro))
            janela_7_dia["6° exercícioY"].update("- "+choice(ombro))
            janela_7_dia["Divisão_treino_Z"].update("Treino 5: Costas, Bíceps e Abdominal")
            janela_7_dia["1° exercícioZ"].update("- "+choice(costas))
            janela_7_dia["2° exercícioZ"].update("- "+choice(costas))
            janela_7_dia["3° exercícioZ"].update("- "+choice(costas))
            janela_7_dia["4° exercícioZ"].update("- "+choice(biceps))
            janela_7_dia["5° exercícioZ"].update("- "+choice(biceps))
            janela_7_dia["6° exercícioZ"].update("- "+choice(abdominal))
            janela_7_dia["Divisão_treino_Z1"].update("Treino 6: Inferiores")
            janela_7_dia["1° exercícioZ1"].update("- "+choice(quadriceps))
            janela_7_dia["2° exercícioZ1"].update("- "+choice(quadriceps))
            janela_7_dia["3° exercícioZ1"].update("- "+choice(posterior))
            janela_7_dia["4° exercícioZ1"].update("- "+choice(posterior))
            janela_7_dia["5° exercícioZ1"].update("- "+choice(panturrilha))
            janela_7_dia["6° exercícioZ1"].update("- "+choice(panturrilha))   
            if event == "Voltar7":                
                janela_7_dia.hide()
                janela2.un_hide()
            elif event == "Fechar7":
                break          
            elif event in (sg.WIN_CLOSED, 'Fechar7'):
                break         
            
        if event == 'montagem' and values["dia"]=="1" and values["sexo"]=="Feminino":
            janela2.hide()
            janela_1_dia = criar_1_dia()
            janela_1_dia["Divisão_treino_A"].update("Treino Full Body")
            janela_1_dia["1° exercícioA"].update("- "+choice(quadriceps))
            janela_1_dia["2° exercícioA"].update("- "+choice(posterior))
            janela_1_dia["3° exercícioA"].update("- "+choice(gluteo))
            janela_1_dia["4° exercícioA"].update("- "+choice(costas))
            janela_1_dia["5° exercícioA"].update("- "+choice(triceps))
            janela_1_dia["6° exercícioA"].update("- "+choice(biceps))
            janela_1_dia["7° exercícioA"].update("- "+choice(abdominal))
            if event == "Voltar1":                
                janela_1_dia.hide()
                janela2.un_hide()
            elif event == "Fechar1":
                break          
            elif event in (sg.WIN_CLOSED, 'Fechar1'):
                break
           
        if event == 'montagem' and values["dia"]=="2" and values["sexo"]=="Feminino":
            janela2.hide()
            janela_2_dia = criar_2_dia()
            janela_2_dia["Divisão_treino_B"].update("Treino 1: Inferiores")
            janela_2_dia["1° exercícioB"].update("- "+choice(quadriceps))
            janela_2_dia["2° exercícioB"].update("- "+choice(quadriceps))
            janela_2_dia["3° exercícioB"].update("- "+choice(posterior))
            janela_2_dia["4° exercícioB"].update("- "+choice(posterior))
            janela_2_dia["5° exercícioB"].update("- "+choice(gluteo))
            janela_2_dia["6° exercícioB"].update("- "+choice(panturrilha))
            janela_2_dia["Divisão_treino_C"].update("Treino 2: Superiores")
            janela_2_dia["1° exercícioC"].update("- "+choice(costas))
            janela_2_dia["2° exercícioC"].update("- "+choice(ombro))
            janela_2_dia["3° exercícioC"].update("- "+choice(biceps))
            janela_2_dia["4° exercícioC"].update("- "+choice(triceps))
            janela_2_dia["5° exercícioC"].update("- "+choice(peitoral))
            janela_2_dia["6° exercícioC"].update("- "+choice(abdominal))
            if event == "Voltar2":                
                janela_2_dia.hide()
                janela2.un_hide()
            elif event == "Fechar2":
                break          
            elif event in (sg.WIN_CLOSED, 'Fechar2'):
                break
            
        if event == 'montagem' and values["dia"]=="3" and values["sexo"]=="Feminino":
            janela2.hide()
            janela_3_dia = criar_3_dia()
            janela_3_dia["Divisão_treino_D"].update("Treino 1: Quadríceps e panturrilha")
            janela_3_dia["1° exercícioD"].update("- "+choice(quadriceps))
            janela_3_dia["2° exercícioD"].update("- "+choice(quadriceps))
            janela_3_dia["3° exercícioD"].update("- "+choice(quadriceps))
            janela_3_dia["4° exercícioD"].update("- "+choice(quadriceps))
            janela_3_dia["5° exercícioD"].update("- "+choice(panturrilha))
            janela_3_dia["6° exercícioD"].update("- "+choice(panturrilha))
            janela_3_dia["Divisão_treino_E"].update("Treino 2: Superiores")
            janela_3_dia["1° exercícioE"].update("- "+choice(costas))
            janela_3_dia["2° exercícioE"].update("- "+choice(ombro))
            janela_3_dia["3° exercícioE"].update("- "+choice(biceps))
            janela_3_dia["4° exercícioE"].update("- "+choice(triceps))
            janela_3_dia["5° exercícioE"].update("- "+choice(peitoral))
            janela_3_dia["6° exercícioE"].update("- "+choice(abdominal))
            janela_3_dia["Divisão_treino_F"].update("Treino 3:  Glúteo, Posterior de Coxa e Abdominal")
            janela_3_dia["1° exercícioF"].update("- "+choice(gluteo))
            janela_3_dia["2° exercícioF"].update("- "+choice(gluteo))
            janela_3_dia["3° exercícioF"].update("- "+choice(gluteo))
            janela_3_dia["4° exercícioF"].update("- "+choice(posterior))
            janela_3_dia["5° exercícioF"].update("- "+choice(posterior))
            janela_3_dia["6° exercícioF"].update("- "+choice(abdominal))
            if event == "Voltar3":                
                janela_3_dia.hide()
                janela2.un_hide()
            elif event == "Fechar3":
                break          
            elif event in (sg.WIN_CLOSED, 'Fechar3'):
                break
            
        if event == 'montagem' and values["dia"]=="4" and values["sexo"]=="Feminino":
            janela2.hide()
            janela_4_dia = criar_4_dia()
            janela_4_dia["Divisão_treino_G"].update("Treino 1: Quadríceps e Panturrilha")
            janela_4_dia["1° exercícioG"].update("- "+choice(quadriceps))
            janela_4_dia["2° exercícioG"].update("- "+choice(quadriceps))
            janela_4_dia["3° exercícioG"].update("- "+choice(quadriceps))
            janela_4_dia["4° exercícioG"].update("- "+choice(quadriceps))
            janela_4_dia["5° exercícioG"].update("- "+choice(panturrilha))
            janela_4_dia["6° exercícioG"].update("- "+choice(panturrilha))
            janela_4_dia["Divisão_treino_H"].update("Treino 2: Peito, Ombro e Tríceps")
            janela_4_dia["1° exercícioH"].update("- "+choice(peitoral))
            janela_4_dia["2° exercícioH"].update("- "+choice(peitoral))
            janela_4_dia["3° exercícioH"].update("- "+choice(ombro))
            janela_4_dia["4° exercícioH"].update("- "+choice(ombro))
            janela_4_dia["5° exercícioH"].update("- "+choice(triceps))
            janela_4_dia["6° exercícioH"].update("- "+choice(triceps))
            janela_4_dia["Divisão_treino_I"].update("Treino 3: Glúteo e Posterior de Coxa")
            janela_4_dia["1° exercícioI"].update("- "+choice(gluteo))
            janela_4_dia["2° exercícioI"].update("- "+choice(gluteo))
            janela_4_dia["3° exercícioI"].update("- "+choice(gluteo))
            janela_4_dia["4° exercícioI"].update("- "+choice(posterior))
            janela_4_dia["5° exercícioI"].update("- "+choice(posterior))
            janela_4_dia["6° exercícioI"].update("- "+choice(posterior))    
            janela_4_dia["Divisão_treino_J"].update("Treino 4: Costas, Bíceps e Abdominal")
            janela_4_dia["1° exercícioJ"].update("- "+choice(costas))
            janela_4_dia["2° exercícioJ"].update("- "+choice(costas))
            janela_4_dia["3° exercícioJ"].update("- "+choice(biceps))
            janela_4_dia["4° exercícioJ"].update("- "+choice(biceps))
            janela_4_dia["5° exercícioJ"].update("- "+choice(abdominal))
            janela_4_dia["6° exercícioJ"].update("- "+choice(abdominal)) 
            if event == "Voltar4":                
                janela_4_dia.hide()
                janela2.un_hide()
            elif event == "Fechar4":
                break          
            elif event in (sg.WIN_CLOSED, 'Fechar4'):
                break
            
        if event == 'montagem' and values["dia"]=="5" and values["sexo"]=="Feminino":
            janela2.hide()
            janela_5_dia = criar_5_dia()
            janela_5_dia["Divisão_treino_K"].update("Treino 1: Quadríceps e Panturrilha")
            janela_5_dia["1° exercícioK"].update("- "+choice(quadriceps))
            janela_5_dia["2° exercícioK"].update("- "+choice(quadriceps))
            janela_5_dia["3° exercícioK"].update("- "+choice(quadriceps))
            janela_5_dia["4° exercícioK"].update("- "+choice(quadriceps))
            janela_5_dia["5° exercícioK"].update("- "+choice(panturrilha))
            janela_5_dia["6° exercícioK"].update("- "+choice(panturrilha))
            janela_5_dia["Divisão_treino_L"].update("Treino 2: Peito, Ombro e Tríceps")
            janela_5_dia["1° exercícioL"].update("- "+choice(peitoral))
            janela_5_dia["2° exercícioL"].update("- "+choice(peitoral))
            janela_5_dia["3° exercícioL"].update("- "+choice(ombro))
            janela_5_dia["4° exercícioL"].update("- "+choice(ombro))
            janela_5_dia["5° exercícioL"].update("- "+choice(triceps))
            janela_5_dia["6° exercícioL"].update("- "+choice(triceps))
            janela_5_dia["Divisão_treino_M"].update("Treino 3: Posterior de Coxa e Panturrilha")
            janela_5_dia["1° exercícioM"].update("- "+choice(posterior))
            janela_5_dia["2° exercícioM"].update("- "+choice(posterior))
            janela_5_dia["3° exercícioM"].update("- "+choice(posterior))
            janela_5_dia["4° exercícioM"].update("- "+choice(posterior))
            janela_5_dia["5° exercícioM"].update("- "+choice(panturrilha))
            janela_5_dia["6° exercícioM"].update("- "+choice(panturrilha))    
            janela_5_dia["Divisão_treino_N"].update("Treino 4: Costas e Bíceps")
            janela_5_dia["1° exercícioN"].update("- "+choice(costas))
            janela_5_dia["2° exercícioN"].update("- "+choice(costas))
            janela_5_dia["3° exercícioN"].update("- "+choice(costas))
            janela_5_dia["4° exercícioN"].update("- "+choice(costas))
            janela_5_dia["5° exercícioN"].update("- "+choice(biceps))
            janela_5_dia["6° exercícioN"].update("- "+choice(biceps))
            janela_5_dia["Divisão_treino_O"].update("Treino 5: Glúteo e Abdominal")
            janela_5_dia["1° exercícioO"].update("- "+choice(gluteo))
            janela_5_dia["2° exercícioO"].update("- "+choice(gluteo))
            janela_5_dia["3° exercícioO"].update("- "+choice(gluteo))
            janela_5_dia["4° exercícioO"].update("- "+choice(gluteo))
            janela_5_dia["5° exercícioO"].update("- "+choice(abdominal))
            janela_5_dia["6° exercícioO"].update("- "+choice(abdominal))
            if event == "Voltar5":                
                janela_5_dia.hide()
                janela2.un_hide()
            elif event == "Fechar5":
                break          
            elif event in (sg.WIN_CLOSED, 'Fechar5'):
                break
            
        if event == 'montagem' and values["dia"]=="6" and values["sexo"]=="Feminino":
            janela2.hide()
            janela_6_dia = criar_6_dia()
            janela_6_dia["Divisão_treino_P"].update("Treino 1: Quadríceps e panturrilha")
            janela_6_dia["1° exercícioP"].update("- "+choice(quadriceps))
            janela_6_dia["2° exercícioP"].update("- "+choice(quadriceps))
            janela_6_dia["3° exercícioP"].update("- "+choice(quadriceps))
            janela_6_dia["4° exercícioP"].update("- "+choice(quadriceps))
            janela_6_dia["5° exercícioP"].update("- "+choice(panturrilha))
            janela_6_dia["6° exercícioP"].update("- "+choice(panturrilha))
            janela_6_dia["Divisão_treino_Q"].update("Treino 2: Superiores")
            janela_6_dia["1° exercícioQ"].update("- "+choice(costas))
            janela_6_dia["2° exercícioQ"].update("- "+choice(ombro))
            janela_6_dia["3° exercícioQ"].update("- "+choice(biceps))
            janela_6_dia["4° exercícioQ"].update("- "+choice(triceps))
            janela_6_dia["5° exercícioQ"].update("- "+choice(peitoral))
            janela_6_dia["6° exercícioQ"].update("- "+choice(abdominal))
            janela_6_dia["Divisão_treino_R"].update("Treino 3:  Glúteo, Posterior de Coxa e Abdominal")
            janela_6_dia["1° exercícioR"].update("- "+choice(gluteo))
            janela_6_dia["2° exercícioR"].update("- "+choice(gluteo))
            janela_6_dia["3° exercícioR"].update("- "+choice(gluteo))
            janela_6_dia["4° exercícioR"].update("- "+choice(posterior))
            janela_6_dia["5° exercícioR"].update("- "+choice(posterior))
            janela_6_dia["6° exercícioR"].update("- "+choice(abdominal))
            janela_6_dia["Divisão_treino_S"].update("Treino 4: Quadríceps e panturrilha")
            janela_6_dia["1° exercícioS"].update("- "+choice(quadriceps))
            janela_6_dia["2° exercícioS"].update("- "+choice(quadriceps))
            janela_6_dia["3° exercícioS"].update("- "+choice(quadriceps))
            janela_6_dia["4° exercícioS"].update("- "+choice(quadriceps))
            janela_6_dia["5° exercícioS"].update("- "+choice(panturrilha))
            janela_6_dia["6° exercícioS"].update("- "+choice(panturrilha))
            janela_6_dia["Divisão_treino_T"].update("Treino 5: Superiores")
            janela_6_dia["1° exercícioT"].update("- "+choice(costas))
            janela_6_dia["2° exercícioT"].update("- "+choice(ombro))
            janela_6_dia["3° exercícioT"].update("- "+choice(biceps))
            janela_6_dia["4° exercícioT"].update("- "+choice(triceps))
            janela_6_dia["5° exercícioT"].update("- "+choice(peitoral))
            janela_6_dia["6° exercícioT"].update("- "+choice(abdominal))
            janela_6_dia["Divisão_treino_U"].update("Treino 6:  Glúteo, Posterior de Coxa e Abdominal")
            janela_6_dia["1° exercícioU"].update("- "+choice(gluteo))
            janela_6_dia["2° exercícioU"].update("- "+choice(gluteo))
            janela_6_dia["3° exercícioU"].update("- "+choice(gluteo))
            janela_6_dia["4° exercícioU"].update("- "+choice(posterior))
            janela_6_dia["5° exercícioU"].update("- "+choice(posterior))
            janela_6_dia["6° exercícioU"].update("- "+choice(abdominal))
            if event == "Voltar6":                
                janela_6_dia.hide()
                janela2.un_hide()
            elif event == "Fechar6":
                break          
            elif event in (sg.WIN_CLOSED, 'Fechar6'):
                break
            
        if event == 'montagem' and values["dia"]=="7" and values["sexo"]=="Feminino":
            janela2.hide()
            janela_7_dia = criar_7_dia()
            janela_7_dia["Divisão_treino_V"].update("Treino 1: Quadríceps e panturrilha")
            janela_7_dia["1° exercícioV"].update("- "+choice(quadriceps))
            janela_7_dia["2° exercícioV"].update("- "+choice(quadriceps))
            janela_7_dia["3° exercícioV"].update("- "+choice(quadriceps))
            janela_7_dia["4° exercícioV"].update("- "+choice(quadriceps))
            janela_7_dia["5° exercícioV"].update("- "+choice(panturrilha))
            janela_7_dia["6° exercícioV"].update("- "+choice(panturrilha))
            janela_7_dia["Divisão_treino_W"].update("Treino 2: Superiores")
            janela_7_dia["1° exercícioW"].update("- "+choice(costas))
            janela_7_dia["2° exercícioW"].update("- "+choice(ombro))
            janela_7_dia["3° exercícioW"].update("- "+choice(biceps))
            janela_7_dia["4° exercícioW"].update("- "+choice(triceps))
            janela_7_dia["5° exercícioW"].update("- "+choice(peitoral))
            janela_7_dia["6° exercícioW"].update("- "+choice(abdominal))
            janela_7_dia["Divisão_treino_X"].update("Treino 3:  Glúteo, Posterior de Coxa e Abdominal")
            janela_7_dia["1° exercícioX"].update("- "+choice(gluteo))
            janela_7_dia["2° exercícioX"].update("- "+choice(gluteo))
            janela_7_dia["3° exercícioX"].update("- "+choice(gluteo))
            janela_7_dia["4° exercícioX"].update("- "+choice(posterior))
            janela_7_dia["5° exercícioX"].update("- "+choice(posterior))
            janela_7_dia["6° exercícioX"].update("- "+choice(abdominal))
            janela_7_dia["Divisão_treino_Y"].update("Treino 4: Quadríceps e panturrilha")
            janela_7_dia["1° exercícioY"].update("- "+choice(quadriceps))
            janela_7_dia["2° exercícioY"].update("- "+choice(quadriceps))
            janela_7_dia["3° exercícioY"].update("- "+choice(quadriceps))
            janela_7_dia["4° exercícioY"].update("- "+choice(quadriceps))
            janela_7_dia["5° exercícioY"].update("- "+choice(panturrilha))
            janela_7_dia["6° exercícioY"].update("- "+choice(panturrilha))
            janela_7_dia["Divisão_treino_Z"].update("Treino 5: Superiores")
            janela_7_dia["1° exercícioZ"].update("- "+choice(costas))
            janela_7_dia["2° exercícioZ"].update("- "+choice(ombro))
            janela_7_dia["3° exercícioZ"].update("- "+choice(biceps))
            janela_7_dia["4° exercícioZ"].update("- "+choice(triceps))
            janela_7_dia["5° exercícioZ"].update("- "+choice(peitoral))
            janela_7_dia["6° exercícioZ"].update("- "+choice(abdominal))
            janela_7_dia["Divisão_treino_Z1"].update("Treino 6:  Glúteo, Posterior de Coxa e Abdominal")
            janela_7_dia["1° exercícioZ1"].update("- "+choice(gluteo))
            janela_7_dia["2° exercícioZ1"].update("- "+choice(gluteo))
            janela_7_dia["3° exercícioZ1"].update("- "+choice(gluteo))
            janela_7_dia["4° exercícioZ1"].update("- "+choice(posterior))
            janela_7_dia["5° exercícioZ1"].update("- "+choice(posterior))
            janela_7_dia["6° exercícioZ1"].update("- "+choice(abdominal))   
            if event == "Voltar7":                
                janela_7_dia.hide()
                janela2.un_hide()
            elif event == "Fechar7":
                break          
            elif event in (sg.WIN_CLOSED, 'Fechar7'):
                break        
        
    if window == janela_1_dia:
        if event == "Fechar":
            break
        if event in (sg.WIN_CLOSED, 'Sair'):         
            janela_1_dia.close()
            janela2.un_hide()
        
window.close()
# tesoura -> papel
# papel -> pedra
# pedra -> lagarto
# lagarto -> spock
# spock -> tesoura
# tesoura -> lagarto
# lagarto -> papel 
# papel -> spock 
# spock -> pedra 
# pedra -> tesora 

# Pedra=0
# Spock=1
# Papel=2
# Lagarto=3
# Tesoura=4

# 0-1=1
# 0-2=2
# 0-3=0
# 0-4=0
# 1-0=1
# 1-2=2
# 1-3=3
# 1-4=4
# 2-0=2
# 2-1=2
# 2-3=3
# 2-4=4
# 3-0=0
# 3-1=3
# 3-2=3
# 3-4=4
# 4-0=0
# 4-1=1
# 4-2=4
# 4-3=4

import random

ppt = input("Digite pedra, papel, tesoura, lagarto ou spock: ")

lista="pedra","papel","tesoura","lagarto","spock"
comp=random.choice(lista)
print("O computador escolheu: ",comp)

if ((comp=="pedra" and ppt=="pedra") or (comp=="tesoura" and ppt=="tesoura") or (comp=="papel" and ppt=="papel") or (comp=="lagarto" and ppt=="lagarto") or (comp=="spock" and ppt=="spock")):
    print("Empate")
elif ((ppt=="tesoura" and comp=="papel") or (ppt=="papel" and comp=="pedra") or (ppt=="pedra" and comp=="lagarto") or (ppt=="lagarto" and comp=="spock") or (ppt=="spock" and comp=="tesoura") or (ppt=="tesoura" and comp=="lagarto") or (ppt=="lagarto" and comp=="papel") or (ppt=="papel" and comp=="spock") or (ppt=="spock" and comp=="pedra") or (ppt=="pedra" and comp=="tesoura")):
    print("!Você Ganhou!")
else:
    print("!O Computador Ganhou!")

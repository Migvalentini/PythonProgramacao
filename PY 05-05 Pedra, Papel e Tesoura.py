#Desenvolva um programa que jogue esse jogo com você de acordo com as regras:
#Você escolhe uma opção;
#O computador escolhe outra;
#Seu programa diz quem ganhou

import random

ppt = input("Digite pedra, papel ou tesoura: ")

lista="pedra","papel","tesoura"
comp=random.choice(lista)
print("O computador escolheu: ",comp)

if ((comp=="pedra" and ppt=="pedra") or (comp=="tesoura" and ppt=="tesoura") or (comp=="papel" and ppt=="papel")):
    print("EMPATE")
if ((comp=="pedra" and ppt=="papel") or (comp=="tesoura" and ppt=="pedra") or (comp=="papel" and ppt=="tesoura")):
    print("!Você Ganhou!")
if ((comp=="pedra" and ppt=="tesoura") or (comp=="tesoura" and ppt=="papel") or (comp=="papel" and ppt=="pedra")):
    print("!O Computador Ganhou!")
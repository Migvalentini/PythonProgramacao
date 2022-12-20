# O produto vetorial AxB de dois vetores A=[ax,ay] e B=[bx,by] é um vetor perpendicular ao plano formado pelos vetores A e B, 
# de módulo igual a | ax*by-ay*bx|

# Faça um programa que leia as componentes ax,ay,bx e by dos vetores A e B, e calcule e escreva o módulo do vetor resultante 
# do produto vetorial.

ax = float(input("Digite um valor para ax:"))
ay = float(input("Digite um valor para ay:"))
bx = float(input("Digite um valor para bx:"))
by = float(input("Digite um valor para by:"))

resultado = abs(ax*by-ay*bx)

print("O módulo do vetor resultante do produto vetoral é:",resultado)
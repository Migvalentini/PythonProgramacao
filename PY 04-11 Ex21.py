# Faça um programa que leia 3 valores a, b e c, coeficientes de uma equação de segundo grau, 
# e calcule e escreva a soma das raízes da equação. Dica: As raízes de uma equação podem ser calculadas pela fórmula de Baskhara.
# (-b+-raizb*b-4ac)/2

from math import sqrt,pow,trunc

a = float(input("Digite o valor de a:"))
b = float(input("Digite o valor de b:"))
c = float(input("Digite o valor de c:"))

delta = (b**2)-4*a*c
raiz1 = -b+pow(delta,2)
raiz2 = -b-pow(delta,2)

resultado = trunc(raiz1 + raiz2)

print("A soma das raízes da equação é:",resultado)
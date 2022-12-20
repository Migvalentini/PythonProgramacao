# O coeficiente angular de um segmento de reta AB dado pelos pontos A(x1,y1) e B(x2,y2) representa a inclinação do segmento de reta,
#  e pode ser calculado por (y2-y1)/(x2-x1).

# Faça um programa que leia, para 3 pontos A, B e C, suas coordenadas x e y, e calcule e escreva os coeficientes angulares 
# das retas AB, BC e AC.

# (y2-y1)/(x2-x1)

Ax = int(input("Digite um valor para Ax:"))
Ay = int(input("Digite um valor para Ay:"))
Bx = int(input("Digite um valor para Bx:"))
By = int(input("Digite um valor para By:"))
Cx = int(input("Digite um valor para Cx:"))
Cy = int(input("Digite um valor para Cy:"))

AB = (By-Bx)/(Ay-Ax)
BC = (Cy-Cx)/(By-Cx)
AC = (Cy-Cx)/(Ay-Ax)

print("O coeficiente angular de AB é: ",AB)
print("O coeficiente angular de BC é: ",BC)
print("O coeficiente angular de AC é: ",AC)
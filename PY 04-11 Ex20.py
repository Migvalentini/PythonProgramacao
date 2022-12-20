# O produto escalar A.B de dois vetores A=[a1,a2,a3...] e B=[b1,b2,b3...] é dado pelo somatório 
# a1*b1+a2*b2+a3*b3+...

# Faça um programa que leia as coordenadas ax,ay,az,bx,by,bz de dois vetores no espaço tridimensional 
# e calcule e escreva seu produto escalar.

ax = float(input("Digite um valor para ax:"))
ay = float(input("Digite um valor para ax:"))
az = float(input("Digite um valor para ax:"))
bx = float(input("Digite um valor para ax:"))
by = float(input("Digite um valor para ax:"))
bz = float(input("Digite um valor para ax:"))

resultado = ax*bx+ay*by+az*bz

print("O seu produto escalar é:",resultado)
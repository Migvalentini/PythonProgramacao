#Leia 10 valores e escreva a soma dos números pares

a=float(input("Digite um número: "))
b=float(input("Digite um número: "))
c=float(input("Digite um número: "))
d=float(input("Digite um número: "))
e=float(input("Digite um número: "))
f=float(input("Digite um número: "))
g=float(input("Digite um número: "))
h=float(input("Digite um número: "))
i=float(input("Digite um número: "))
j=float(input("Digite um número: "))

aux=0

if a%2==0:
    aux=aux+a
if b%2==0:
    aux=aux+b
if c%2==0:
    aux=aux+c
if d%2==0:
    aux=aux+d
if e%2==0:
    aux=aux+e
if f%2==0:
    aux=aux+f
if g%2==0:
    aux=aux+g
if h%2==0:
    aux=aux+h
if i%2==0:
    aux=aux+i
if j%2==0:
    aux=aux+j

print("A soma dos números pares é:",aux)
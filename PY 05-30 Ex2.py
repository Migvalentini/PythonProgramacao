#Leia 5 valores e escreva quantos são múltiplos de 5

a=float(input("Digite um número: "))
b=float(input("Digite um número: "))
c=float(input("Digite um número: "))
d=float(input("Digite um número: "))
e=float(input("Digite um número: "))

m=0

if a%5==0:
    m=m+1
if b%5==0:
    m=m+1
if c%5==0:
    m=m+1
if d%5==0:
    m=m+1
if e%5==0:
    m=m+1

if m==0:
    print("Nenhum número múltiplo de 5")
elif m==1:
    print("1 número múltiplo de 5")
elif m==2:
    print("2 números múltiplos de 5")
elif m==3:
    print("3 números múltiplos de 5")
elif m==4:
    print("4 números múltiplos de 5")
else: 
    print("5 números múltiplos de 5")

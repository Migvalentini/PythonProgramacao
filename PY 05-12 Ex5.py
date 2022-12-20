import math

#1 se possui dígitos repetidos
#2 se possui dígitos consecutivos
#3 ambos
#0 ou nenhum dos dois

n=int(input("Digite um número de 4 dígitos: "))

n1=math.floor(n/1000)
r1=n%1000
n2=math.floor(r1/100)
r2=r1%100
n3=math.floor(r2/10)
r3=r2%10
n4=math.floor(r3)

aux=0
if (n1==n2) or (n1==n3) or (n1==n4) or (n2==n3) or (n2==n4) or (n3==n4):
    aux=aux=+1
if (n2-n1==1 or n2-n1==-1) or (n3-n2==1 or n3-n2==-1) or (n4-n3==1 or n4-n3==-1):
    aux=aux+2
if aux==1:
    print("1")
if aux==2:
    print("2")
if aux==3:
    print("3")
if (n1!=n2) and (n1!=n3) and (n1!=n4) and (n2!=n3) and (n2!=n4) and (n3!=n4):
    print("0")

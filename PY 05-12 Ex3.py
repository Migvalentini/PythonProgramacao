from math import floor

n=int(input("Digite um número de 6 dígitos:"))

n1=floor(n/100000)
r1=n%100000
n2=floor(r1/10000)
r2=r1%10000
n3=floor(r2/1000)
r3=r2%1000
n4=floor(r3/100)
r4=r3%100
n5=floor(r4/10)
r5=r4%10
n6=floor(r5/1)

a=n1*7
b=n2*6
c=n3*5
d=n4*4
e=n5*3
f=n6*2
produto=a+b+c+d+e+f
resto=produto%11

if resto==0 or resto==1:
    print("Dígito verificador: 0")
else:
    print("Dígito verificador:",11-resto)
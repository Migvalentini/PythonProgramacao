import math

n=int(input("Digite um número de 4 dígitos:"))

n1=math.floor(n/1000)
r1=n%1000
n2=math.floor(r1/100)
r2=r1%100
n3=math.floor(r2/10)
r3=r2%10
n4=math.floor(r3)

a=n1*1
b=n2*2
c=n3*1
d=n4*2

n1b=math.floor(b/10)
n2b=math.floor(b%10)
n1d=math.floor(d/10)
n2d=math.floor(d%10)
somatorio=a+n1b+n2b+c+n1d+n2d
resto=math.floor(somatorio%10)

if resto!=0:
    print("Digito verificador:",10-resto)
else:
    print("0")
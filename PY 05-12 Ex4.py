from math import floor

n=int(input("Digite um número de 9 dígitos: "))

n1=floor(n/100000000)
r1=n%100000000
n2=floor(r1/10000000)
r2=r1%10000000
n3=floor(r2/1000000)
r3=r2%1000000
n4=floor(r3/100000)
r4=r3%100000
n5=floor(r4/10000)
r5=r4%10000
n6=floor(r5/1000)
r6=r5%1000
n7=floor(r6/100)
r7=r6%100
n8=floor(r7/10)
r8=r7%10
n9=r8

soma=((10*n1)+(9*n2)+(8*n3)+(7*n4)+(6*n5)+(5*n6)+(4*n7)+(3*n8)+(2*n9))
resto=soma%11

if resto==0 or resto==1:
    print("Dígito verificador: 0")
else:
    print("Dígito verificador:",11-resto)
#1 – Faça um programa em Python que leia 3 valores A, B e C, lados de um triângulo, e verifique o tipo de triângulo formado escrevendo:
#"0" - se o triângulo é retângulo (A2=B2+C2);
#"1" - se o triângulo é acutângulo (A2 > B2 + C2) ;
#"2" - obtusângulo (A2 < B2 + C2).
#Lembre que, para aplicar as relações mostradas, o programa deve garantir que o maior dos 3 lados estará em A.

from math import sqrt

a=float(input("Digite A: "))
b=float(input("Digite B: "))
c=float(input("Digite C: "))

if a<b:
    aux=a
    a=b
    b=aux
if a<c:
    aux2=a
    a=c
    c=aux2

if a==sqrt(b**2+c**2):
   print("0")
elif a>sqrt(b**2+c**2):
    print("1")
elif a<sqrt(b**2+c**2):
    print("2")
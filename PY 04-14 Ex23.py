numero = int(input("Digite um número: "))

n1 = numero%1000
r1 = numero//1000
n2 = n1%100
r2 = n1//100
n3 = n2%10
r3 = n2//10
n4 = n3%1
r4 = n3//1

print("O resultado da soma dos dígitos de ",numero,"é", r1+r2+r3+r4)
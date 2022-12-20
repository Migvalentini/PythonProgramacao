reais = int(input("Digite um valor:"))

a100 = reais//100
reais = reais%100
a50 = reais//50
reais = reais%50
a20 = reais//20
reais = reais%20
a10 = reais//10
reais = reais%10
a5 = reais//5
reais = reais%5
a2 = reais//2
reais = reais%2
a1 = reais//1


print("O menor número possível de notas de 100 reais em que o valor pode ser decomposto é",a100)
print("O menor número possível de notas de 50 reais em que o valor pode ser decomposto é",a50)
print("O menor número possível de notas de 20 reais em que o valor pode ser decomposto é",a20)
print("O menor número possível de notas de 10 reais em que o valor pode ser decomposto é",a10)
print("O menor número possível de notas de 5 reais em que o valor pode ser decomposto é",a5)
print("O menor número possível de notas de 2 reais em que o valor pode ser decomposto é",a2)
print("O menor número possível de notas de 1 real em que o valor pode ser decomposto é",a1)
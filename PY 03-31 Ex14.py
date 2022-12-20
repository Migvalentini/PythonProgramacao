import math

numero = float(input("Digite um ângulo:"))

numero_r = math.radians(numero)

seno = math.sin(numero_r)
cosseno = math.cos(numero_r)
tangente = math.tan(numero_r)


print("O seno do ângulo", numero, "é",seno)
print("O cosseno do ângulo", numero, "é",cosseno)
print("A tangente do ângulo", numero, "é",tangente)
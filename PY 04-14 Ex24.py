import math

segundos = math.trunc(float(input("Digite um número: ")))

seg = segundos % 60
x = segundos // 60
min = x % 60
horas = x // 60

print(segundos,"segundos correspondem a ",horas,"horas,",min,"minutos e",seg,"segundos")
print(segundos,"segundos correspondem a ",horas,":",min,":",seg)
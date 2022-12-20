h1hora = float(input("Digite a hora1: "))
h1min = float(input("Digite o minuto1: "))
h1seg = float(input("Digite o segundo1: "))
h2hora = float(input("Digite a hora2: "))
h2min = float(input("Digite o minuto2: "))
h2seg = float(input("Digite o segundo2: "))

total = abs(h1hora*60*60-h2hora*60*60 + h1min*60-h2min*60 + h1seg-h2seg)

print("O total de segundos entre os dois horários é: ",total)
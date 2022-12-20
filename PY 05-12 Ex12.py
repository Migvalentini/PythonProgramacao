#Até 20 minutos isento
#até 1 hora R$ 9,00
#até 2 horas R$ 13,00
#3 até 16 horas R$ 2,50 a mais por hora
#17 até 24 horas preço único R$ 50,50

hora_entrada=int(input("Digite a hora de entrada: "))
minuto_entrada=int(input("Digite o minuto de entrada: "))
hora_saida=int(input("Digite a hora de saída: "))
minuto_saida=int(input("Digite o minuto de saída: "))

if hora_entrada==hora_saida and minuto_entrada!=minuto_saida:
    diferenca_minutos=minuto_saida-minuto_entrada
if hora_saida>hora_entrada and minuto_saida>minuto_entrada:
    diferenca_minutos=60*(hora_saida-hora_entrada)+minuto_saida-minuto_entrada
if hora_saida>hora_entrada and minuto_saida<minuto_entrada:
    diferenca_minutos=60*((hora_saida-1)-hora_entrada)+minuto_saida+60-minuto_entrada
if hora_saida<hora_entrada and minuto_saida>minuto_entrada:
    diferenca_minutos=60*(24-hora_entrada+hora_saida)+minuto_saida-minuto_entrada
if hora_saida<hora_entrada and minuto_saida<minuto_entrada:
    diferenca_minutos=60*(23-hora_entrada+hora_saida)+60+minuto_saida-minuto_entrada
if hora_saida==hora_entrada and minuto_entrada<minuto_saida:
    diferenca_minutos=minuto_saida-minuto_entrada
if hora_saida==hora_entrada and minuto_entrada>minuto_saida:
    diferenca_minutos=60*23+60+minuto_saida-minuto_entrada
if minuto_entrada==minuto_saida:
    diferenca_minutos=60*(hora_saida-hora_entrada)

if diferenca_minutos<=20:
    preco=0
if diferenca_minutos>20 and diferenca_minutos<=60:
    preco=9
if diferenca_minutos>60 and diferenca_minutos<=120:
    preco=13
if diferenca_minutos>120 and diferenca_minutos<=960:
    preco=2.5*(diferenca_minutos/60)+13
if diferenca_minutos>960 and diferenca_minutos<=1440:
    preco=50.50

print("A diferença entre os horários é",diferenca_minutos,"minutos")
print("O valor a ser pago é de",preco,"reais")
hora_entrada=int(input("Digite a hora de entrada: "))
minuto_entrada=int(input("Digite o minuto de entrada: "))
hora_saida=int(input("Digite a hora de saída: "))
minuto_saida=int(input("Digite o minuto de saída: "))

minutos_entrada=hora_entrada*60+minuto_entrada
minutos_saida=hora_saida*60+minuto_saida
resultado_minutos=minutos_saida-minutos_entrada
if resultado_minutos<0:
    resultado_minutos=1440+resultado_minutos

if resultado_minutos<=20:
    preco=0
if resultado_minutos>20 and resultado_minutos<=60:
    preco=9
if resultado_minutos>60 and resultado_minutos<=120:
    preco=13
if resultado_minutos>120 and resultado_minutos<=960:
    preco=2.5*(resultado_minutos/60)+13
if resultado_minutos>960 and resultado_minutos<=1440:
    preco=50.50

print("A diferença entre os horários é",resultado_minutos,"minutos")
print("O valor a ser pago é de",preco,"reais")
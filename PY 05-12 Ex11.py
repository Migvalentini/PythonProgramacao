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

print("A diferença entre os horários é",diferenca_minutos," minutos")

if diferenca_minutos<30:
    preco=15
else:
    preco=5*(diferenca_minutos//15)+15

#O custo pelo serviço nos Estados Unidos é de US$ 15 pelos primeiros 30 minutos e US$ 5 por
#cada 15 minutos adicionais. Ou seja, após os primeiros 30 minutos, a cobrança será feita a cada 15 minutos cheios

#Por exemplo, se o contratado ficou 31 minutos na fila, serão cobrados 45 minutos (20 US$), se ficou 50
#minutos serão cobrados 60 minutos (U$$ 25), e assim sucessivamente.


print("O preço a ser pago pelo serviço é de",preco,"dólares")
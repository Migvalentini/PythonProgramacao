hora_entrada=int(input("Digite a hora de entrada: "))
minuto_entrada=int(input("Digite o minuto de entrada: "))
hora_saida=int(input("Digite a hora de saída: "))
minuto_saida=int(input("Digite o minuto de saída: "))

diferenca=(hora_saida*60+minuto_saida)-(hora_entrada*60+minuto_entrada)
if diferenca<0:
    diferenca=1440+diferenca

if diferenca<60:
    preco=20
elif diferenca<120:
    preco=30
else:
    preco=5*(diferenca//60)+20
if diferenca%60!=0:
    preco=preco+5

print("A diferença é de",diferenca,"segundos")
print("O preco a ser pago é de",preco,"centavos")
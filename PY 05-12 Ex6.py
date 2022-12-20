valor_at_invest=float(input("Digite o valor atual do investimento: "))
dia_inicial=int(input("Digite o dia inicial do investimento: "))
mes_inicial=int(input("Digite o mês inicial do investimento: "))
ano_inicial=int(input("Digite o ano inicial do investimento: "))
dia_atual=int(input("Digite o dia atual do investimento: "))
mes_atual=int(input("Digite o mês atual do investimento: "))
ano_atual=int(input("Digite o ano atual do investimento: "))

if dia_atual>31 or dia_inicial>31 or mes_atual>12 or mes_inicial>12 or (dia_atual>28 and mes_atual==2) or (dia_inicial>28 and mes_inicial==2):
    print("Data inválida")

if mes_atual==mes_inicial and dia_atual<dia_inicial:
    diferenca=ano_atual-ano_inicial-1
elif mes_atual<mes_inicial:
    diferenca=ano_atual-ano_inicial-1
else: 
    diferenca=ano_atual-ano_inicial

print("A diferença entre as datas são:",diferenca,"anos")

if diferenca<2:
    print("O valor final é: ",(valor_at_invest/100)*65,"reais")
if diferenca>=2 and diferenca<4:
    print("O valor final é: ",(valor_at_invest/100)*70,"reais")
if diferenca>=4 and diferenca<6:
    print("O valor final é: ",(valor_at_invest/100)*75,"reais")
if diferenca>=6 and diferenca<8:
    print("O valor final é: ",(valor_at_invest/100)*80,"reais")
if diferenca>=8 and diferenca<10:
    print("O valor final é: ",(valor_at_invest/100)*85,"reais")
if diferenca>=10:
    print("O valor final é: ",(valor_at_invest/100)*90,"reais")
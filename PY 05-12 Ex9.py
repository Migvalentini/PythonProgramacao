from math import floor

salario=float(input("Digite o salário do funcionário: "))
dia_entrada=int(input("Digite o dia inicial do investimento: "))
mes_entrada=int(input("Digite o mês inicial do investimento: "))
ano_entrada=int(input("Digite o ano inicial do investimento: "))
dia_atual=int(input("Digite o dia atual do investimento: "))
mes_atual=int(input("Digite o mês atual do investimento: "))
ano_atual=int(input("Digite o ano atual do investimento: "))

if mes_atual==mes_entrada and dia_atual<dia_entrada:
    diferenca=ano_atual-ano_entrada-1
elif mes_atual<mes_entrada:
    diferenca=ano_atual-ano_entrada-1
else: 
    diferenca=ano_atual-ano_entrada

trienio=floor(diferenca/3)

print("O salário final do usuário é de:",floor(salario+(salario/100*trienio*2)),"reais")
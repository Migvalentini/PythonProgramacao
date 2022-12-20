#1 Uma auto locadora aluga seus carros com uma (taxa fixa por dia) mais uma (taxa por km rodado), 
# e oferece (desconto percentual sobre a taxa fixa de aluguel por dia).

#2 Escrever um algoritmo que lê a taxa fixa por dia (em reais), o percentual de desconto na taxa fixa por dia,
#  taxa por Km rodado (em reais), o número de dias e o número de Km rodados.

#3 O algoritmo deve calcular e escrever: o valor total do aluguel (já aplicado o desconto), 
# o percentual de desconto, o valor do desconto em reais, o número de dias, e a quilometragem rodada.

taxa_diaria= float(input("Digite o valor da taxa diária:"))
dias= float(input("Digite a quantidade de dias que o carro foi alugado:"))
percentual_desconto=float(input("Digite o percentual de desconto na taxa fixa por dia:"))
taxa_km=float(input("Digite a taxa por km rodado:"))
km_rodados=float(input("Digite por quantos km o carro foi alugado:"))

percentual_desconto2=taxa_diaria*(percentual_desconto/100)

total=(taxa_diaria-percentual_desconto2)*dias+(taxa_km*km_rodados)


print("O valor total gasto foi de: R$",total)
print("O percentual de desconto é de:",percentual_desconto,"%")
print("O valor do desconto em reais é de: R$",percentual_desconto)
print("O número de dias foi de:",dias)
print("A quilometragem rodada foi de:",km_rodados,"km")
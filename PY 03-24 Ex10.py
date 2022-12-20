taxa_dia = float(input("Informe a taxa fixa por dia:"))
taxa_km = float(input("Informe a taxa por km rodado:"))
#desconto sobre a taxa fixa por dia
desconto = float(input("Informe o desconto(%):"))
dias = float(input("Quantos dias usou o veículo?"))
km = float(input("Quantos quilometros percorreu?"))

total_dias = taxa_dia * dias
valor_desconto = (total_dias*desconto/100)
total_dias = total_dias - valor_desconto

total_km = taxa_km * km

total_aluguel = total_dias + total_km

print("Total do Aluguel:",total_aluguel)
print("% Desconto:",desconto,"Valor do desconto:",valor_desconto)
print(dias,"dias com o veículo!")
print(km,"km rodados!")

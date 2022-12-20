from math import floor

horas = int(input("Digite o número de horas trabalhadas:"))
valor = float(input("Digite o valor que recebe por hora:"))
tempo_anos = float(input("Digite o tempo de serviço em anos:"))

salario_bruto = horas*valor

trienio=floor(tempo_anos/3)
salario_total=(salario_bruto/100)*2*trienio+salario_bruto

if salario_total<1434:
    print("O salário líquido é:",salario_total*0)
if salario_total>=1434 and salario_total<2150:
    print("O salário líquido é:",salario_total-(salario_total/100*7.5))
if salario_total>=2150 and salario_total<2866:
    print("O salário líquido é:",salario_total-(salario_total/100*15))
if salario_total>=2866 and salario_total<3582:
    print("O salário líquido é:",salario_total-(salario_total/100*22.5))
if salario_total>=3582:
    print("O salário líquido é:",salario_total-(salario_total/100*27.5))
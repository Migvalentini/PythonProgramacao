from math import trunc

numero=int(input("Digite o número do usuário: "))
salario_bruto=float(input("Digite o salário bruto do usuário: "))

if salario_bruto<1903.98:
    IRRF=salario_bruto
elif salario_bruto>=1903.98 and salario_bruto<=2826.65:
    IRRF=salario_bruto-(salario_bruto/100*7.5)
elif salario_bruto>=2826.66 and salario_bruto<=3751.05:
    IRRF=salario_bruto-(salario_bruto/100*15)
elif salario_bruto>=3751.06 and salario_bruto<=4664.68:
    IRRF=salario_bruto-(salario_bruto/100*22.5)
else:
    IRRF=salario_bruto-(salario_bruto/100*27.5)

if IRRF<1399.12:
    INSS=IRRF-(IRRF/100*8)
elif IRRF>=1399.13 and IRRF<=2331.88:
    INSS=IRRF-(IRRF/100*9)
elif IRRF>=2331.89 and IRRF<=4663.75:
    INSS=IRRF-(IRRF/100*11)
else:
    INSS=IRRF-513.02

desconto_IRRF=salario_bruto-IRRF
desconto_INSS=IRRF-INSS

print("O número do funcionário é",numero,", o desconto do IRRF é ",desconto_IRRF,"reais, o desconto do INSS é: ",desconto_INSS,"reais e o seu salário líquido é de",trunc(INSS),"reais")
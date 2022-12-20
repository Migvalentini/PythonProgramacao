#2 - Faça um programa em Python que implemente uma calculadora de 4 operações. O programa deve ler, nessa ordem: o primeiro operando, 
# o operador (+,-,*,/) e o segundo operando, e deve escrever o resultado da operação.

operando1=float(input("Digite o operando 1: "))
operador=input("Digite o operador: ")
operando2=float(input("Digite o operador 2: "))

if operador=='+':
    print(operando1+operando2)
elif operador=='-':
    print(operando1-operando2)
elif operador=='/':
    print(operando1/operando2)
elif operador=='*':
    print(operando1*operando2)
    
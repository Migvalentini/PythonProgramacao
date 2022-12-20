from math import floor 

n=int(input("Digite um número de 8 dígitos:"))

if n>10000000 and n<99999999:
    n1=floor(n/10000000)
    r1=n%10000000
    n2=floor(r1/1000000)
    r2=r1%1000000
    n3=floor(r2/100000)
    r3=r2%100000
    n4=floor(r3/10000)
    r4=r3%10000
    n5=floor(r4/1000)
    r5=r4%1000
    n6=floor(r5/100)
    r6=r5%100
    n7=floor(r6/10)
    r7=r6%10
    n8=floor(r7/1)
    soma_pares=(n2+n4+n6)
    soma_impares=n1*3+n3*3+n5*3+n7*3
    soma=soma_pares+soma_impares
    div_int=soma%10
    fim=10-div_int

    if fim==n8:
        print("1")
    if fim!=n8:
        print("0")
else:
    print("Número inválido")    
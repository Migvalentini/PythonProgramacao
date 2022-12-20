hi=int(input("Digite a hora inicial: "))
mi=int(input("Digite o minuto inicial: "))
si=int(input("Digite o segundo inicial: "))
hf=int(input("Digite a hora final: "))
mf=int(input("Digite o minuto final: "))
sf=int(input("Digite o segundo final: "))

seg_inicial=hi*3600+mi*60+si
seg_final=hf*3600+mf*60+sf
diferenca=seg_final-seg_inicial
if diferenca<0:
    diferenca=86400+diferenca

if diferenca<=3:
    preco=0
elif 4<=diferenca<=30:
    preco=40
else: 
    preco=5*(diferenca//6)+15
if diferenca%6!=0:
    preco=preco+5

print("A diferença é de",diferenca,"segundos")
print("O preco a ser pago é de",preco,"centavos")
morango=float(input("Digite a quantidade de morangos: "))
maca=float(input("Digite a quantidade de morangos: "))
if morango<=5:
    preco_morango=2.5*morango
else:
    preco_morango=2.2*morango
if maca<=5:
    preco_maca=1.8*maca
else:
    preco_maca=1.5*maca
total_fruta=morango+maca
total_preco=preco_morango+preco_maca
if (total_fruta>8) or (total_preco>25):
    total_preco=total_preco-(total_preco/100*10)

print("O valor a ser pago é de",total_preco,"reais")
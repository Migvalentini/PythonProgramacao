codigo=float(input("Digite o código do produto:"))
quantidade=float(input("Digite a quantidade:"))

desconto=quantidade*4
if desconto>20:
    desconto=20

if codigo==100:
    print("O código do produto é 100")
    print("A quantidade de itens adquiridos foi de: ",quantidade," unidades")
    print("O preço inicial foi de: ",quantidade*1.59,"reais")
    print("O preço final foi de: ",round(quantidade*1.59-quantidade*1.59*(desconto/100),2),"reais")
if codigo==101:
    print("O código do produto é 100")
    print("A quantidade de itens adquiridos foi de: ",quantidade," unidades")
    print("O preço inicial foi de: ",quantidade*7.06,"reais")
    print("O preço final foi de: ",round(quantidade*7.06-quantidade*7.06*(desconto/100),2),"reais")
if codigo==102:
    print("O código do produto é 100")
    print("A quantidade de itens adquiridos foi de: ",quantidade," unidades")
    print("O preço inicial foi de: ",quantidade*0.07,"reais")
    print("O preço final foi de: ",round(quantidade*0.07-quantidade*0.07*(desconto/100),2),"reais")
if codigo==103:
    print("O código do produto é 100")
    print("A quantidade de itens adquiridos foi de: ",quantidade," unidades")
    print("O preço inicial foi de: ",quantidade*8.11,"reais")
    print("O preço final foi de: ",round(quantidade*8.11-quantidade*8.11*(desconto/100),2),"reais")
if codigo==104:
    print("O código do produto é 100")
    print("A quantidade de itens adquiridos foi de: ",quantidade," unidades")
    print("O preço inicial foi de: ",quantidade*4.53,"reais")
    print("O preço final foi de: ",round(quantidade*4.53-quantidade*4.53*(desconto/100),2),"reais")
if codigo==105:
    print("O código do produto é 100")
    print("A quantidade de itens adquiridos foi de: ",quantidade," unidades")
    print("O preço inicial foi de: ",quantidade*1,"reais")
    print("O preço final foi de: ",round(quantidade*1-quantidade*1*(desconto/100),2),"reais")
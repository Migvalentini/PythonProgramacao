v=float(input("Digite a velocidade do carro: "))

if v>80:
    print("MULTADO!")
    print("O valor da multa é de",(v-80)*5,"reais")
else:
    print("Parabéns, vc está andando direitnho :)")
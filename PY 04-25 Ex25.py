nome = str(input("Digite um nome: "))

print(nome.upper())
print(nome.lower())
print(len(nome)-nome.count(" "))
print(len(nome[0:nome.find(" ")]))
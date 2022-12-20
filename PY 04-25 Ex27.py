nome = str(input("Digite um nome: "))

print(nome[:nome.find(" ")])
inteiro = nome.split()
#print(format(inteiro[0]))
print(format(inteiro[len(inteiro)-1]))
#inteiro = nomes[0],[-1]
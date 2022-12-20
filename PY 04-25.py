texto = "Curso de Programação em Python"
#[C],[u],[r],[s],[o]...
#[0],[1],[2],[3],[4]
print(texto[13])
print(texto[9:13])
print(texto[11:])
print(texto[:7])

print(" ")

print(texto[3:13:2])#[Indice inicial:Indice final:salto]
print(texto.count('o'))
print(len(texto))
print(len(texto)-texto.count(" "))

print(" ")

print(texto.count("o",5,19))
print(texto.count("Prog"))
print(texto.find("o"))
print(texto.find("A"))#-1=erro
frase = texto.upper()

print(" ")

print(frase)
print(frase.find("A"))
frase = texto.lower()
print(frase)
print(texto.strip())
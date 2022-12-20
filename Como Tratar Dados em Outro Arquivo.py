arq_notas = open('notas.csv','w') #escreve no arquivo
#arq_notas = open('notas.csv','a')
#arq_notas = open('notas.csv','r')

parar = 'S'
while parar == 'S':
    nome = input("Informe o nome do aluno: ")
    nota1 = input("Informe a nota 1: ")
    nota2 = input("Informe a nota 2: ")
    nota3 = input("Informe a nota 3: ")
    arq_notas.write(nome+';'+nota1+';'+nota2+';'+nota3+'\n')

    parar = input("Deseja continuar informando valores:? (S/N) ").upper()

arq_notas.close()


arq_notas = open('notas.csv','r') #lê no arquivo

for linha in arq_notas:
    print(linha.strip())
    nomea,nota1a,nota2a,nota3a = linha.strip().split(';')
    media = (float(nota1a)+float(nota2a)+float(nota3a)/3)
    print(nomea,media)

arq_notas.close()
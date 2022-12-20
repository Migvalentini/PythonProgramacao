#Leia uma data e verifique se é uma data válida

dia=int(input("Digite o dia: "))
mes=int(input("Digite o dia: "))

meses_30="1","3","5","7","8","10","12"
meses_31="4","6","9","11"

if mes==meses_31 and dia>31:
    print("Data Inválida")
elif mes==meses_30 and dia>30:
    print("Data Inválida")
elif mes==2 and dia>28:
    print("Data Inválida")
else: 
    print("Data Válida")
s1=float(input("Digite um valor: "))
s2=float(input("Digite um valor: "))
s3=float(input("Digite um valor: "))

if s1<s2+s3 and s2<s1+s3 and s3<s1+s2:
    print("É possível fazer um triângulo com esses números")
    if s1==s2==s3:
        print("Equilátero")
    elif s1!=s2 and s2!=s3 and s1!=s3: #elif=poupa código // if ao elif são a msm coisa e o else compreende os dois
        print("Escaleno")
    else:
        print("Isósceles")
else:
    print("Não é possível fazer um triângulo com esses números")

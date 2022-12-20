from math import sqrt

N=int(input("Digite o número de degruas da escada: "))
H=float(input("Digite a altura do degrau: "))
C=float(input("Digite o comprimento do degrau: "))
L=float(input("Digite a largura do degrau: "))
diagonal=sqrt(H**2+C**2)
area_centimetros=N*L*diagonal
area=area_centimetros/100
print("A área total é de",area,"metros")
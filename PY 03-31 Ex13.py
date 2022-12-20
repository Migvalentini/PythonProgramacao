from math import trunc,sqrt,hypot

oposto = float(input("Digite o cateto oposto:"))
adjacente = float(input("Digite o cateto adjacente:"))

hipotenusa = (oposto**2+ adjacente**2)
resultado = trunc(sqrt(hipotenusa))

print(" O valor da hipotenusa é:", resultado)

#hipotenusa2 = hypot(oposto,adjacente)
#print(hipotenusa2)
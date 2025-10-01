par = int(input("Introduce un número par: "))
impar = int(input("Introduce un número impar: "))
keyImpar = False
keyPar = False


if impar % 2 != 0:
    keyImpar = True
else:
    print("El número impar no es impar")

if par % 2 == 0:
    keyPar = True
else:
    print("El número par no es par")

if keyImpar is True and keyPar is True:
    print("Correcto")
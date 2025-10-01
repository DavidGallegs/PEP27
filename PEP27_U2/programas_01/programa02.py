par = int(input("Introduce un número par: "))

if par % 2 == 0:
    impar = int(input("Introduce un número impar: "))
    if impar % 2 != 0:
        print("Correcto")
    else:
        print("El número impar no es impar")
else:
    print("El número par no es par")


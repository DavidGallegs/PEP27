numero = int(input("Introduce un número de 2 cifras: "))

decenas = numero // 10
unidades = numero % 10
numeroInv = unidades * 10 + decenas

print("El número invertido es", numeroInv)
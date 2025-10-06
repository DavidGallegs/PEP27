suma = 0
contador = 0

while True:
    numero = float(input("Introduce un número (0 para salir): "))
    if numero == 0:
        break
    suma += numero
    contador += 1

if contador > 0:
    print("Suma:", suma)
    print("Media:", suma / contador)
else:
    print("No se introdujeron números.")



# FORMA 2: SIN BREAK
numero = None
suma = 0
contador = 0

while numero != 0:
    numero = float(input("Introduce un número (0 para salir): "))
    if numero != 0:
        suma += numero
        contador += 1

if contador > 0:
    print("Suma:", suma)
    print("Media:", suma / contador)
else:
    print("No se introdujeron números.")
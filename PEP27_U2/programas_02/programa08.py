import random

numero_secreto = random.randrange(1, 21)
intentos = 3

print("Adivina un número entre 1 y 20")

while intentos > 0:
    intento = int(input("Introduce tu número: "))
    if intento == numero_secreto:
        print("Acertaste")
        break
    elif intento < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
    
    intentos -= 1
    print(f"Te quedan {intentos} intentos.\n")

if intentos == 0:
    print(f"Perdiste, el número era {numero_secreto}.")
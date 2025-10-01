dividendo = float(input("Introduce el dividendo: "))
divisor = float(input("Introduce el divisor: "))

if divisor == 0:
    print("El divisor no puede ser 0")
else:
    total = dividendo / divisor
    print("El total es: ",total)
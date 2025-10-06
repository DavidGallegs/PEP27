continuar = "s"

while continuar.lower() == "s":
    numero = 0
    while numero < 1 or numero > 10:
        numero = int(input("Introduce un número entre 1 y 10: "))

    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

    continuar = input("Quieres introducir otro número? [s/n]: ")

print("Programa finalizado.")
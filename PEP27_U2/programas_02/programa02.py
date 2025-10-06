key = False

while key == False:  # noqa: E712

    num = int(input("Introduce un número entre 1 y 10: "))
    if num > 10 or num < 1:
        print("Número incorrecto")
    else:
        key = True

print("Número correcto, fin del bucle")
    
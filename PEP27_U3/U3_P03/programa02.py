import operaciones

def main():

    resultado_suma = operaciones.sumar(10,5)
    print(f"El resultado es: {resultado_suma}")

    resultado_resta = operaciones.restar(10,5)
    print(f"El resultado es: {resultado_resta}")

    resultado_multiplicar = operaciones.multiplicacion(10,5)
    print(f"El resultado es: {resultado_multiplicar}")

    resultado_division = operaciones.division(10,5)
    print(f"El resultado es: {resultado_division}")

# Bloque para asegurar ejecución sólo si el archivo es el principal
if __name__ == "__main__":
    # Se pueden procesar argumentos, inicializar variables, etc.
    main()
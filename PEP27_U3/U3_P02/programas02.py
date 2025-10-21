import operaciones

def main():

    suma = operaciones.sumar(10,5)
    print(f"El resultado es: {suma}")

    resta = operaciones.restar(10,5)
    print(f"El resultado es: {resta}")

    multiplicacion = operaciones.multiplicacion(10,5)
    print(f"El resultado es: {multiplicacion}")

    division = operaciones.division(10,5)
    print(f"El resultado es: {division}")

if __name__ == "__main__":
    main()
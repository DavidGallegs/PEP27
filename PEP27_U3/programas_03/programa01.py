# imports de módulos propios
import matematicas

def main():
    print("""
1. Operaciones matemáticas 
2. Cálculo de áreas
3. Conversión numérica""")

    option = int(input("Elige una opción: "))

    match option:
        case 1:
            a = int(input("Introduce el primer número: "))
            b = int(input("Introduce el segundo número: "))

            print(f"Suma: {matematicas.sumar(a, b)}")
            print(f"Resta: {matematicas.restar(a, b)}")
            print(f"Multiplicación: {matematicas.multiplicacion(a, b)}")
            division = matematicas.division(a, b)

            if division is not None:
                print(f"División: {division}")
            print(f"Binario de {a}: {matematicas.a_binario(a)}")
            print(f"Hexadecimal de {a}: {matematicas.a_hexadecimal(a)}")
            print(f"Octal de {a}: {matematicas.a_octal(a)}")

        case 2:
            print("1. Rectángulo")
            print("2. Triángulo")
            print("3. Círculo")
            figura = int(input("Seleccione la figura: "))

            if figura == 1:
                base = float(input("Base: "))
                altura = float(input("Altura: "))
                print("")
                print(f"Área del rectángulo: {matematicas.area_rectangulo(base, altura)}")

            elif figura == 2:
                base = float(input("Base: "))
                altura = float(input("Altura: "))
                print(f"Área del triángulo: {matematicas.area_triangulo(base, altura)}")

            elif figura == 3:
                radio = float(input("Radio: "))
                print(f"Área del círculo: {matematicas.area_circulo(radio)}")

            else:
                print("Opcion no válida")

        case 3:
            print("1. Binario")
            print("2. Hexadecimal")
            print("3. Octal")

            tipo = int(input("Seleccione el tipo de conversión: "))
            decimal = int(input("Ingrese un número decimal: "))
            print("")

            if tipo == 1:
                print(f"Binario: {matematicas.a_binario(decimal)}")
            elif tipo == 2:
                print(f"Hexadecimal: {matematicas.a_hexadecimal(decimal)}")
            elif tipo == 3:
                print(f"Octal: {matematicas.a_octal(decimal)}")
            else:
                print("Opción no válida.")

        case _:
            print("Opción no reconocida.")


if __name__ == "__main__":
    main()
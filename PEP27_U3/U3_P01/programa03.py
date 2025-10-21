import math

def calcular_area_circulo(radio):
    return  math.pi * (radio ** 2)
def calcular_area_rectangulo(base, altura):
    return base * altura
def calcular_area_triangulo(base, altura):
    return (base * altura) /2

def mostrar_menu():

    print("1. Calcular el área de un círculo: ")
    print("2. Calcular el área de un triángulo: ")
    print("3. Calcular el área de un rectangulo: ")
    print("4. Salir: ")


def opcion1():
        try:
            radio = float(input("Introduce el radio del circulo: "))
            if radio <=0:
                print("El radio debe ser mayor que 0.")
                return
            area= calcular_area_circulo(radio)
            print(f"Área del circulo: {round(area,2)}")
        except ValueError:
                print("Entrada inválida. Debes introducir un número.")


def opcion2():
            try:
                base = float(input("Introduce la base del triángulo: "))
                altura = float(input("Introduce la altura del triángulo: "))
                if base <= 0 or altura <= 0:
                    print("La base y la altura deben ser mayores que 0.")
                    return
                area = calcular_area_triangulo(base, altura)
                print(f"Área del triángulo: {round(area, 2)}")

            except ValueError:
                print("Entrada inválida. Debes introducir números.")


def opcion3():
            try:
                base = float(input("Introduce la base del rectángulo: "))
                altura = float(input("Introduce la altura del rectángulo: "))
                if base <= 0 or altura <= 0:
                    print("La base y la altura deben ser mayores que 0.")
                    return
                area = calcular_area_rectangulo(base, altura)
                print(f"Área del rectángulo: {round(area, 2)}")

            except ValueError:
                print("Entrada inválida. Debes introducir números.")


def main():
            while True:
                mostrar_menu()
                try:
                    opcion = int(input("Introduce una opción (1-4): "))
                    if opcion == 1:
                        opcion1()
                    elif opcion == 2:
                        opcion2()
                    elif opcion == 3:
                        opcion3()
                    elif opcion == 4:
                        print("Programa terminado.")
                        break
                    else:
                        print("Opción no válida. Debes elegir entre 1 y 4.")
                except ValueError:
                    print("Entrada inválida. Debes introducir un número entero.")

# Ejecución del programa
main()
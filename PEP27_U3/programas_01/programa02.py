nombre = input("Introduce tu nombre: ")
apellido1 = input("Introduce tu primer apellido: ")
apellido2 = input("Introduce tu segundo apellido: ")

def saludar (nombre,apellido1,apellido2,curso):
    print(f"Hola {nombre} {apellido1} {apellido2} {curso}")

saludar(nombre,apellido1,apellido2, curso="2DAW")
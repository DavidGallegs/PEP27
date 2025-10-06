# FORMA 1: CON EL USO DE BREAK
while True:
    numero = int(input("Introduce un número (45 para salir): "))
    if numero == 45:
        print("Has acertado")
        break

# FORMA 2: 
numero = 0
while numero != 45:
    numero = int(input("Introduce un número (45 para salir): "))

print("Has acertado")
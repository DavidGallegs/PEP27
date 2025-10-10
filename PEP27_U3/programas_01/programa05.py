
mensaje = "Hola desde fuera"

def funcion_principal():
    saludo = "Hola desde dentro"

    def funcion_interna():
        nonlocal saludo
        saludo = "Modificado desde función interna"
        print("Dentro de interna:", saludo)

    funcion_interna()
    print("Dentro de principal:", saludo)

funcion_principal()
print("Fuera de todo:", mensaje)
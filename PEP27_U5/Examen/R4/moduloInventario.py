def crear_inventario():
    inventario = {}
    return inventario

def agregar_producto(inventario,codigo,nombre,precio_inicial):
    if codigo in inventario:
        return False
    else:
        inventario[codigo] = {"nombre":nombre,"precio_inicial":list(precio_inicial)}
        return True


def actualizar_precio(inventario,codigo,nuevo_precio):
    if codigo in inventario:
        inventario[codigo]["precio_incial"].append(nuevo_precio)
        return True
    else:
        return False

def obtener_producto(inventario,codigo,):
    if codigo in inventario:
        print(f'PRODUCTO: {inventario[codigo]["nombre"]} | PRECIO ACTUAL: {inventario[codigo]["precio_inicial"]}')
    else:
        return ""

def analizar_precios_productos(inventario,codigo):
    if codigo in inventario:
        print(f'Precios: {inventario[codigo]["precio_incial"]}')
    else:
        return False
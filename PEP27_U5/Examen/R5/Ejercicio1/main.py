import json
import os

# Uso esto para que se cree en la carpeta del programa.
from os import strerror
ruta_carpeta = os.path.dirname(__file__)
ruta_archivo = os.path.join(ruta_carpeta, "planetas.json")


planetas = [
    {"Nombre": "Marte", "Tipo":"Rocoso","Lunas":2},
    {"Nombre": "Jupiter", "Tipo":"Gaseoso","Lunas":79},
    {"Nombre": "Venus", "Tipo":"Rocoso","Lunas":0},
]

# Escribir el fichero
try:
    with open(ruta_archivo, "w", encoding="utf-8") as fichero_json:
        json.dump(planetas, fichero_json, ensure_ascii=False, indent=4)

    print(f"Archivo '{ruta_archivo}' creado correctamente.")
except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))

#Lee un fichero json
try:
    with open(ruta_archivo, "r", encoding="utf-8") as fichero_json:
        planetas = json.load(fichero_json)

    for planeta in planetas:
        print(f"{planeta['Nombre']} es de tipo {planeta['Tipo']} y tiene {planeta['Lunas']} lunas")

except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
except Exception as e:
    print("Ocurrió un error inesperado:", e)
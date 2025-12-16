import json
import os
from os import strerror

# Crear la ruta del archivo en la misma carpeta que el script
ruta_carpeta = os.path.dirname(__file__)
ruta_archivo = os.path.join(ruta_carpeta, "paises.json")

#Lee un fichero json
try:
    with open(ruta_archivo, "r", encoding="utf-8") as fichero_json:
        paises = json.load(fichero_json)

    for pais in paises:
        print(f"{pais['nombre']} está en {pais['continente']} y tiene {pais['poblacion']} millones de habitantes.")

except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
except Exception as e:
    print("Ocurrió un error inesperado:", e)

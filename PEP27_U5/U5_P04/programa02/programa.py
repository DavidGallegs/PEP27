import json
import os
from os import strerror

ruta_carpeta = os.path.dirname(__file__)
ruta_archivo = os.path.join(ruta_carpeta, "capitales.json")

capitales = [
    {"país": "Francia", "capital": "París"},
    {"país": "Australia", "capital": "Canberra"},
    {"país": "Kenia", "capital": "Nairobi"},
    {"país": "Brasil", "capital": "Brasilia"}
]

#Crea un fichero JSON
try:
    with open(ruta_archivo, "w", encoding="utf-8") as fichero_json:
        json.dump(capitales, fichero_json, ensure_ascii=False, indent=4)

    print(f"Archivo '{ruta_archivo}' creado correctamente.")
except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))

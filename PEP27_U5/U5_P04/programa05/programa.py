import json
import os
from os import strerror

# Rutas de archivos
ruta_carpeta = os.path.dirname(__file__)
ruta_entrada = os.path.join(ruta_carpeta, "../programa01/paises.json")
ruta_salida = os.path.join(ruta_carpeta, "paises_filtrados.json")

try:
    # Leer archivo original
    with open(ruta_entrada, "r", encoding="utf-8") as f:
        paises = json.load(f)

    # Pedir al usuario un continente
    continente = input("Introduce el nombre de un continente: ").strip()

    # Filtrar países por continente
    paises_filtrados = [pais for pais in paises if pais['continente'].lower() == continente.lower()]

    # Mostrar resultados
    if paises_filtrados:
        print(f"Países en {continente}:")
        for pais in paises_filtrados:
            print(f"{pais['nombre']} - {pais['poblacion']} millones de habitantes")
    else:
        print(f"No se encontraron países en {continente}.")

    # Guardar resultados en archivo JSON
    with open(ruta_salida, "w", encoding="utf-8") as f:
        json.dump(paises_filtrados, f, ensure_ascii=False, indent=4)

    print(f"Archivo '{ruta_salida}' creado correctamente con los países filtrados.")

except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
except Exception as e:
    print("Ocurrió un error inesperado:", e)

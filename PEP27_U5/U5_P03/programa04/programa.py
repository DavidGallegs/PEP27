import csv
import os

# Carpeta donde está el script
ruta_carpeta = os.path.dirname(__file__)
# Ruta completa del archivo
ruta_archivo = os.path.join(ruta_carpeta, "patrimonios.csv")

patrimonios = [
    {"Ciudad": "Roma", "País": "Italia", "Lugar emblemático": "Coliseo"},
    {"Ciudad": "El Cairo", "País": "Egipto", "Lugar emblemático": "Pirámides de Guiza"},
    {"Ciudad": "Kioto", "País": "Japón", "Lugar emblemático": "Templos históricos"}
]

cabeceras = ["Ciudad", "País", "Lugar emblemático"]

try:
    with open(ruta_archivo, "w", encoding="utf-8", newline="") as fichero_csv:
        writer = csv.DictWriter(fichero_csv, fieldnames=cabeceras, delimiter=";")

        # Escribir cabecera
        writer.writeheader()
        # Escribir filas
        writer.writerows(patrimonios)

    print(f"Archivo '{ruta_archivo}' generado correctamente.")

except IOError as e:
    print("Error durante la operación de archivos:", os.strerror(e.errno))

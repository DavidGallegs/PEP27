import csv
import os

# Carpeta donde está el script
ruta_carpeta = os.path.dirname(__file__)
# Ruta completa del archivo
ruta_archivo = os.path.join(ruta_carpeta, "capitales.csv")

capitales = [
    ["París", "Francia", "Europa"],
    ["Canberra", "Australia", "Oceanía"],
    ["Nairobi", "Kenia", "África"],
    ["Ottawa", "Canadá", "América"]
]

cabeceras = ["Ciudad", "País", "Continente"]

# Crea un fichero CSV
try:
    with open(ruta_archivo, "w", encoding="utf-8", newline="") as fichero_csv:
        writer = csv.writer(fichero_csv)
        writer.writerow(cabeceras)
        writer.writerows(capitales)

    print(f"Archivo '{ruta_archivo}' creado correctamente.")

except IOError as e:
    print("Error durante la operación de archivos:", os.strerror(e.errno))

import csv
import os

ruta = os.path.join(os.path.dirname(__file__), "../programa01/ciudades.csv")

#Lee un fichero de una carpeta y lo muestra por terminal
try:
    with open(ruta, encoding="utf-8") as fichero_csv:
        reader = csv.DictReader(fichero_csv)

        # Mostrar los nombres de las columnas
        print(f"Nombres de las columnas: {reader.fieldnames}")

        # Recorrer filas
        for fila in reader:
            print(
                f"{fila['Ciudad']} ({fila['País']}) tiene una población aproximada de {fila['Población (millones)']} millones."
            )

except IOError as e:
    print("Error durante la operación de archivos:", os.strerror(e.errno))
except Exception as e:
    print("Ocurrió un error inesperado:", e)

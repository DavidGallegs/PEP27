import os
import csv
ruta = os.path.join(os.path.dirname(__file__), "ciudades.csv")

try:
    with open(ruta, encoding="utf-8") as fichero_csv:
        reader = csv.reader(fichero_csv, delimiter=",")

        # Leer cabecera
        cabecera_fila = next(reader)
        print(f"Los nombres de las columnas son {', '.join(cabecera_fila)}")

        for fila in reader:
            print(
                f"La ciudad de {fila[0]} está en {fila[1]} y tiene {fila[2]} millones de habitantes."
            )

except IOError as e:
    print("Error durante la operación de archivos:", os.strerror(e.errno))
except Exception as e:
    print("Ocurrió un error inesperado:", e)
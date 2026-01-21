# Programa04: Consultar datos
import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host="localhost",
        port=3307,
        user="ciudades",
        password="ciudades",
        database="ciudades"
    )
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, pais, poblacion_millones FROM ciudades WHERE poblacion_millones > 25")
    resultado = cursor.fetchall()
    for fila in resultado:
        print(f"{fila[0]} ({fila[1]}) → {fila[2]} millones de habitantes")

except Error as e:
    print(f"Error: {e}")

finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()

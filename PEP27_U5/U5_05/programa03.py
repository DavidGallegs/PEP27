# Programa03: Insertar varias filas
import mysql.connector
from mysql.connector import Error

datos = [
    ("Tokio", "Japón", 37.4),
    ("Delhi", "India", 30.3),
    ("Shanghái", "China", 27.1),
    ("São Paulo", "Brasil", 22.0),
    ("Ciudad de México", "México", 21.7)
]

try:
    conexion = mysql.connector.connect(
        host="localhost",
        port=3307,
        user="ciudades",
        password="ciudades",
        database="ciudades"
    )
    cursor = conexion.cursor()
    sql = "INSERT INTO ciudades (nombre, pais, poblacion_millones) VALUES (%s, %s, %s)"
    cursor.executemany(sql, datos)
    conexion.commit()
    print(f"{cursor.rowcount} filas insertadas")

except Error as e:
    print(f"Error: {e}")

finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()

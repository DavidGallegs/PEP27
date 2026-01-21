# Programa02: Crear tabla
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
    cursor.execute("""
    CREATE TABLE ciudades (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        pais VARCHAR(50),
        poblacion_millones FLOAT
    )
    """)
    print("Tabla creada correctamente")

except Error as e:
    print(f"Error: {e}")

finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()

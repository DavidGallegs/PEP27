# Programa01: Conexión a la base de datos
import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host="localhost",
        port=3307,           # Puerto de Docker
        user="ciudades",     # Usuario creado en MySQL
        password="ciudades", # Contraseña del usuario
        database="ciudades"  # Base de datos a conectar
    )
    if conexion.is_connected():
        print("Conexión establecida correctamente")

except Error as e:
    print(f"Error de conexión: {e}")

finally:
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()

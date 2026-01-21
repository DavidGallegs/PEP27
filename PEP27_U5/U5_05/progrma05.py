# Programa05: Transacción
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
    conexion.start_transaction()

    # Insertar nueva ciudad
    cursor.execute(
        "INSERT INTO ciudades (nombre, pais, poblacion_millones) VALUES (%s, %s, %s)",
        ("Madrid", "España", 6.8)
    )

    # Borrar ciudades con población menor a 10 millones
    cursor.execute(
        "DELETE FROM ciudades WHERE poblacion_millones < 10"
    )

    conexion.commit()
    print("Transacción completada correctamente")

except Error as e:
    if 'conexion' in locals() and conexion.is_connected():
        conexion.rollback()
    print("Transacción revertida por error:", e)

finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()

import mysql.connector
from mysql.connector import Error

datos = [
    ("Marte", "Rocoso", 2),
    ("Jupiter", "Gaseoso", 79),
    ("Venus", "Rocoso", 0)
]

try:
    conexion = mysql.connector.connect(
        host="localhost",
        port=3307,
        user="planetas",
        password="planetas",
        database="planetas"
    )

    # Funciona si la tabla no existe
    cursor = conexion.cursor()
    cursor.execute("""
    CREATE TABLE planetas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        tipo VARCHAR(50),
        lunas INT
    )
    """)
    print("Tabla creada correctamente")

    cursor = conexion.cursor()
    sql = "INSERT INTO planetas (nombre, tipo, lunas) VALUES (%s, %s, %s)"
    cursor.executemany(sql, datos)
    conexion.commit()
    print(f"{cursor.rowcount} filas insertadas")

    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM planetas WHERE id = 1")
    resultado = cursor.fetchall()
    for fila in resultado:
        print(f"El nombre del planeta es {fila[0]} de tipo ({fila[1]}) con {fila[2]} lunas ")


except Error as e:
    print(f"Error: {e}")

finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()
import sqlite3


# Crear las tablas si no existen
def inicializar_base_de_datos():
    with sqlite3.connect("puntuaciones.db") as conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS jugadores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT UNIQUE
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS puntuaciones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                jugador_id INTEGER,
                puntuacion INTEGER,
                FOREIGN KEY (jugador_id) REFERENCES jugadores(id)
            )
        """)
        conexion.commit()

def guardar_puntuacion(nombre, puntuacion):
    with sqlite3.connect("puntuaciones.db") as conexion:
        cursor = conexion.cursor()

        try:
            # Insertar la puntuación en la base de datos
            cursor.execute("INSERT INTO jugadores (nombre, puntuacion) VALUES (?, ?)", (nombre, puntuacion))
            conexion.commit()
            print(f"Puntuación de {nombre} guardada correctamente.")
        except sqlite3.Error as e:
            print(f"Error al guardar la puntuación: {e}")
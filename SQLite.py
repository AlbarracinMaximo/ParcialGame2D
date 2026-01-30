import sqlite3


# # Crear las tablas si no existen
# def inicializar_base_de_datos():
#     with sqlite3.connect("puntuaciones.db") as conexion:
#         cursor = conexion.cursor()
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS jugadores (
#                 nombre TEXT PRIMARY KEY
#             )
#         """)
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS puntuaciones (
#                 jugador_nombre TEXT,
#                 puntuacion INTEGER,
#                 FOREIGN KEY (jugador_nombre) REFERENCES jugadores(nombre)
#             )
#         """)
#         conexion.commit()


# def guardar_puntuacion(nombre, puntuacion):
#     with sqlite3.connect("puntuaciones.db") as conexion:
#         cursor = conexion.cursor()

#         try:
#             # Insertar la puntuación en la base de datos
#             cursor.execute("INSERT INTO puntuaciones (jugador_nombre, puntuacion) VALUES (?, ?)", (nombre, puntuacion))
#             conexion.commit()
#             print(f"Puntuación de {nombre} guardada correctamente.")
#         except sqlite3.Error as e:
#             print(f"Error al guardar la puntuación: {e}")

def inicializar_base_de_datos():
    with sqlite3.connect("puntuaciones.db") as conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS jugadores (
                nombre TEXT PRIMARY KEY
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS puntuaciones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                jugador_nombre TEXT,
                puntuacion INTEGER,
                FOREIGN KEY (jugador_nombre) REFERENCES jugadores(nombre)
            )
        """)
        conexion.commit()

def insertar_jugador(nombre):
    with sqlite3.connect("puntuaciones.db") as conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("INSERT INTO jugadores (nombre) VALUES (?)", (nombre,))
            conexion.commit()
            print(f"Jugador {nombre} insertado correctamente.")
        except sqlite3.Error as e:
            print(f"Error al insertar jugador: {e}")

def guardar_puntuacion(nombre, puntuacion):
    with sqlite3.connect("puntuaciones.db") as conexion:
        cursor = conexion.cursor()
        try:
            # Verificar si el jugador ya está en la tabla jugadores
            cursor.execute("SELECT * FROM jugadores WHERE nombre=?", (nombre,))
            jugador = cursor.fetchone()
            if jugador is None:
                # Si el jugador no está en la tabla, insertarlo
                insertar_jugador(nombre)
            # Insertar la puntuación en la tabla puntuaciones
            cursor.execute("INSERT INTO puntuaciones (jugador_nombre, puntuacion) VALUES (?, ?)", (nombre, puntuacion))
            conexion.commit()
            print(f"Puntuación de {nombre} guardada correctamente.")
        except sqlite3.Error as e:
            print(f"Error al guardar la puntuación: {e}")
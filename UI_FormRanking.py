import pygame
from GUI_button import *
from GUI_slider import *
from GUI_textbox import *
from GUI_label import *
from GUI_form import *
from GUI_button_image import *
from Z_UI_colores import*
import sqlite3

class FormRanking(Form):
    def __init__(self, screen, x, y, w, h, active, path_image):
        super().__init__(screen, x, y, w, h, active)
        self.pantalla = screen
        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))
        self._slave = aux_imagen

        self.btn_salir = Button_Image(self._slave, x, y, 130, 331, 200, 70, r"texturas\Menu\VOLVER.png", self.btn_salir, "Volver al menu")

        self.lista_widgets.append(self.btn_salir)
        self.render()

    def btn_salir(self, param): #Volver a los ajustes 
        self.end_dialog() 

    def render(self):
        self._slave.fill(self._color_background)

    def obtener_datos_sql(self):
        """
        Obtener los datos de puntuacion de la base de datos sqlite y mostrarlos en la interfaz de usuario.
        En caso de no existir se crear un label que muestra un usuario vacio.

        Returns:
            list: Lista de tuplas con los datos de los jugadores y sus puntuaciones.
        """
        try:
            conexion = sqlite3.connect("puntuaciones.db")
        except sqlite3.Error as e:
            # Manejar el error de base de datos
            pos_inicial_x = 30
            pos_inicial_y = 0
            cadena = f"La no existe jugadores."
            pos = Label(self._slave, pos_inicial_x, pos_inicial_y, 400, 60, cadena, "Verdana", 23, (255, 255, 255), r"texturas\Menu\barra.png")
            self.lista_widgets.append(pos)

        cursor = conexion.cursor()

        try:
            cursor.execute("SELECT jugador_nombre, puntuacion FROM puntuaciones")
            datos = cursor.fetchall()

            pos_inicial_x = 30
            pos_inicial_y = 0

            # Ordenar la lista de datos por puntaje de mayor a menor
            datos_ordenados = sorted(datos, key=lambda x: x[1], reverse=True)
            # Recorrer solo los top 5 jugadores
            for i, dato in enumerate(datos_ordenados[:5], start=1):
                nombre, score = dato[0], dato[1]
                cadena = f"#{i} - Nick: {nombre}      Score: {score}"  # Sin \n\n aquí
                pos = Label(self._slave, pos_inicial_x, pos_inicial_y, 400, 60, cadena, "Verdana", 23, (255, 255, 255), r"texturas\Menu\barra.png")
                self.lista_widgets.append(pos)
                pos_inicial_y += 70
        except sqlite3.Error as e:
            # Manejar el error de no encontrar puntaje
            pos_inicial_x = 30
            pos_inicial_y = 0
            cadena = f"La no existe jugadores."
            pos = Label(self._slave, pos_inicial_x, pos_inicial_y, 400, 60, cadena, "Verdana", 23, (255, 255, 255), r"texturas\Menu\barra.png")
            self.lista_widgets.append(pos)

        conexion.close()

    def update(self, lista_eventos):
        if self.active:
            self.draw()
            self.render()
            self.obtener_datos_sql()
            for wid in self.lista_widgets:
                wid.update(lista_eventos)
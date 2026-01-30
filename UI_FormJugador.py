from GUI_textbox import TextBox
from GUI_form import Form
from GUI_button_image import Button_Image
from GUI_label import Label
from UI_Jugar import FormNiveles
from Z_UI_colores import*
import pygame

class FormJugador(Form):
    def __init__(self, screen, x, y, w, h, active,path_image):
        super().__init__(screen, x, y, w, h, active)
        self.pantalla = screen
        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))
        self._slave = aux_imagen

        self.usuario = Label(self._slave, 70, 150, 200, 40, "Nombre del jugador:", "Verdana", 18, "White", r"texturas\Menu\nada.png")
        
        self.nombre_jugador = TextBox(self._slave, x, y, 280, 155, 150, 30, color_gris_claro, blanco, "White", "White", 2, font = "Comic Sans", font_size=15, font_color= "Black" )
        self.niveles = Button_Image(self._slave, x, y, 280, 265, 170, 70, r"texturas\Menu\JUGAR.png", self.btn_play, "Niveles")
        self.btn_salir = Button_Image(self._slave, x, y, 30, 265, 200, 70, r"texturas\Menu\VOLVER.png", self.btn_salir, "Volver al menu")
        
        self.lista_widgets.append(self.usuario)
        self.lista_widgets.append(self.btn_salir)
        self.lista_widgets.append(self.nombre_jugador)
        self.lista_widgets.append(self.niveles)

    def btn_play(self, texto):
        nombre_jugador = self.nombre_jugador.get_text()
        if nombre_jugador:
            niveles = FormNiveles(self._master, 270, 230, 500, 400, True, nombre_jugador, r"texturas\Menu\panel_jugador.png")
            self.show_dialog(niveles)

    def btn_salir(self, param): #Volver a los ajustes
        self.end_dialog() 

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                for widget in self.lista_widgets: #por cada widget en la lista lo dibujo
                    widget.update(lista_eventos) # en la pantalla
        else:
            self.hijo.update(lista_eventos)
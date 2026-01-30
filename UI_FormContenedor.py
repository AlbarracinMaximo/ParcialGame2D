# import pygame
# from pygame.locals import *
import pygame
from GUI_form import Form
from GUI_button_image import Button_Image
from UI_FormPausa import FormPausa


class FormContenedorNivel(Form):
    def __init__(self, pantalla, nivel, jugador, numero_nivel):
        super().__init__(pantalla, 0, 0, pantalla.get_width(), pantalla.get_height(), color_background=None)
        nivel._slave = self._slave
        self.nivel = nivel
        self.pause = False
        self.form_pausa = None
        self.tiempo_pausa = 0  # Variable para almacenar el tiempo transcurrido durante la pausa
        self.nivel.nombre_jugador = jugador
        self.nivel.numero_nivel = numero_nivel

        self.btn_home_click = Button_Image(screen=self._slave,
                                    master_x = self._x,
                                    master_y = self._y,
                                    x= 963,
                                    y= 4,
                                    w=50, 
                                    h=50, 
                                    color_background=(255,0,0), color_border=(255,0,255), 
                                    onclick=self.btn_home_click, onclick_param="", text="", 
                                    font="Verdana", font_size=15, font_color=(0,255,0), 
                                    path_image=r"texturas\Menu\menu.png")
        self.lista_widgets.append(self.nivel)
        self.lista_widgets.append(self.btn_home_click)


    def btn_home_click(self, texto):#Volver a los ajustes
        self.tiempo_pausa = pygame.time.get_ticks() - self.nivel.tiempo_inicial
        self.pause = True  # Variable para controlar el estado de pausa
        pause = FormPausa(self._master,200, 200, 500, 600, True, self.continuar_desde_pausa, self.btn_salir_click, r"texturas\Menu\nada.png")
        self.show_dialog(pause)
    
    def continuar_desde_pausa(self):
        tiempo_actual = pygame.time.get_ticks()
        self.nivel.tiempo_inicial = tiempo_actual - self.tiempo_pausa
        self.pause = False
    
    def btn_salir_click(self):
        self.end_dialog()

    def terminar_nivel(self):
        if self.nivel.nivel_superado:
            self.end_dialog()

    def update(self, lista_eventos):
        if self.verificar_dialog_result() and not self.pause:
            #self.nivel.update(lista_eventos)
            self.terminar_nivel()
            if not self.nivel.nivel_superado:
                for wid in self.lista_widgets:
                    wid.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)
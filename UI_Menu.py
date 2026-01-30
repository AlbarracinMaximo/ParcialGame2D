import pygame, sys
from GUI_form import Form
from GUI_button_image import Button_Image
from UI_ajustes import FormAjustes
from UI_FormJugador import FormJugador
from UI_FormRanking import FormRanking
from Z_UI_colores import*


class Inicio(Form):
    def __init__(self, screen, x, y, w, h,  active, path_image):
        super().__init__(screen, x, y, w, h, active)
        self.pantalla = screen
        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))
        self._slave = aux_imagen

        self.niveles = Button_Image(self._slave, x, y, 30, 30, 117, 41, r"texturas\Menu\start.png", self.btn_play, "Niveles")
        self.btn_ajustes = Button_Image(self._slave, x, y, 30, 81, 176, 41, r"texturas\Menu\opciones.png" , self.btn_ajustes, "Ajustes")
        self.btn_ranking = Button_Image(self._slave, x, y, 30, 132, 176, 41, r"texturas\Menu\puntaje.png", self.btn_ranking, "ranking")
        self.btn_salir = Button_Image(self._slave, x, y, 30, 183, 117, 41, r"texturas\Menu\exit.png", self.btn_salir, "salir")

        self.lista_widgets.append(self.niveles)
        self.lista_widgets.append(self.btn_ajustes)
        self.lista_widgets.append(self.btn_ranking)
        self.lista_widgets.append(self.btn_salir)
        self.render()

    def update(self, lista_eventos): # actualizar elementos en mi formulario
        if self.verificar_dialog_result():
            if self.active:
                self.render()
                for widget in self.lista_widgets: #por cada widget en la lista lo dibujo
                    widget.update(lista_eventos) # en la pantalla
                self.draw() #DIBUJO el formulario
        else:
            self.hijo.update(lista_eventos)

    def btn_play(self, texto):
        ranking = FormJugador(self._master, 270, 230, 500, 400, True, r"texturas\Menu\panel_jugador.png")
        self.show_dialog(ranking)

    def btn_ajustes(self, texto):
        opciones = FormAjustes(self._master, 270, 230, 500, 400, True, r"texturas\Menu\panel_opciones.png")
        self.show_dialog(opciones)

    def render(self):
        self._slave.fill(self._color_background)

    def btn_salir(self, texto):
        pygame.quit()
        sys.exit()
    
    def btn_ranking(self, texto):
        ranking = FormRanking(self._master, 270, 230, 500, 400, True, r"texturas\Menu\panel_opciones.png")
        self.show_dialog(ranking)
        
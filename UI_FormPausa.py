import pygame, sys
from GUI_form import Form
from GUI_button_image import Button_Image
from UI_ajustes import FormAjustes
from Z_UI_colores import*


class FormPausa(Form):
    def __init__(self, screen, x, y, w, h,  active, continuar, salir, path_image):
        super().__init__(screen, x, y, w, h, active)
        self.pantalla = screen
        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))
        self._slave = aux_imagen
        self.continuar = continuar
        self.salir = salir

        self.btn_continuar = Button_Image(self._slave, x, y, 180, 30, 200, 70, r"texturas\Menu\start.png", self.btn_continuar, "Continuar")
        self.btn_ajustes = Button_Image(self._slave, x, y, 180, 100, 200, 70, r"texturas\Menu\opciones.png" , self.btn_ajustes, "Ajustes")
        self.btn_salir = Button_Image(self._slave, x, y, 180, 170, 200, 70, r"texturas\Menu\exit.png", self.btn_salir, "Volver al menu")

        self.lista_widgets.append(self.btn_continuar)
        self.lista_widgets.append(self.btn_ajustes)
        self.lista_widgets.append(self.btn_salir)
        self.render()
        
    def update(self, lista_eventos): # actualizar elementos en mi formulario
        if self.verificar_dialog_result():
            if self.active:
                self.draw() #DIBUJO el formulario
                self.render()
                for widget in self.lista_widgets: #por cada widget en la lista lo dibujo
                    widget.update(lista_eventos) # en la pantalla
        else:
            self.hijo.update(lista_eventos)

    def render(self):
        self._slave.fill(self._color_background)

    def btn_continuar(self, param):
        self.continuar()
        self.end_dialog()
    
    def btn_ajustes(self, texto):
        opciones = FormAjustes(self._master, 270, 230, 500, 400, True, r"texturas\Menu\panel_opciones.png")
        self.show_dialog(opciones)

    def btn_salir(self, param):
        self.end_dialog()
        self.salir()
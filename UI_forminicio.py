import pygame, sys
from GUI_form import Form
from GUI_button_image import Button_Image
from UI_ajustes import FormAjustes
from UI_colores import*
from UI_niveles import FormNiveles


class Inicio(Form):
    def __init__(self, screen, x, y, w, h,  active, path_image):
        super().__init__(screen, x, y, w, h, active)
        self.pantalla = screen
        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))
        self._slave = aux_imagen

        self.btn_ajustes = Button_Image(self._slave, x, y, 180, 100, 200, 70, r"C:\Users\Glewi\Desktop\parcialito\texturas\opciones.png" , self.btn_ajustes, "Ajustes")
        self.niveles = Button_Image(self._slave, x, y, 180, 30, 200, 70, r"C:\Users\Glewi\Desktop\parcialito\texturas\start.png", self.btn_play, "Niveles")
        self.btn_salir = Button_Image(self._slave, x, y, 185, 170, 200, 70, r"C:\Users\Glewi\Desktop\parcialito\texturas\exit.png", self.btn_salir, "salir")

        self.lista_widgets.append(self.niveles)
        self.lista_widgets.append(self.btn_ajustes)
        self.lista_widgets.append(self.btn_salir)
        self.render()
        
    def update(self, lista_eventos): # actualizar elementos en mi formulario
        if self.verificar_dialog_result():
            if self.active:
                self.draw() #DIBUJO el formulario
                for widget in self.lista_widgets: #por cada widget en la lista lo dibujo
                    widget.update(lista_eventos) # en la pantalla
        else:
            self.hijo.update(lista_eventos)
            
    
    def btn_play(self, texto):
        niveles = FormNiveles(self._master, 493, 229, 500, 550, None, True, r"C:\Users\Glewi\Desktop\parcialito\texturas\nada.png")
        self.show_dialog(niveles)
    
    def btn_salir(self, texto):
        pygame.quit()
        sys.exit()
    
    def btn_ajustes(self, texto):
        opciones = FormAjustes(self._master, 493, 229, 500, 550, "white", "white", 3, True)
        self.show_dialog(opciones)

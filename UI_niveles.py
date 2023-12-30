import pygame
from GUI_button_image import Button_Image
from GUI_form import Form
from UI_manejador import ManejadorNiveles
from UI_FormContenedor import FormContenedorNivel

class FormNiveles(Form):
    def __init__(self, screen, x, y, w, h, color_background, active, path_image):
        super().__init__(screen, x, y, w, h, color_background, active)
        self.manejador_niveles = ManejadorNiveles(self._slave)
        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))
        self._slave = aux_imagen
        
        self.btn_Uno = Button_Image(screen=self._slave, x=170, y=170,
                                     master_x=x, master_y=y, 
                                     w=100, h=70, color_background=(255,0,0),
                                       color_border=(255,0,255), onclick=self.manejador_nivel,
                                         onclick_param="Nivel_1", text="", font="Verdana",
                                           font_size=15, font_color=(0,255,0),
                                             path_image=r"C:\Users\Glewi\Desktop\parcialito\texturas\1.png")
        self.btn_Dos = Button_Image(screen=self._slave, x=270, y=170,
                                     master_x=x, master_y=y, w=100, h=70,
                                       color_background=(255,0,0), color_border=(255,0,255),
                                         onclick=self.manejador_nivel,
                                           onclick_param="Nivel_2", text="",
                                             font="Verdana", font_size=15,
                                               font_color=(0,255,0), path_image=r"C:\Users\Glewi\Desktop\parcialito\texturas\2.png")
        self.btn_Tres = Button_Image(screen=self._slave, x=170, y=230,
                                      master_x=x, master_y=y,
                                        w=100, h=70, color_background=(255,0,0),
                                        color_border=(255,0,255), onclick=self.manejador_nivel,
                                          onclick_param="Nivel_3", text="",
                                            font="Verdana", font_size=15,
                                            font_color=(0,255,0),
                                              path_image=r"C:\Users\Glewi\Desktop\parcialito\texturas\3.png")
        self._btn_home = Button_Image(screen=self._slave, x=160, y=300,
                                       master_x=x, master_y=y, w=270, h=80,
                                         color_background=(255,0,0), color_border=(255,0,255),
                                           onclick=self.btn_home_click, onclick_param="",
                                             text="", font="Verdana", font_size=15,
                                               font_color=(0,255,0),
                                                 path_image=r"C:\Users\Glewi\Desktop\parcialito\texturas\menu.png")
        
        self.lista_widgets.append(self.btn_Uno)
        self.lista_widgets.append(self._btn_home)
        self.lista_widgets.append(self.btn_Dos)
        self.lista_widgets.append(self.btn_Tres)


    def btn_home_click(self, param): #Volver a los ajustes      
        self.end_dialog() 


    def manejador_nivel(self, numero_nivel):
        nivel = self.manejador_niveles.get_nivel(numero_nivel)
        form_contenedor_nivel = FormContenedorNivel(self._master, nivel)
        self.show_dialog(form_contenedor_nivel)


    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                for wid in self.lista_widgets:
                    wid.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)
            






















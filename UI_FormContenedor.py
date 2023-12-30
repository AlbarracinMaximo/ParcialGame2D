from GUI_form import Form
from GUI_button_image import Button_Image

class FormContenedorNivel(Form):
    def __init__(self, pantalla, nivel):
        super().__init__(pantalla, 0, 0, pantalla.get_width(), pantalla.get_height(), color_background=None)
        nivel._slave = self._slave
        self.nivel = nivel
        
        self._btn_home = Button_Image(screen=self._slave, 
                                    master_x = self._x, 
                                    master_y = self._y, 
                                    x= 963,
                                    y= 4,
                                    w=50, 
                                    h=50, 
                                    color_background=(255,0,0), color_border=(255,0,255), 
                                    onclick=self.btn_home_click, onclick_param="", text="", 
                                    font="Verdana", font_size=15, font_color=(0,255,0), 
                                    path_image=r"C:\Users\Glewi\Desktop\parcialito\texturas\menu.png")
        #self.lista_widgets.append(self.nivel)
        self.lista_widgets.append(self._btn_home)


    def btn_home_click(self, param):#Volver a los ajustes 
        self.end_dialog() 

    def update(self, lista_eventos):
        self.nivel.update(lista_eventos)
        for wid in self.lista_widgets:
            wid.update(lista_eventos)
        self.draw()
        







import pygame
from GUI_slider import Slider
from GUI_label import Label
from GUI_form import Form
from GUI_button import Button
from GUI_button_image import Button_Image
from loads import *
from Z_UI_colores import*



class FormAjustes(Form):
    def __init__(self, screen, x, y, w, h, active, path_image):
        super().__init__(screen, x, y, w, h, active)

        #self.pantalla = screen
        self.volumen = pygame.mixer.music.get_volume()
        self.flag_play = True
        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))
        self._slave = aux_imagen
        pygame.mixer.init()

        self.apagar_prender_efectos = Label(self._slave, 40, 90, 180, 50, "Apagar/Prender efectos de sonido:", "Verdana", 15, "Black", r"texturas\Menu\nada.png")
        self.btn_play_efectos = Button(self._slave, x, y, 280, 100, 80, 30, "black", LightCoral, self.btn_play_click_efectos, "Play", "Pause",font = "Verdana", font_size=15, font_color="white")
        self.apagar_prender = Label(self._slave, 40, 140, 180, 50, "Apagar/Prender musica:", "Verdana", 15, "Black", r"texturas\Menu\nada.png")
        self.btn_play = Button(self._slave, x, y, 280, 150, 80, 30, "black", LightCoral, self.btn_play_click, "Play", "Pause",font = "Verdana", font_size=15, font_color="white")
        self.label_volumen = Label(self._slave, 280, 200, 50, 50, "", "Comic Sans", 15, negro, r"texturas\Menu\nada.png")
        self.slider_volumen = Slider(self._slave, x, y, 40, 210, 180, 15, self.volumen, blanco, negro)
        self.btn_salir = Button_Image(self._slave, x, y, 140, 302, 200, 70, r"texturas\Menu\VOLVER.png", self.btn_salir, "Volver al menu")

        pygame.mixer.music.load(r"texturas\Sounds\Musica\temaiken.mp3")#musica que quiero
        pygame.mixer.music.set_volume(self.volumen) #Volumen
        pygame.mixer.music.play(-1) # play

        self.lista_widgets = []
        self.lista_widgets.append(self.btn_salir)
        self.lista_widgets.append(self.btn_play_efectos)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.apagar_prender)
        self.lista_widgets.append(self.apagar_prender_efectos)
        self.render()

    def btn_play_click(self,texto):
        if self.flag_play:
            pygame.mixer.music.pause() #pausar musica
            self.btn_play._color_background = negro  #COLOR FONDO boton
            self.btn_play._font_color = "white" # COLOR texto
            self.btn_play.set_text("Play") #NUEVO MENSAJE
        else: #vuelvo a lo de antes
            pygame.mixer.music.unpause() # despausa musica
            self.btn_play._color_background = negro
            self.btn_play._font_color = "white"
            self.btn_play.set_text("Pause")
        self.flag_play = not self.flag_play #Bandera de cambios 
    
    def btn_play_click_efectos(self,texto):
        if self.flag_play:
            desactivar_sonidos(efectos_sonido)
            self.btn_play_efectos._color_background = negro  #COLOR FONDO boton
            self.btn_play_efectos._font_color = "white" # COLOR texto
            self.btn_play_efectos.set_text("Play") #NUEVO MENSAJE
        else: #vuelvo a lo de antes
            activar_sonidos(efectos_sonido)
            self.btn_play_efectos._color_background = negro
            self.btn_play_efectos._font_color = "white"
            self.btn_play_efectos.set_text("Pause")
        self.flag_play = not self.flag_play #Bandera de cambios 

    def update_volumen(self, lista_eventos): #AJUSTES DE VOLUMEN
        self.volumen = self.slider_volumen.value
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)

    def btn_salir(self, param): #Volver a los ajustes 
        self.end_dialog()

    def update(self, lista_eventos):
        if self.active:
            self.update_volumen(lista_eventos)
            for wid in self.lista_widgets:
                wid.update(lista_eventos)
            self.draw()
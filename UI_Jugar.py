import pygame
from GUI_button_image import Button_Image
from GUI_form import Form
from SQLite import inicializar_base_de_datos
from UI_manejador import ManejadorNiveles
from UI_FormContenedor import FormContenedorNivel
from cargar_partida import *

class FormNiveles(Form):
    def __init__(self, screen, x, y, w, h, active, jugador, path_image):
        super().__init__(screen, x, y, w, h, active)
        self.manejador_niveles = ManejadorNiveles(self._slave)
        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))
        self._slave = aux_imagen
        self.jugador = jugador

        # self.btn_Uno = Button_Image(screen=self._slave, x=49, y=98, master_x=x, master_y=y, w=390, h=70, 
        #                             onclick=self.manejador_nivel, onclick_param="Nivel_1", path_image=r"texturas\Menu\Nivel_1_1.png")
        # self.btn_Dos = Button_Image(screen=self._slave, x=49, y=189, master_x=x, master_y=y, w=390, h=70,
        #                              onclick=self.manejador_nivel, onclick_param="Nivel_2", path_image=r"texturas\Menu\Nivel_2_2.png")
        # self.btn_Tres = Button_Image(screen=self._slave, x=49, y=278,master_x=x, master_y=y,w=390, h=70,
        #                               onclick=self.manejador_nivel,onclick_param="Nivel_3",path_image=r"texturas\Menu\Nivel_3_2.png")
        self.progreso = cargar_progresos()
        nivel_1_desbloqueado = self.progreso["progresos"][0]["desbloqueado"]
        if nivel_1_desbloqueado:
            score = obtener_puntaje_nivel(1)  # Reemplaza esto con la forma en que obtienes el puntaje del jugador
            print(f"Puntaje del nivel 1: {score}")
            if score is not None and score >= 1200:
                cadena = r"texturas\Menu\Nivel_1_4.png"
            elif score is not None and score >= 950:
                cadena = r"texturas\Menu\Nivel_1_3.png"
            elif score is not None and score >= 700:
                cadena = r"texturas\Menu\Nivel_1_2.png"
            else:
                cadena = r"texturas\Menu\Nivel_1_1.png"

        self.progreso = cargar_progresos()
        nivel_2_desbloqueado = self.progreso["progresos"][1]["desbloqueado"]  
        if nivel_2_desbloqueado:
            score = obtener_puntaje_nivel(2)  # Reemplaza esto con la forma en que obtienes el puntaje del jugador
            if score is not None and score >= 1200:
                cadena_dos = r"texturas\Menu\Nivel_2_5.png"
            elif score is not None and score >= 950:
                cadena_dos = r"texturas\Menu\Nivel_2_4.png"
            elif score is not None and score >= 700:
                cadena_dos = r"texturas\Menu\Nivel_2_3.png"
            else:
                cadena_dos = r"texturas\Menu\Nivel_2_2.png"
        
        self.progreso = cargar_progresos()
        nivel_3_desbloqueado = self.progreso["progresos"][2]["desbloqueado"]
        if nivel_3_desbloqueado:
            score = obtener_puntaje_nivel(3)  # Reemplaza esto con la forma en que obtienes el puntaje del jugador
            if score is not None and score >= 1200:
                cadena_tres = r"texturas\Menu\Nivel_3_5.png"
            elif score is not None and score >= 950:
                cadena_tres = r"texturas\Menu\Nivel_3_4.png"
            elif score is not None and score >= 700:
                cadena_tres = r"texturas\Menu\Nivel_3_3.png"
            else:
                cadena_tres = r"texturas\Menu\Nivel_3_2.png"


        self.btn_Uno = Button_Image(screen=self._slave, x=49, y=98, master_x=x, master_y=y, w=390, h=70, 
                                     onclick=self.manejador_nivel, onclick_param="Nivel_1", path_image= cadena)
        self.btn_Dos = Button_Image(screen=self._slave, x=49, y=189, master_x=x, master_y=y, w=390, h=70, 
                                    onclick=self.manejador_nivel, onclick_param="Nivel_2", path_image= cadena_dos)
        self.btn_Tres = Button_Image(screen=self._slave, x=49, y=278,master_x=x, master_y=y,w=390, h=70,
                                      onclick=self.manejador_nivel,onclick_param="Nivel_3",path_image=cadena_tres)
        self.btn_salir = Button_Image(self._slave, x, y, 50, 35, 50, 30, r"texturas\Menu\flechita.png", self.btn_salir, "Volver al menu")
        
        self.lista_widgets.append(self.btn_Uno)
        self.lista_widgets.append(self.btn_Dos)
        self.lista_widgets.append(self.btn_Tres)
        
        self.lista_widgets.append(self.btn_salir)


    def btn_salir(self, param): #Volver a los ajustes      
        self.end_dialog()

    def manejador_nivel(self, numero_nivel):
        nivel = self.manejador_niveles.get_nivel(numero_nivel)
        match numero_nivel:
            case "Nivel_1":
                numero_nivel = 1
            case "Nivel_2":
                numero_nivel = 2
            case "Nivel_3":
                numero_nivel = 3
        nivel.tiempo_transcurrido = 0
        nivel.tiempo_inicial = pygame.time.get_ticks()
        inicializar_base_de_datos()
        form_contenedor_nivel = FormContenedorNivel(self._master, nivel, self.jugador, numero_nivel)
        self.show_dialog(form_contenedor_nivel)

    #def actualizar_botones_niveles_uno(self):
    #   self.progreso = cargar_progresos()
    #   for i, btn in enumerate([self.btn_Uno, self.btn_Dos, self.btn_Tres]):
    #       btn.desbloqueado = self.progreso["progresos"][i]["desbloqueado"]
    #       if btn.desbloqueado:
    #           # Si el nivel está desbloqueado, mostrar el botón correspondiente
    #           self.lista_widgets.append(btn)
    #         self.progreso = cargar_progresos()
        

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                for wid in self.lista_widgets:
                  wid.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)
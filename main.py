import pygame
from UI_forminicio import Inicio
from class_nivel1 import NivelUno
from class_nivel2 import NivelDos
from class_nivel3 import NivelTres
pygame.font.init()
from pygame.locals import *
from bala import *
#from personaje_principal import Personaje
from personaje_principal_copy import Personaje
from loads import *
from Modo import *
from premio import Premio
import random
from enemigo import Enemigo
from spawn import *
from moneda import *
from trampa import *
from vida import *
from plataformas import *
from plataforma_movible import *
import re
import pygame, sys
from GUI_form import Form
from GUI_button_image import Button_Image
from UI_ajustes import FormAjustes  
from UI_colores import*
from UI_niveles import FormNiveles


pygame.init()
pygame.mixer.init()


#Config de pantalla
W, H = 1024, 720
FPS = 30
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((W, H))


pygame.display.set_caption("Juego.exe")
pygame.display.set_icon(icono)
# Fondo
fondo = pygame.image.load(r"texturas\fondo.png")
fondo = pygame.transform.scale(fondo, (W,H))

#Cancion
cancion = r"texturas\temaiken.mp3"
pygame.mixer.music.load(cancion)
pygame.mixer.music.play(-1)

formulario = Inicio(PANTALLA,0, 0, 1024, 720, True, r"texturas\fondo.png")
nivel_actual = NivelUno(PANTALLA)

while True:
    RELOJ.tick(FPS)
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == QUIT:
            pygame.quit()
            sys.exit(0)

    #nivel_actual.update(eventos)
    formulario.update(eventos)

    pygame.display.update()

pygame.quit()
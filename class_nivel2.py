import pygame
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
from nivel import *
from Boss import *

class NivelDos(Nivel):
    def __init__ (self,pantalla:pygame.Surface):
        #Inicializa pygame
        pygame.init()
        pygame.mixer.init()
        #Config de pantalla
        W = pantalla.get_width()
        H = pantalla.get_height()
        
        #FONDO
        fondo = pygame.image.load(r"texturas\lvl_2.png").convert()
        fondo = pygame.transform.scale(fondo, (W, H))

        #Movimientos del jugador del jugador
        acciones = {}
        acciones["Quieto"] = personaje_quieto
        acciones["Derecha"] = personaje_camina_derecha
        acciones["Izquierda"] = personaje_camina_izquierda
        acciones["Salta"] = personaje_salta
        acciones["Super_Quieto"] = personaje_poderoso_quieto
        acciones["Super_Derecha"] = personaje_poderoso_derecha
        acciones["Super_Izquierda"] = personaje_poderoso_izquierda
        acciones["Super_Salta"] = personaje_poderoso_salta
        acciones["Muriendo"] = personaje_muriendo
        acciones["Muerto"] = personaje_muerto

        #Heroe
        player = Personaje(acciones, 5, (40, 40), (24, 445))

        # Crear ubicaciones aleatorias
        ubicaciones_aleatorias = [(167, 600), (390, 430), (780, 345), (935, 595)]

        #respawn
        respawn = Respawn(player,ubicaciones_aleatorias)

        #Enemigos
        diccionario_animaciones = {}
        diccionario_animaciones["derecha"] = enemigo_camina_derecha
        diccionario_animaciones["izquierda"] = enemigo_camina_izquierda
        diccionario_animaciones["muere"] = enemigo_aplasta

        d = {"muere": diccionario_animaciones["muere"]}
        reescalar_imagenes(d, 20, 20)

        bala_manager = BalaManager(respawn, player)

        moneda1 = Moneda((27, 27), 50, (480, 530), r"texturas\coin.png")
        moneda2 = Moneda((27, 27), 50, (590, 530), r"texturas\coin.png")
        moneda3 = Moneda((27, 27), 50, (955, 555), r"texturas\coin.png")
        moneda4 = Moneda((27, 27), 50, (700, 335), r"texturas\coin.png")
        moneda5 = Moneda((27, 27), 50, (900, 335), r"texturas\coin.png")
        moneda6 = Moneda((27, 27), 50, (700, 530), r"texturas\coin.png")
        moneda7 = Moneda((27, 27), 50, (160, 150), r"texturas\coin.png")
        moneda8 = Moneda((27, 27), 50, (245, 150), r"texturas\coin.png")
        moneda9 = Moneda((27, 27), 50, (200, 480), r"texturas\coin.png")
        moneda10 = Moneda((27, 27), 50, (920, 555), r"texturas\coin.png")

        # Lista de monedas
        lista_monedas = [moneda1, moneda2,moneda3,moneda4,moneda5,moneda6,moneda7,moneda8,moneda9,moneda10]

        #Lista plataformas
        plataformas = [piso_cueva_bajo_uno, piso_cueva_bajo_dos,
                        piso_cueva_media_dos, piso_cueva_media_dos, piso_cueva_alta,
                        piso_cueva_alta,piso_casa]
        
        plataformas_movibles = [piso_inmovil,plataforma_dos]

        flag_disparo = False
        tiempo_ultimo_disparo = 0 #Si pongo 0 es consecutivo

        # Definición del cronómetro
        duracion_maxima = 75000 # 1 minutos en milisegundos
        inicializar_base_de_datos()
        super().__init__(fondo,pantalla, player,plataformas,plataformas_movibles, respawn, bala_manager, lista_monedas, fondo, diccionario_animaciones, tiempo_ultimo_disparo, flag_disparo, duracion_maxima)
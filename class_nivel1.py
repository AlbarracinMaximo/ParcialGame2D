import pygame

from enemigo_volador import EnemigoVolador
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

class NivelUno(Nivel):
    def __init__ (self,pantalla:pygame.Surface):
        #Inicializa pygame
        pygame.init()
        pygame.mixer.init()
        #Config de pantalla
        W = 1024
        H = 720
        
        #FONDO
        fondo = pygame.image.load(r"texturas\Mapas\Pantalla\level_1.5.2.png").convert()
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
        player = Personaje(acciones, 5, (40, 40), (302, 589))

        # Crear ubicaciones aleatorias
        ubicaciones_aleatorias = [(60, 408), (271, 600), (630, 597), (400, 168)]
        ojo_aleatorio = [(60, 200), (800, 200)]

        #respawn
        respawn = Respawn(player,ubicaciones_aleatorias,ojo_aleatorio)

        #Enemigos
        diccionario_animaciones = {}
        diccionario_animaciones["Derecha"] = enemigo_camina_derecha
        diccionario_animaciones["Izquierda"] = enemigo_camina_izquierda
        diccionario_animaciones["Muere"] = enemigo_aplasta

        bala_manager = BalaManager(respawn, player)
        #bala_manager_enemigo = BalaEnemigo()

        moneda1 = Moneda((27, 27), 50, (360, 90), coin)
        moneda2 = Moneda((27, 27), 50, (20, 300), coin)
        moneda3 = Moneda((27, 27), 50, (60, 300), coin)
        moneda4 = Moneda((27, 27), 50, (655, 240), coin)
        moneda5 = Moneda((27, 27), 50, (800, 240), coin)
        moneda6 = Moneda((27, 27), 50, (600, 500), coin)
        moneda7 = Moneda((27, 27), 50, (715, 500), coin)
        moneda8 = Moneda((27, 27), 50, (880, 500), coin)
        moneda9 = Moneda((27, 27), 50, (450, 90), coin)
        moneda10 = Moneda((27, 27), 50, (214, 485), coin)

        # Lista de monedas
        lista_monedas = [moneda1, moneda2,moneda3,moneda4,moneda5,moneda6,moneda7,moneda8,moneda9,moneda10]

        #Lista plataformas
        plataformas = [piso_bajo_uno, piso_bajo_dos,
                    piso_medio, muro_medio_derecho, piso_medio_apoyo,
                        piso_alto_apoyo_atravesable, piso_alto, muro_alto_izquierdo, muro_alto_derecho]
        
        #Lista_plataformas movibles
        plataformas_movibles = [trampa_baja,plataforma_movimiento]

        flag_disparo = False
        tiempo_ultimo_disparo = 0 #Si pongo 0 es consecutivo

        duracion_maxima = 75000  # 1 minutos en milisegundos

        #Enemigos
        animaciones_enemigo_volador = {}
        animaciones_enemigo_volador["Derecha"] = enemigo_volador_derecha
        animaciones_enemigo_volador["Izquierda"] = enemigo_volado_izquierda
        animaciones_enemigo_volador["Muere"] = enemigo_volador_muerto

        inicializar_base_de_datos()
        super().__init__(fondo,pantalla, player,plataformas,plataformas_movibles, respawn, bala_manager, lista_monedas, fondo, diccionario_animaciones, tiempo_ultimo_disparo, flag_disparo, duracion_maxima, animaciones_enemigo_volador, False, None)
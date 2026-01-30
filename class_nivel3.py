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

class NivelTres(Nivel):
    def __init__ (self,pantalla:pygame.Surface):
        #Inicializa pygame
        pygame.init()
        pygame.mixer.init()
        #Config de pantalla
        W = 1024
        H = 720
        
        #FONDO
        fondo = pygame.image.load(r"texturas\Mapas\Pantalla\lvl_3.png").convert()
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
        player = Personaje(acciones, 5, (40, 40), (140, 480))

        # Crear ubicaciones aleatorias
        ubicaciones_aleatorias = [(167, 490), (390, 490), (780, 490), (935, 490)]
        ojo_aleatorio = [(167, 200), (600, 200)]

        #respawn
        respawn = Respawn(player,ubicaciones_aleatorias, ojo_aleatorio)

        #Enemigos
        diccionario_animaciones = {}
        diccionario_animaciones["Derecha"] = enemigo_camina_derecha
        diccionario_animaciones["Izquierda"] = enemigo_camina_izquierda
        diccionario_animaciones["Muere"] = enemigo_aplasta

        bala_manager = BalaManager(respawn, player)

        moneda1 = Moneda((27, 27), 50, (480, 230), coin)
        moneda2 = Moneda((27, 27), 50, (590, 330), coin)
        moneda3 = Moneda((27, 27), 50, (955, 405), coin)
        moneda4 = Moneda((27, 27), 50, (700, 335), coin)
        moneda5 = Moneda((27, 27), 50, (900, 335), coin)
        moneda6 = Moneda((27, 27), 50, (700, 430), coin)
        moneda7 = Moneda((27, 27), 50, (160, 150), coin)
        moneda8 = Moneda((27, 27), 50, (245, 150), coin)
        moneda9 = Moneda((27, 27), 50, (200, 480), coin)
        moneda10 = Moneda((27, 27), 50, (920, 325), coin)

        # Lista de monedas
        lista_monedas = [moneda1, moneda2,moneda3,moneda4,moneda5,moneda6,moneda7,moneda8,moneda9,moneda10]

        #Lista plataformas
        plataformas = [boss_pltaforma]
        
        plataformas_movibles = [piso_inmovil_boss_dos,piso_inmovil_boss]

        flag_disparo = False
        tiempo_ultimo_disparo = 0 #Si pongo 0 es consecutivo

        # Definición del cronómetro
        duracion_maxima = 75000 # 1 minutos en milisegundos

        #Enemigos
        nuevo_jefe_animaciones = {}
        nuevo_jefe_animaciones["Derecha"] = jefe_camina_derecha
        nuevo_jefe_animaciones["Izquierda"] = jefe_camina_izquierda
        nuevo_jefe_animaciones["Daño"] = jefe_daño
        nuevo_jefe_animaciones["Ataca"] = jefe_ataca
        nuevo_jefe_animaciones["Muriendo"] = jefe_mueriendo
        nuevo_jefe_animaciones["Muerto"] = jefe_muerto

        # Agrega las animaciones del nuevo jefe según sea necesario
        nuevo_jefe = Boss(nuevo_jefe_animaciones, 2, (100, 100), (890, 420), "horizontal")  # Ajusta la posición según sea necesario
        inicializar_base_de_datos()

        #Enemigos
        animaciones_enemigo_volador = {}
        animaciones_enemigo_volador["Derecha"] = enemigo_volador_derecha
        animaciones_enemigo_volador["Izquierda"] = enemigo_volado_izquierda
        animaciones_enemigo_volador["Muere"] = enemigo_volador_muerto
        lista_jefe = [nuevo_jefe]
        
        super().__init__(fondo,pantalla, player,plataformas,plataformas_movibles, respawn, bala_manager, lista_monedas, fondo, diccionario_animaciones, tiempo_ultimo_disparo, flag_disparo, duracion_maxima, animaciones_enemigo_volador, True, lista_jefe)
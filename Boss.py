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
class Boss(Enemigo):
    def __init__(self, animaciones, velocidad, tamaño, posicion=(0, 0), patron_movimiento="horizontal"):
        super().__init__(animaciones, velocidad, tamaño, posicion, patron_movimiento)
        self.vidas = 10
        self.tiempo_ataque = 0
        self.tiempo_entre_ataques = 1000
        self.lista_proyectiles = []  # Lista para almacenar los proyectiles

    def actualizar(self, pantalla, piso, jugador):
        super().actualizar(pantalla, piso, jugador)
        if self.tiempo_ataque == 0:
            #self.lanzar_proyectil()
            self.tiempo_ataque = self.tiempo_entre_ataques
        elif self.tiempo_ataque > 0:
            self.tiempo_ataque -= 1
        self.seguir_jugador(jugador)

        proyectiles_para_eliminar = []
        for proyectil in self.lista_proyectiles:
            proyectil.actualizar(pantalla)

            # ... (verificación de colisiones y otras lógicas)

        for proyectil in proyectiles_para_eliminar:
            self.lista_proyectiles.remove(proyectil)

    def lanzar_proyectil(self):
        direccion = "izquierda" if self.velocidad < 0 else "derecha"
        proyectil = Disparo(self.rectangulo_principal.x, self.rectangulo_principal.y, 10, direccion)
        self.lista_proyectiles.append(proyectil)


    def recibir_danio(self, cantidad_danio):
        # Método para reducir las vidas del jefe cuando recibe daño
        self.vidas -= cantidad_danio
        if self.vidas <= 0:
            self.esta_muerto = True
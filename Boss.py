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
        self.direccion_personaje = None
        self.tiempo_cambio_direccion = 15000

    def update(self, pantalla, piso, jugador):
        # if self.tiempo_ataque == 0:
        #     #self.lanzar_proyectil()
        #     self.tiempo_ataque = self.tiempo_entre_ataques
        # elif self.tiempo_ataque > 0:
        #     self.tiempo_ataque -= 1
        self.perseguir_jugador(jugador)
        self.animar(pantalla)
        self.avanzar(pantalla,piso)
        self.verificar_colision_personaje(jugador)
        self.detener_caida(piso)
        self.caer(self.velocidad)
        self.caminar_automaticamente(pantalla)
        self.update_hitbox()
        # proyectiles_para_eliminar = []
        # for proyectil in self.lista_proyectiles:
        #     proyectil.actualizar(pantalla)

        #     # ... (verificación de colisiones y otras lógicas)

        # for proyectil in proyectiles_para_eliminar:
        #     self.lista_proyectiles.remove(proyectil)
        

    def lanzar_proyectil(self):
        self.direccion = "Izquierda" if self.velocidad < 0 else "Derecha"
        proyectil = Disparo(self.rectangulo_principal.x, self.rectangulo_principal.y, 10, direccion)
        self.lista_proyectiles.append(proyectil)

    def animar(self, pantalla):
        if not self.esta_muerto:
            self.animacion_actual = self.animaciones[self.direccion]
            largo = len(self.animacion_actual)

            if self.contador_pasos >= largo:
                self.contador_pasos = 0

            pantalla.blit(self.animacion_actual[self.contador_pasos], self.rectangulo_principal)
            self.contador_pasos += 1
        else:
            if self.contador_animacion < len(self.animaciones["Muriendo"]):
                pantalla.blit(self.animaciones["Muriendo"][self.contador_animacion], self.rectangulo_principal)
                self.contador_animacion += 1
            else:
                # Cambia a la animación de muerto
                pantalla.blit(self.animaciones["Muerto"][0], self.rectangulo_principal)

    def recibir_danio(self, cantidad_danio):
        # Método para reducir las vidas del jefe cuando recibe daño
        self.vidas -= cantidad_danio
        if self.vidas <= 0:
            self.esta_muerto = True

    def perseguir_jugador(self, jugador):
        self.jugador = jugador
        jugador_x = self.jugador.rectangulo_principal.x
        jugador_y = self.jugador.rectangulo_principal.y

        # Verificar si el personaje está a la izquierda o a la derecha del enemigo
        if jugador_x < self.rectangulo_principal.x:
            self.direccion_personaje = "Izquierda"
        else:
            self.direccion_personaje = "Derecha"
        # Verificar si el personaje está en la misma altura que el enemigo
        if abs(jugador_y - self.rectangulo_principal.y) < 100:
            # Si el personaje está en la misma dirección en la que el enemigo se mueve, perseguirlo
            if self.direccion_personaje == self.direccion:
                if jugador_x < self.rectangulo_principal.x:
                    self.rectangulo_principal.x -= 7
                else:
                    self.rectangulo_principal.x += 7

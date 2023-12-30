import pygame
from loads import *
from premio import Premio
from proyectiles import Disparo
from loads import *


class BalaManager:
    def __init__(self, respawn, player):
        self.respawn = respawn
        self.personaje = player
        #self.proyectiles = proyectiles
        self.lista_proyectiles = []
    
    def agregar_proyectil(self, x, y, direccion, velocidad):
        proyectil = Disparo(x, y, direccion, velocidad)
        self.lista_proyectiles.append(proyectil)

    def verificar_colision_proyectil_plataforma(self,proyectil, plataformas):
        for plataforma in plataformas:
            if proyectil.rectangulo.colliderect(plataforma["rectangulo"]):
                return True
        return False

    def verificar_colision_proyectil_enemigo(self, proyectil, lista_enemigos):
        for enemigo in lista_enemigos:
            if proyectil.rectangulo.colliderect(enemigo.rectangulo_principal):
                # Colisión con enemigo
                #self.eliminar_proyectil(proyectil)
                # Realizar acciones adicionales, por ejemplo, eliminar al enemigo
                lista_enemigos.remove(enemigo)
                self.personaje.puntuacion += 100
                return True  # Indicar que hubo colisión con un enemigo
        return False

    def eliminar_proyectil(self, proyectil):
        # Eliminar el proyectil de la lista
        if proyectil in self.lista_proyectiles:
            self.lista_proyectiles.remove(proyectil)
            impacto.play()

    def eliminar_proyectil_y_enemigo(self, proyectil, enemigo_colisionado_respawn,pantalla):
        if proyectil.rectangulo.centerx < 0 or proyectil.rectangulo.centerx > pantalla.get_width():
            self.lista_proyectiles.remove(proyectil)
        elif enemigo_colisionado_respawn in self.respawn.lista_enemigos:
            # Aquí puedes realizar acciones adicionales antes de eliminar al enemigo
            self.respawn.lista_enemigos.remove(enemigo_colisionado_respawn)
            self.lista_proyectiles.remove(proyectil)

    def actualizar_proyectiles(self, pantalla, plataformas):
        proyectiles_a_eliminar = []

        for proyectil in self.lista_proyectiles:
            proyectil.actualizar(pantalla)

            # Lógica de colisión con plataformas
            if self.verificar_colision_proyectil_plataforma(proyectil, plataformas):
                proyectiles_a_eliminar.append(proyectil)
                continue

            # Lógica de colisión con enemigos generados en respawn
            enemigo_colisionado_respawn = self.verificar_colision_proyectil_enemigo(proyectil, self.respawn.lista_enemigos)
            if enemigo_colisionado_respawn:
                proyectiles_a_eliminar.append(proyectil)
                continue

            # ... (otras lógicas de colisión)

        # Lógica de eliminación de proyectiles
        for proyectil in proyectiles_a_eliminar:
            self.eliminar_proyectil(proyectil)

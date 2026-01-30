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
        proyectil = Disparo(x, y, direccion, velocidad, r"texturas\Aru\Mago\fire_ball.png")
        self.lista_proyectiles.append(proyectil)

    def verificar_colision_proyectil_plataforma_o_pantalla(self,proyectil, plataformas,pantalla):
        for plataforma in plataformas:
            if proyectil.rectangulo.colliderect(plataforma["rectangulo"]):
                return 

        if proyectil.rectangulo.right < 0 or proyectil.rectangulo.left > pantalla.get_width() or proyectil.rectangulo.bottom < 0 or proyectil.rectangulo.top > pantalla.get_height():
            return True  # El proyectil está fuera de la pantalla, eliminarlo
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
    
    def verificar_colision_proyectil_ojo(self, proyectil, lista_enemigos):
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
            efectos_sonido['impacto'].play()

    def actualizar_proyectiles(self, pantalla, plataformas):
        proyectiles_a_eliminar = []

        for proyectil in self.lista_proyectiles:
            proyectil.actualizar(pantalla)

            # Lógica de colisión con plataformas
            if self.verificar_colision_proyectil_plataforma_o_pantalla(proyectil, plataformas,pantalla):
                proyectiles_a_eliminar.append(proyectil)
                continue

            # Lógica de colisión con enemigos generados en respawn
            enemigo_colisionado_respawn = self.verificar_colision_proyectil_enemigo(proyectil, self.respawn.lista_enemigos)
            if enemigo_colisionado_respawn:
                proyectiles_a_eliminar.append(proyectil)
                continue

            ojo_colisionado_respawn = self.verificar_colision_proyectil_ojo(proyectil, self.respawn.lista_ojos)
            if ojo_colisionado_respawn:
                proyectiles_a_eliminar.append(proyectil)
                continue

        # Lógica de eliminación de proyectiles
        for proyectil in proyectiles_a_eliminar:
            self.eliminar_proyectil(proyectil)
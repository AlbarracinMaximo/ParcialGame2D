import pygame
from loads import *
from premio import Premio


class Disparo:
    def __init__(self, x, y, direccion,velocidad):
        self.superficie = pygame.image.load(r"texturas\fire_ball.png")
        self.superficie = pygame.transform.scale(self.superficie, (20,20))
        self.rectangulo = self.superficie.get_rect()
        self.rectangulo.x = x
        self.rectangulo.centery = y
        self.direccion = direccion
        self.velocidad = velocidad

    def actualizar(self,pantalla):
        if self.direccion == "Derecha":
            self.rectangulo.x += self.velocidad
        elif self.direccion == "Izquierda":
            self.rectangulo.x -= self.velocidad
        pantalla.blit(self.superficie, self.rectangulo)

    def verificar_colision_plataforma_disparo(self, plataformas):
        for plataforma in plataformas:
            if self.rectangulo.colliderect(plataforma["rectangulo"]):
                return True
        return False
    
    def verificar_colision_enemigo(self, lista_enemigos):
        for enemigo in lista_enemigos:
            if self.rectangulo.colliderect(enemigo.rectangulo_principal):
                return enemigo
        return None
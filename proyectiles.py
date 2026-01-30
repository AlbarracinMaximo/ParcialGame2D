import pygame
from loads import *
from premio import Premio


class Disparo:
    def __init__(self, x, y, direccion,velocidad, path_image):
        self.superficie = pygame.image.load(path_image)
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
        elif self.direccion == "Abajo":
            self.rectangulo.y += self.velocidad
        pantalla.blit(self.superficie, self.rectangulo)
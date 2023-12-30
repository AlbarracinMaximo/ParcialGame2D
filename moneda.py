import pygame
from loads import *
# Definir la clase de la moneda
class Moneda:
    def __init__(self, tamaño, puntos, ubicacion = (0,0), imagen = ""):
        self.image = pygame.image.load(imagen)
        self.image = pygame.transform.scale(self.image, tamaño)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = ubicacion
        self.puntos = puntos
        self.lista_monedas = []

    def actualizar(self,pantalla):
        pantalla.blit(self.image, self.rect)
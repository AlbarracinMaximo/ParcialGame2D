import pygame
from loads import *
# Definir la clase de la moneda
class Vida:
    def __init__(self, tamaño, posicion, vidas,imagen = ""):
        self.image = pygame.image.load(imagen)
        self.image = pygame.transform.scale(self.image, tamaño)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = posicion
        self.vidas = vidas
        self.lista_vidas = []

    def actualizar(self,velocidad,plataformas,pantalla):
        self.detener_caida(plataformas)
        self.caer(velocidad)
        pantalla.blit(self.image, self.rect)

    def caer(self, velocidad):
        self.rect.y += velocidad

    def detener_caida(self,plataformas):
        for piso in plataformas:
            if self.rect.colliderect(piso["rectangulo"]) and piso["esSuelo"]:
                self.rect.y = piso["rectangulo"].top - self.rect.height

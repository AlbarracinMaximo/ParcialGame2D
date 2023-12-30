import pygame
import random
from loads import *

class Premio():
    def __init__(self, tamaño, posicion = (0,0),imagen = ""):
        self.image = pygame.image.load(imagen)
        self.image = pygame.transform.scale(self.image, tamaño)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = posicion
        self.descubierta = False
        self.tocada = False
        self.disponible = False
        self.tiempo_aparicion = pygame.time.get_ticks()

    def actualizar(self,velocidad,plataformas,pantalla):
        self.detener_caida(plataformas)
        self.caer(velocidad)
        self.activar_premio(plataformas)
        pantalla.blit(self.image, self.rect)

    def caer(self, velocidad):
        self.rect.y += velocidad

    def revelar(self):
        self.descubierta = True
    
    def detener_caida(self,plataformas):
        for piso in plataformas:
            if self.rect.colliderect(piso["rectangulo"]) and piso["esSuelo"]:
                self.rect.y = piso["rectangulo"].top - self.rect.height
    
    def activar_premio(self,plataformas):
        for piso in plataformas:
            if self.rect.colliderect(piso["rectangulo"]) and piso["esSuelo"]:
                self.disponible = True
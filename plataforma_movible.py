import pygame
from loads import *

class plataformas_movible:
    def __init__(self, tamaño, x, y, velocidad_vertical, velocidad_horizontal, rango, tiempo_espera, path=""):
        self.superficie = pygame.image.load(path)
        self.superficie = pygame.transform.scale(self.superficie, tamaño)
        self.rectangulo = self.superficie.get_rect(topleft=(x, y))
        self.velocidad_vertical = velocidad_vertical
        self.velocidad_horizontal = velocidad_horizontal
        self.rango = rango
        self.direccion_vertical = 1
        self.direccion_horizontal = 1
        self.tiempo_inicial = pygame.time.get_ticks()
        self.tiempo_espera = tiempo_espera  # Intervalo en milisegundos para el movimiento

    def actualizar(self,pantalla):
        self.mover()
        pantalla.blit(self.superficie, self.rectangulo)

    
    def mover(self):
        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = tiempo_actual - self.tiempo_inicial

        if tiempo_transcurrido >= self.tiempo_espera:
            self.rectangulo.y += self.velocidad_vertical * self.direccion_vertical

            # Verifica si la plataforma ha alcanzado los límites
            if self.rectangulo.y <= self.rango[0] or self.rectangulo.y >= self.rango[1]:
                self.direccion_vertical *= -1  # Cambia la dirección al llegar a los límites
                self.tiempo_inicial = tiempo_actual
            self.mover_horizontal()

    def mover_horizontal(self):
        # Movimiento horizontal
        self.rectangulo.x += self.velocidad_horizontal * self.direccion_horizontal

        # Verifica si la plataforma ha alcanzado los límites horizontales
        if self.rectangulo.x <= self.rango[2] or self.rectangulo.x >= self.rango[3]:
            self.direccion_horizontal *= -1  # Cambia la dirección al llegar a los límites
            self.tiempo_inicial = pygame.time.get_ticks()


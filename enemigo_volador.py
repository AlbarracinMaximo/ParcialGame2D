from loads import *
from enemigo import Enemigo
from balaenemigo import BalaEnemigo
import math

class EnemigoVolador(Enemigo):
    def __init__(self, animaciones, velocidad, tamaño, posicion,  altura_vuelo, rango_horizontal,jugador, patron_movimiento="horizontal"):
        super().__init__(animaciones, velocidad, tamaño, posicion, patron_movimiento)
        self.altura_vuelo = altura_vuelo
        self.direccion_vuelo = 1  # 1 para volar hacia arriba, -1 para volar hacia abajo
        self.rango_horizontal = rango_horizontal  # Límites del rango horizontal
        self.contador = 0
        # Tiempo entre disparos en milisegundos (por ejemplo, 2000ms = 2 segundos)
        self.tiempo_entre_disparos = 2000
        self.tiempo_ultimo_disparo = pygame.time.get_ticks()
        self.bala_manager_enemigo = BalaEnemigo(self.rectangulo_principal.x, self.rectangulo_principal.y, "Abajo", 10, r"texturas\Enemigo\Aereos\proyectil.png")
        self.jugador = jugador

    def mover(self,pantalla,plataformas):
        # Movimiento horizontal
        if self.direccion == "Izquierda":
            self.rectangulo_principal.x -= self.velocidad
            if self.rectangulo_principal.x < self.rango_horizontal[0]:
                self.direccion = "Derecha"
        elif self.direccion == "Derecha":
            self.rectangulo_principal.x += self.velocidad
            if self.rectangulo_principal.x > self.rango_horizontal[1]:
                self.direccion = "Izquierda"

        # Movimiento vertical (fluctuación)
        fluctuacion = math.sin(self.contador) * self.altura_vuelo
        self.rectangulo_principal.y += fluctuacion

        self.contador += 0.1  # Ajusta la velocidad de la fluctuación según sea necesario
        
        self.animar(pantalla)

         # Lanzar un proyectil automáticamente cada cierto tiempo
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_ultimo_disparo >= self.tiempo_entre_disparos:
            self.tiempo_ultimo_disparo = tiempo_actual
            self.lanzar_proyectil_automaticamente()
        self.bala_manager_enemigo.actualizar_proyectiles_enemigos(pantalla,plataformas,self.jugador)
    
    def lanzar_proyectil_automaticamente(self):
        x = self.rectangulo_principal.centerx
        y = self.rectangulo_principal.centery

        if x is not None:
            self.bala_manager_enemigo.agregar_proyectil_enemigo(x, y, "Abajo", 10)
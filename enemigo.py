from loads import *
from personaje_principal_copy import *
from loads import *
class Enemigo:
    def __init__(self, animaciones, velocidad, tamaño, posicion=(0,0), patron_movimiento="horizontal"):
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, * tamaño)
        self.rectangulo_principal = self.animaciones['derecha'][0].get_rect()
        self.rectangulo_principal.x, self.rectangulo_principal.y = posicion
        self.patrón_movimiento = patron_movimiento
        self.esta_muerto = False
        self.contador_pasos = 0
        self.animacion_actual = self.animaciones['izquierda']
        self.animacion_actual = self.animaciones['derecha']
        self.muriendo = False
        self.esta_derrotado = False
        #self.lista_enemigos = []
        self.desplazamiento_x = 0
        self.velocidad = velocidad  # Puedes ajustar la velocidad a tu preferencia
        self.direccion = "derecha"  # Inicialmente, el enemigo se mueve hacia la izquierda
        self.tiempo_cambio_direccion = 3000  # Tiempo en milisegundos para cambiar de dirección (ejemplo: 3000ms = 3 segundos)
        self.tiempo_ultimo_cambio = pygame.time.get_ticks()
        self.distancia_recorrida = 0

    def actualizar(self, pantalla,piso,jugador):
        if not self.esta_muerto:
            self.animar(pantalla)
            self.avanzar(pantalla,piso)
            self.verificar_colision_personaje(jugador)
            self.detener_caida(piso)
            self.caer(self.velocidad)
            #pantalla.blit(self.animaciones[self.direccion], self.rectangulo_principal)

    def animar(self, pantalla):
        largo = len(self.animaciones[self.direccion])

        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        imagen_actual = self.animaciones[self.direccion][self.contador_pasos]

        pantalla.blit(imagen_actual, self.rectangulo_principal)
        self.contador_pasos += 1

        if self.muriendo and self.contador_pasos >= largo:
            self.esta_muerto = True

    def avanzar(self,pantalla,plataformas):
        for piso in plataformas:
            if self.rectangulo_principal.colliderect(piso["rectangulo"]):
                if piso["esSuelo"]:
                    self.caminar_automaticamente()
                    self.desplazamiento_x = self.velocidad

                    if self.direccion == "izquierda":
                        self.desplazamiento_x *= -1

                    nueva_x = self.rectangulo_principal.x + self.desplazamiento_x

                    if piso["rectangulo"].left <= nueva_x <= piso["rectangulo"].right - self.rectangulo_principal.width:
                        self.rectangulo_principal.x += self.desplazamiento_x

    def caer(self, velocidad):    
        self.rectangulo_principal.y += velocidad

    def detener_caida(self,plataformas):
        for piso in plataformas:
            if self.rectangulo_principal.colliderect(piso["rectangulo"]) and piso["esSuelo"]:
                self.rectangulo_principal.y = piso["rectangulo"].top - self.rectangulo_principal.height

    def seguir_jugador(self, jugador):
        velocidad = 1  # Ajusta según sea necesario

        if self.rectangulo_principal.x < jugador.rectangulo_principal.x and abs(self.rectangulo_principal.y - jugador.rectangulo_principal.y) < 2:
            self.rectangulo_principal.x += velocidad
        elif self.rectangulo_principal.x > jugador.rectangulo_principal.x and abs(self.rectangulo_principal.y - jugador.rectangulo_principal.y) < 2:
            self.rectangulo_principal.x -= velocidad

    def verificar_colision_personaje(self, player):
        if not self.esta_derrotado and self.rectangulo_principal.colliderect(player.rectangulo_principal):
            if player.tiempo_invulnerable == 0 and self.rectangulo_principal.right > player.rectangulo_principal.left:
                player.simular_salto_lateral("Izquierda")
                player.perder_vida()
                golpe_enemigo.play()
                if player.vidas == 0:
                    player.esta_muerto = True
                    # Colisión desde la derecha
                    # Manejar según tus necesidades (puedes detener al enemigo, reducir la vida, etc.)
            elif player.tiempo_invulnerable == 0 and self.rectangulo_principal.left < player.rectangulo_principal.right:
                player.simular_salto_lateral("Derecha")
                player.perder_vida()
                golpe_enemigo.play()
                if player.vidas == 0:
                    player.esta_muerto = True
                    # Colisión desde la izquierda
                    # Manejar según tus necesidades
                # Colisión desde los lados
                # Resta una vida al jugador (ajusta según tus necesidades)
                # Puedes agregar lógica adicional aquí, como detener al jugador o reiniciar su posición
    

    def caminar_automaticamente(self):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_ultimo_cambio >= self.tiempo_cambio_direccion:
            self.tiempo_ultimo_cambio = tiempo_actual
            # Cambiar la dirección del enemigo cada cierto tiempo
            if self.direccion == "izquierda":
                self.direccion = "derecha"
            else:
                self.direccion = "izquierda"
    
    def caminar(self, pantalla):
        self.desplazamiento_x = self.velocidad

        if self.direccion == "izquierda":
            self.desplazamiento_x *= -1

        nueva_x = self.rectangulo_principal.x + self.desplazamiento_x

        if nueva_x >= 0 and nueva_x <= pantalla.get_width() - self.rectangulo_principal.width:
            self.rectangulo_principal.x += self.desplazamiento_x
        

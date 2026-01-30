from loads import *
from personaje_principal_copy import *
class Enemigo:
    def __init__(self, animaciones, velocidad, tamaño, posicion=(0,0), patron_movimiento="horizontal"):
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, * tamaño)
        self.rectangulo_principal = self.animaciones["Derecha"][0].get_rect()
        self.rectangulo_principal.x, self.rectangulo_principal.y = posicion
        # Definir la hitbox del enemigo
        self.hitbox = pygame.Rect(self.rectangulo_principal.x, self.rectangulo_principal.y, tamaño[0], tamaño[1])
        self.patron_movimiento = patron_movimiento
        self.esta_muerto = False
        self.direccion = "Izquierda"  # Inicialmente, el enemigo se mueve hacia la Izquierda
        self.contador_pasos = 0
        #self.animacion_actual = self.animaciones["Izquierda"]
        self.muriendo = False
        self.esta_derrotado = False
        #self.lista_enemigos = []
        self.desplazamiento_x = 0
        self.velocidad = velocidad  # Puedes ajustar la velocidad a tu preferencia
        self.tiempo_cambio_direccion = 3000  # Tiempo en milisegundos para cambiar de dirección (ejemplo: 3000ms = 3 segundos)
        self.tiempo_ultimo_cambio = pygame.time.get_ticks()
        self.distancia_recorrida = 0
        self.contador_animacion = 0

    def actualizar(self, pantalla,piso,jugador):
            self.animar(pantalla)
            self.avanzar(pantalla,piso)
            self.verificar_colision_personaje(jugador)
            self.detener_caida(piso)
            self.caer(self.velocidad)
            #pantalla.blit(self.animaciones[self.direccion], self.rectangulo_principal)
            self.update_hitbox()
            self.caminar_automaticamente(pantalla)

    def animar(self, pantalla):
        if not self.esta_muerto:
            self.animacion_actual = self.animaciones[self.direccion]
            largo = len(self.animacion_actual)

            if self.contador_pasos >= largo:
                self.contador_pasos = 0

            pantalla.blit(self.animacion_actual[self.contador_pasos], self.rectangulo_principal)
            self.contador_pasos += 1
        #  else:
        #         if self.contador_animacion < len(self.animaciones["Muriendo"]):
        #             pantalla.blit(self.animaciones["muriendo"][self.contador_animacion], self.rectangulo_principal)
        #             self.contador_animacion += 1
        #         else:
        #         # Cambia a la animación de muerto
        #         pantalla.blit(self.animaciones["muerto"][0], self.rectangulo_principal)

    def avanzar(self,pantalla,plataformas):
        for piso in plataformas:
            if self.rectangulo_principal.colliderect(piso["rectangulo"]):
                if piso["esSuelo"]:
                    #self.caminar_automaticamente(pantalla)
                    self.desplazamiento_x = self.velocidad

                    if self.direccion == "Izquierda":
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

    def verificar_colision_personaje(self, jugador):
        if not self.esta_derrotado and self.hitbox.colliderect(jugador.hitbox):
            if jugador.tiempo_invulnerable == 0:
                if self.hitbox.midright[0] + 40 > jugador.hitbox.midleft[0]:
                    jugador.simular_salto_lateral("Izquierda")
                    jugador.perder_vida()
                    efectos_sonido['golpe_enemigo'].play()
                    if jugador.vidas == 0:
                        jugador.esta_muerto = True
                        # Colisión desde la derecha
                        # Manejar según tus necesidades (puedes detener al jugador, reducir la vida, etc.)
                elif self.hitbox.midleft[0] - 40 < jugador.hitbox.midright[0]:
                    jugador.simular_salto_lateral("Derecha")
                    jugador.perder_vida()
                    efectos_sonido['golpe_enemigo'].play()
                    if jugador.vidas == 0:
                        jugador.esta_muerto = True


    def caminar_automaticamente(self,pantalla):
        # tiempo_actual = pygame.time.get_ticks()
        # #self.animacion_actual = self.animaciones[self.direccion]
        # if tiempo_actual - self.tiempo_ultimo_cambio >= self.tiempo_cambio_direccion:
        #     self.tiempo_ultimo_cambio = tiempo_actual
        #     # Cambiar la dirección del enemigo cada cierto tiempo
        #     if self.direccion == "Izquierda":
        #         self.direccion = "Derecha"
        #     else:
        #         self.direccion = "Izquierda"
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_ultimo_cambio >= self.tiempo_cambio_direccion:
            self.tiempo_ultimo_cambio = tiempo_actual
            # Obtener el ancho de la pantalla
            
            self.cambiar_direccion()
        ancho_pantalla = pantalla.get_width()
        # Cambiar la dirección del enemigo si colisiona con el borde de la pantalla
        if (self.direccion == "Izquierda" and self.rectangulo_principal.left - 14 <= 0) or (self.direccion == "Derecha" and self.rectangulo_principal.right + 14 >= ancho_pantalla):
            self.cambiar_direccion()
    
    def cambiar_direccion(self):
        if self.direccion == "Izquierda":
            self.direccion = "Derecha"
        else:
            self.direccion = "Izquierda"
        
    def update_hitbox(self):
        # Actualizar la posición de la hitbox para que coincida con la posición del enemigo
        self.hitbox.x = self.rectangulo_principal.x
        self.hitbox.y = self.rectangulo_principal.y
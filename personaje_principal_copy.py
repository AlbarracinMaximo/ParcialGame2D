from loads import *
import pygame
from premio import Premio
from proyectiles import Disparo
from loads import *

class Personaje:
    def __init__(self, animaciones, velocidad, tamaño, posicion =(0,0)):
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, *tamaño)
        #Movimientos de mario
        self.rectangulo_principal = self.animaciones["Quieto"][0].get_rect()
        self.rectangulo_principal.x, self.rectangulo_principal.y = posicion
        self.velocidad = velocidad
        self.que_hace = "Quieto"
        self.contador_pasos = 0
        self.animacion_actual = self.animaciones["Quieto"]
        #Desplazamiento de personaje
        self.desplazamiento_y = 0
        self.desplazamiento_x = 0
        self.potencia_salto = -18
        self.limite_velocidad_salto = 18
        self.gravedad = 1
        #Boleanos de estado de _personaje
        self.esta_saltando = False
        self.esta_cayendo = False
        self.esta_muerto = False
        #esto pa ponerle tiempo a cuanto dura la habilidad de super_personaje
        self.habilidad_especial = False
        self.tiempo_habilidad_especial = 6000 #10 segundo en milisegundos
        self.tiempo_anterior = 0
        self.lista_proyectiles = []
        self.vidas = 5
        self.tiempo_invulnerable = 0  # Inicialmente no invulnerable
        self.contador_animacion = 0
        self.ultima_tecla = ""
        self.puntuacion = 0

    def actualizar(self, pantalla, piso):
        tiempo_actual = pygame.time.get_ticks()

        if tiempo_actual > self.tiempo_anterior + self.tiempo_habilidad_especial:
            self.habilidad_especial = False

        accion = ""

        if self.habilidad_especial:
            match self.que_hace:
                case "Derecha":
                    self.animacion_actual = self.animaciones["Super_Derecha"]
                case "Izquierda":
                    #accion = "Super_Izquierda"
                    self.animacion_actual = self.animaciones["Super_Izquierda"]
                case "Salta":
                    self.animacion_actual = self.animaciones["Super_Salta"]
                    #accion = "Super_Salta"
                case "Quieto":
                    self.animacion_actual = self.animaciones["Super_Quieto"]
                    #accion = "Super_Quieto"
        else:
            self.animacion_actual = self.animaciones[self.que_hace]

        match self.que_hace:
            case "Derecha":
                if not self.esta_saltando:
                    self.animar(pantalla)
                if not self.esta_muerto:
                    self.utima_tecla = self.que_hace
                    self.caminar(pantalla)
            case "Izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla)
                if not self.esta_muerto:
                    self.utima_tecla = self.que_hace
                    self.caminar(pantalla)
            case "Salta":
                if not self.esta_saltando and not self.esta_muerto:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
                    salto.play()
            case "Quieto":
                if not self.esta_saltando:
                    self.animar(pantalla)

        self.aplicar_gravedad(pantalla, piso)
        self.actualizar_invulnerabilidad()
        self.verificar_muerte(pantalla)

    def animar(self, pantalla):
        if not self.esta_muerto:
            largo = len(self.animacion_actual)

            if self.contador_pasos >= largo:
                self.contador_pasos = 0

            pantalla.blit(self.animacion_actual[self.contador_pasos], self.rectangulo_principal)
            self.contador_pasos += 1
        else:
            if self.contador_animacion < len(self.animaciones["Muriendo"]):
                pantalla.blit(self.animaciones["Muriendo"][self.contador_animacion], self.rectangulo_principal)
                self.contador_animacion += 1
            else:
                # Cambia a la animación de muerto
                pantalla.blit(self.animaciones["Muerto"][0], self.rectangulo_principal)

    def caminar(self, pantalla):
        self.desplazamiento_x = self.velocidad

        if self.que_hace == "Izquierda":
            self.desplazamiento_x *= -1

        nueva_x = self.rectangulo_principal.x + self.desplazamiento_x

        if nueva_x >= 0 and nueva_x <= pantalla.get_width() - self.rectangulo_principal.width:
            self.rectangulo_principal.x += self.desplazamiento_x

    def aplicar_gravedad(self, pantalla, plataformas):
        if self.esta_saltando:
            self.animar(pantalla)
            self.rectangulo_principal.y += self.desplazamiento_y

            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_salto:
                self.desplazamiento_y += self.gravedad

            if self.desplazamiento_y > 1:
                self.esta_cayendo = True
        else:
            # Si no está saltando, está cayendo
            if self.esta_cayendo:
                self.cayendo()
                
        self.colisionar_plataformas(plataformas)

    def colisionar_plataformas(self, plataformas):
        for piso in plataformas:
            if self.rectangulo_principal.colliderect(piso["rectangulo"]):
                if piso["esMuro"]:
                    # Colisión con un muro
                    if self.desplazamiento_x > 0:  # Movimiento a la derecha
                        self.rectangulo_principal.right = piso["rectangulo"].left
                        self.rectangulo_principal.x += 0
                    elif self.desplazamiento_x < 0:  # Movimiento a la izquierda
                        self.rectangulo_principal.left = piso["rectangulo"].right
                        self.rectangulo_principal.x += 0
                if piso["esSuelo"]:
                    # Colisión con una plataforma normal (piso)
                    if self.desplazamiento_y > 0:
                        self.esta_cayendo = False
                        self.desplazamiento_y = 0
                        self.esta_saltando = False
                        self.rectangulo_principal.bottom = piso["rectangulo"].top
                        break
                    elif self.desplazamiento_y < 0:
                        self.desplazamiento_y = 0
                        self.rectangulo_principal.top = piso["rectangulo"].bottom
                if piso["esAtravesable"] and self.esta_cayendo:
                    self.esta_cayendo = False
                    self.desplazamiento_y = 0
                    self.esta_saltando = False
                    self.rectangulo_principal.bottom = piso["rectangulo"].top
                    break
                if piso["esPremio"]:
                    return piso["rectangulo"].topleft
            else:
                self.esta_saltando = True
        return None

    def verificar_colision_premio(self, premio):
        if premio.disponible and self.rectangulo_principal.colliderect(premio.rect):
            premio.descubierta = False
            premio.tocada = True
            premio.disponible = False
            self.tiempo_anterior = pygame.time.get_ticks()
            self.habilidad_especial = True

    def romper_bloque(self,lista_plataformas,premio):
        for plataforma in lista_plataformas:
            if plataforma["esPremio"]:
                if self.rectangulo_principal.colliderect(plataforma["rectangulo"]):
                    premio.descubierta = True
                    premio.tocada = False

    def lanzar_proyectiles(self,bala_manager):
        x = None
        #margen = 47
        y = self.rectangulo_principal.centery
        if self.utima_tecla == "Derecha":
            x = self.rectangulo_principal.right 
        
        elif self.utima_tecla == "Izquierda":
            x = self.rectangulo_principal.left 

        if x is not None:
            bala_manager.agregar_proyectil(x, y, self.utima_tecla, 10)
            proyectil.play()
    
    def perder_vida(self):
        if self.tiempo_invulnerable <= 0:
            self.vidas -= 1
            self.tiempo_invulnerable = 150  # Puedes ajustar el tiempo según tus necesidades

    def actualizar_invulnerabilidad(self):
        if self.tiempo_invulnerable > 0:
            self.tiempo_invulnerable -= 1
    
    def simular_salto_lateral(self, direccion):
        if direccion == "Derecha":
            self.rectangulo_principal.x += 30
        elif direccion == "Izquierda":
            self.rectangulo_principal.x -= 30
        elif direccion == "Arriba":
            self.rectangulo_principal.y -= 20
        elif direccion == "Abajo":
            self.rectangulo_principal.y += 20

    def cayendo(self):
        # Lógica específica para cuando el personaje está cayendo
        # Puedes ajustar la velocidad de caída según tus necesidades
        # Por ejemplo, puedes usar una gravedad más fuerte al caer
        self.rectangulo_principal.y += self.gravedad
        # Agrega cualquier otra lógica específica que necesites
    
    def obtener_moneda(self, monedas):
        monedas_a_eliminar = []

        for moneda in monedas:
            if self.rectangulo_principal.colliderect(moneda.rect):
                # Sumar puntos al jugador al colisionar con una moneda
                self.puntuacion += moneda.puntos
                print(f"Puntuación actual: {self.puntuacion}")
                monedas_a_eliminar.append(moneda)
                coin.play()

        # Eliminar las monedas recogidas de la lista
        for moneda in monedas_a_eliminar:
            monedas.remove(moneda)

    def manejar_colision_trampa(self, trampa):
        if self.rectangulo_principal.colliderect(trampa.rectangulo):
            if self.desplazamiento_y > 0:
                # Colisión desde arriba, el personaje salta sobre la trampa
                self.esta_cayendo = False
                self.desplazamiento_y = 0
                self.rectangulo_principal.bottom = trampa.rectangulo.top
                self.esta_saltando = False
            elif self.desplazamiento_y < 0:
                # Colisión desde abajo, detener el salto y hacer otras acciones si es necesario
                self.esta_cayendo = False
                self.desplazamiento_y = 0
                self.rectangulo_principal.top = trampa.rectangulo.bottom
                self.simular_salto_lateral("Abajo")
                self.vidas -= 1
                # Agregar otras acciones si es necesario, por ejemplo, quitar vidas
                # o reiniciar el nivel. 

    def verificar_muerte(self,pantalla):
        if self.vidas == 0:
            self.esta_muerto = True
            muerte_personaje.play()
        
        if self.rectangulo_principal.y > pantalla.get_height():
            self.vidas = 0
            self.esta_muerto = True
            muerte_personaje.play()
        
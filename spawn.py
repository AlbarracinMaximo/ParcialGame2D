import pygame
import random
import sys
from enemigo_volador import EnemigoVolador
from premio import Premio
from enemigo import Enemigo
from vida import *
from loads import *

# Define tus clases de Premio y Enemigo aquí (asumo que ya las tienes)

class Respawn:
    def __init__(self, personaje,ubicacion_aleatoria, ojo_aleatorio):
        self.personaje = personaje
        self.tiempo_anterior_premio = pygame.time.get_ticks()
        self.tiempo_anterior_enemigo = pygame.time.get_ticks()
        self.tiempo_anterior_vida = pygame.time.get_ticks()
        self.ubicaciones_posibles_premios = ubicacion_aleatoria
        self.ubicaciones_posibles_enemigos = ubicacion_aleatoria
        self.ubicaciones_posibles_vidas = ubicacion_aleatoria
        self.ubicaciones_posibles_enemigos_ojo = ojo_aleatorio
        self.tiempo_anterior_respawn = pygame.time.get_ticks()
        self.intervalo_respawn = 20000
        self.primer_round = True
        self.segundo_round = False
        self.max_rounds = 2
        self.round_actual = 0
        self.lista_premios = []
        self.lista_enemigos = []
        self.lista_ojos = []
        self.lista_vidas = []

    def generar_premio(self):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_anterior_premio > 20000:  # Generar cada 10 segundos
            nuevo_premio = Premio((30, 30), random.choice(self.ubicaciones_posibles_premios), manzana)
            self.lista_premios.append(nuevo_premio)
            self.tiempo_anterior_premio = tiempo_actual

    def generar_vida(self):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_anterior_vida > 10000:  # Generar cada 10 segundos
            nueva_vida = Vida((30, 30), random.choice(self.ubicaciones_posibles_vidas),1,r"texturas\Mapas\Articulos\vida.png")
            self.lista_vidas.append(nueva_vida)
            self.tiempo_anterior_vida = tiempo_actual

    def actualizar_premios(self):
        tiempo_actual = pygame.time.get_ticks()
        for premio in self.lista_premios:
            if tiempo_actual - premio.tiempo_aparicion > 7000:  # Desaparecer después de 5 segundos
                self.lista_premios.remove(premio)

    def generar_enemigo(self,diccionario_animaciones):
        nuevo_ubicacion = random.choice(self.ubicaciones_posibles_enemigos)  # Posición X aleatoria
        nuevo_ubicacion_2 = random.choice(self.ubicaciones_posibles_enemigos)  # Posición X aleatoria
        nuevo_ubicacion_3 = random.choice(self.ubicaciones_posibles_enemigos)  # Posición X aleatoria
        nuevo_ubicacion_4 = random.choice(self.ubicaciones_posibles_enemigos)  
        nuevo_enemigo = Enemigo(diccionario_animaciones, 1, (30,30),nuevo_ubicacion,"horizontal")
        nuevo_enemigo_2 = Enemigo(diccionario_animaciones, 1, (30,30),nuevo_ubicacion_2,"horizontal")
        nuevo_enemigo_3 = Enemigo(diccionario_animaciones, 1, (30,30),nuevo_ubicacion_3,"horizontal")
        nuevo_enemigo_4 = Enemigo(diccionario_animaciones, 1, (30,30),nuevo_ubicacion_4,"horizontal")
        self.lista_enemigos.extend([nuevo_enemigo,nuevo_enemigo_2,nuevo_enemigo_3,nuevo_enemigo_4])

        # Limpiar enemigos muertos después de generar uno nuevo
        enemigos_vivos = []
        for enemigo in self.lista_enemigos:
            if not enemigo.esta_muerto:
                enemigos_vivos.append(enemigo)
    
        self.list_enemigos = enemigos_vivos

    def generar_enemigo_volador(self,diccionario_animaciones):
        nuevo_ubicacion = random.choice(self.ubicaciones_posibles_enemigos_ojo)
        nuevo_ubicacion_2 = random.choice(self.ubicaciones_posibles_enemigos_ojo) 
        nuevo_enemigo = EnemigoVolador(diccionario_animaciones, 1, (30,30),nuevo_ubicacion,1,(50,100),self.personaje,"horizontal")
        nuevo_enemigo_2 = EnemigoVolador(diccionario_animaciones, 1, (30,30),nuevo_ubicacion_2,1,(500,700),self.personaje,"horizontal")
        self.lista_ojos.extend([nuevo_enemigo,nuevo_enemigo_2])

        # Limpiar enemigos muertos después de generar uno nuevo
        enemigos_vivos = []
        for enemigo in self.lista_ojos:
            if not enemigo.esta_muerto:
                enemigos_vivos.append(enemigo)

    def crear_enemigos(self,diccionario_animaciones,diccionario_ojo_volador):
        tiempo_actual = pygame.time.get_ticks()
        if self.primer_round and tiempo_actual - self.tiempo_anterior_enemigo > 10000:
            self.generar_enemigo(diccionario_animaciones)
            self.generar_enemigo_volador(diccionario_ojo_volador)
            self.primer_round = False
            self.round_actual += 1
            self.tiempo_anterior_enemigo = tiempo_actual
        elif not self.primer_round  and self.round_actual == 1 and tiempo_actual - self.tiempo_anterior_enemigo > 10000:
            self.generar_enemigo(diccionario_animaciones)
            self.generar_enemigo_volador(diccionario_ojo_volador)
            self.tiempo_anterior_enemigo = tiempo_actual
            self.round_actual += 1
            self.segundo_round = True
            print("Segundo round:", self.segundo_round)

        if self.round_actual >= self.max_rounds:
            self.round_actual = 0  # Reiniciar el contador de rounds

    def generar_todo(self,diccionario_animaciones,diccionario_ojo_volador):
        self.generar_premio()
        self.crear_enemigos(diccionario_animaciones, diccionario_ojo_volador)
        self.actualizar_premios()
        self.generar_vida()

    def verificar_colision_enemigo_respawn(self, pantalla):
        enemigos_para_remover = []

        for enemigo in self.lista_enemigos:
            if self.personaje.hitbox.colliderect(enemigo.hitbox):
                if self.personaje.esta_cayendo and self.personaje.hitbox.bottom > enemigo.hitbox.top :
                    # Colisión desde arriba, el personaje salta sobre el enemigo
                    enemigo.esta_muerto = True
                    enemigo.esta_derrotado = True
                    enemigo.animacion_actual = enemigo.animaciones['Muere']
                    enemigo.animar(pantalla)
                    enemigos_para_remover.append(enemigo)
                    self.personaje.puntuacion += 20
                    
        # Remover los enemigos marcados para eliminación
        for enemigo in enemigos_para_remover:
            self.lista_enemigos.remove(enemigo)

    def verificar_colision_ojo_respawn(self, pantalla):
        enemigos_para_remover = []

        for enemigo in self.lista_ojos:
            if self.personaje.hitbox.colliderect(enemigo.hitbox):
                if self.personaje.esta_cayendo and self.personaje.hitbox.bottom > enemigo.hitbox.top :
                    # Colisión desde arriba, el personaje salta sobre el enemigo
                    enemigo.esta_muerto = True
                    enemigo.esta_derrotado = True
                    enemigo.animacion_actual = enemigo.animaciones['Muere']
                    enemigo.animar(pantalla)
                    enemigos_para_remover.append(enemigo)
                    self.personaje.puntuacion += 20
                    
        # Remover los enemigos marcados para eliminación
        for enemigo in enemigos_para_remover:
            self.lista_ojos.remove(enemigo)

    def sumar_vida(self):
        vidas_a_eliminar = []
        for vida in self.lista_vidas:
            if self.personaje.rectangulo_principal.colliderect(vida.rect):
                if self.personaje.vidas > 4:
                    vidas_a_eliminar.append(vida)
                else:
                    self.personaje.vidas += vida.vidas
                    vidas_a_eliminar.append(vida)
                    efectos_sonido['vida'].play()

        # Eliminar las vidas recogidas de la lista
        for vida in vidas_a_eliminar:
            self.lista_vidas.remove(vida)
import pygame
from Modo import cambiar_modo, obtener_modo
from blit_vidas import Vidas_personaje
pygame.font.init() 
from pygame.locals import *
from loads import *
from SQLite import *
from cargar_partida import *

class Nivel:
    def __init__(self,fondo,pantalla, personaje_principal,lista_plataformas,plataformas_movibles, respawn, bala, lista_monedas, imagen_fondo, diccionario_animaciones, tiempo_ultimo_disparo, flag_disparo, duracion_maxima, dic_ojo, jefe_nivel: bool, Jefe) -> None:
        self._slave = pantalla
        self.imagen_fondo = fondo
        self.jugador = personaje_principal
        self.respawn = respawn
        self.bala = bala
        self.plataformas = lista_plataformas
        self.plataformas_movibles = plataformas_movibles
        self.lista_monedas = lista_monedas
        self.diccionario_animaciones = diccionario_animaciones
        self.dic_ojo = dic_ojo
        self.tiempo_ultimo_disparo = tiempo_ultimo_disparo
        self.flag_disparo = flag_disparo
        self.duracion_maxima = duracion_maxima
        self.nivel_superado = False
        # Tiempo inicial en milisegundos
        self.tiempo_inicial = pygame.time.get_ticks()
        self.jefe = Jefe
        self.nivel_jefe = jefe_nivel
        self.nombre_jugador = None
        self.numero_nivel = None

    def update(self, eventos):
        for evento in eventos:
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == KEYDOWN:
                if evento.key == K_TAB:
                    cambiar_modo()
        self.leer_teclas()
        self.actualizar_pantalla()
        self.actualizar_respawn()
        self.actualizar_habilidad()
        self.dibujar_rectangulos()
        self.blit_texto()
        self.verificar_fin_juego()
            

    def leer_teclas(self):
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_d]:
            self.jugador.que_hace = "Derecha"
        elif teclas[pygame.K_a]:
            self.jugador.que_hace = "Izquierda"
        elif teclas[pygame.K_w]:
            self.jugador.que_hace = "Salta"
        else:
            self.jugador.que_hace = "Quieto"

        self.flag_disparo = False
        if teclas[pygame.K_f]:
            self.flag_disparo = True
    
        
    def dibujar_rectangulos(self):
        if obtener_modo():
            pygame.draw.rect(self._slave, "blue", self.jugador.rectangulo_principal, 3)

            for plataforma in self.plataformas:
                pygame.draw.rect(self._slave, 'red', plataforma['rectangulo'], 3)

    def actualizar_pantalla(self):
        self._slave.blit(self.imagen_fondo, (0, 0))
        for trampa in self.plataformas_movibles:
            trampa.actualizar(self._slave)
            self.jugador.manejar_colision_trampa(trampa)
        self.jugador.actualizar(self._slave, self.plataformas)
        self.respawn.generar_todo(self.diccionario_animaciones,self.dic_ojo)
        if self.nivel_jefe == True:
            for jefe in self.jefe:
                jefe.update(self._slave, self.plataformas, self.jugador)
    
    def actualizar_respawn(self):
        for moneda in self.lista_monedas:
            moneda.actualizar(self._slave)
            self.jugador.obtener_moneda(self.lista_monedas)

        for vida in self.respawn.lista_vidas:
            vida.actualizar(5,self.plataformas,self._slave)
            self.respawn.sumar_vida()

        for premio in self.respawn.lista_premios:
            if not premio.tocada:
                premio.actualizar(5,self.plataformas,self._slave)
            if premio.disponible: 
                self.jugador.verificar_colision_premio(premio)

        for enemig in self.respawn.lista_enemigos:
            if not enemig.esta_muerto:
                self.respawn.verificar_colision_enemigo_respawn(self._slave)
                enemig.actualizar(self._slave, self.plataformas, self.jugador)
        
        for enemig in self.respawn.lista_ojos:
            if not enemig.esta_muerto:
                self.respawn.verificar_colision_ojo_respawn(self._slave)
                enemig.mover(self._slave, self.plataformas)

    def actualizar_habilidad(self):
        if self.jugador.habilidad_especial and self.flag_disparo:
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - self.tiempo_ultimo_disparo >= 1000:
                self.jugador.lanzar_proyectiles(self.bala)
                self.tiempo_ultimo_disparo = tiempo_actual
        self.bala.actualizar_proyectiles(self._slave,self.plataformas)

    
    def obtener_tiempo(self):
        return pygame.time.get_ticks()

    def blit_texto(self):
        tiempo_actual = self.obtener_tiempo()
        tiempo_transcurrido = (tiempo_actual - self.tiempo_inicial) // 1000  # Convertir a segundos
        tiempo_restante = max(0, self.duracion_maxima - tiempo_transcurrido * 1000)
        minutos = tiempo_restante // 60000  # Convertir milisegundos a minutos
        segundos = (tiempo_restante % 60000) // 1000  # Obtener los segundos restantes
        tiempo_formateado = f'{minutos:02}:{segundos:02}'

        font = pygame.font.Font(None, 36)
        texto_superficie = font.render(tiempo_formateado, True, (255, 255, 255))
        self._slave.blit(texto_superficie, (483, 19))

        font = pygame.font.Font(None, 36)
        texto_superficie = font.render(tiempo_formateado, True, (255, 255, 255))
        self._slave.blit(texto_superficie, (483, 19))
        # Blitear la cantidad de vidas
        font = pygame.font.Font(None, 36) 
        texto_vidas = font.render(f"X {self.jugador.vidas}", True, (255, 255, 255))
        self._slave.blit(texto_vidas, (123, 36))

        # Blitear la cantidad de puntos
        texto_puntos = font.render(f"Puntos: {self.jugador.puntuacion}", True, (255, 255, 255))
        self._slave.blit(texto_puntos, (815, 30))

    def verificar_fin_juego(self):
        tiempo_transcurrido_actual = pygame.time.get_ticks() - self.tiempo_inicial + self.tiempo_transcurrido
        if tiempo_transcurrido_actual >= self.duracion_maxima or self.jugador.esta_muerto:
            efectos_sonido['finalizo_game'].play()
            self.nivel_superado = True
            print("Fin del juego")

    def verificar_gano(self):
        if self.respawn.segundo_round and not self.respawn.lista_enemigos:
            if self.jugador.esta_muerto:
                self.jugador.puntuacion = 0
            guardar_puntuacion(self.nombre_jugador, self.jugador.puntuacion)
            efectos_sonido['finalizo_game'].play()
            self.nivel_superado = True
            if self.numero_nivel < 3:  # Suponiendo que solo hay 3 niveles en total
                progresos = cargar_progresos()
                progresos["progresos"][self.numero_nivel]["desbloqueado"] = True
                guardar_progreso(progresos)
            print("Fin del juego")

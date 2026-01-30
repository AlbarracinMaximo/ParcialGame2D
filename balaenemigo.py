from proyectiles import Disparo
import pygame

class BalaEnemigo(Disparo):
    def __init__(self, x, y, direccion, velocidad, path_image):
        super().__init__(x, y, direccion, velocidad,path_image)
        self.lista_proyectiles_enemigos = []

    def agregar_proyectil_enemigo(self, x, y, direccion, velocidad):
        proyectil = BalaEnemigo(x, y, direccion, velocidad, r"texturas\Enemigo\Aereos\proyectil.png")
        self.lista_proyectiles_enemigos.append(proyectil)

    def verificar_colision_proyectil_plataforma_o_pantalla(self,proyectil, plataformas,pantalla):
        for plataforma in plataformas:
            if proyectil.rectangulo.colliderect(plataforma["rectangulo"]):
                return 

        if proyectil.rectangulo.right < 0 or proyectil.rectangulo.left > pantalla.get_width() or proyectil.rectangulo.bottom < 0 or proyectil.rectangulo.top > pantalla.get_height():
            return True  # El proyectil está fuera de la pantalla, eliminarlo
        return False

    def verificar_colision_proyectil_jugador(self, proyectil, jugador):
        if proyectil.rectangulo.colliderect(jugador.rectangulo_principal):
            jugador.perder_vida()  # Restar una vida al jugador
            return True  # Indicar que hubo colisión con el jugador
        return False

    def actualizar_proyectiles_enemigos(self, pantalla, plataformas,jugador):
        proyectiles_a_eliminar = []

        for proyectil in self.lista_proyectiles_enemigos:
            proyectil.actualizar(pantalla)

            # Lógica de colisión con plataformas
            if self.verificar_colision_proyectil_plataforma_o_pantalla(proyectil, plataformas, pantalla):
                proyectiles_a_eliminar.append(proyectil)
                continue

            if self.verificar_colision_proyectil_jugador(proyectil,jugador):
                proyectiles_a_eliminar.append(proyectil)

        for proyectil in proyectiles_a_eliminar:
            self.lista_proyectiles_enemigos.remove(proyectil)

    def actualizar_proyectiles(self, pantalla, plataformas):
        # Lógica para actualizar proyectiles del personaje...
        pass
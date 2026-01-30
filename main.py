import pygame

pygame.font.init()
from UI_Menu import Inicio
from pygame.locals import *
import pygame, sys
from loads import icono

pygame.init()
pygame.mixer.init()


#Config de pantalla
W, H = 1024, 720
FPS = 30
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((W, H))


pygame.display.set_caption("Juego.exe")
pygame.display.set_icon(icono)
# Fondo
fondo = pygame.image.load(r"texturas\Menu\fondo.png")
fondo = pygame.transform.scale(fondo, (W,H))

#Cancion
cancion = r"texturas\Sounds\Musica\temaiken.mp3"
pygame.mixer.music.load(cancion)
pygame.mixer.music.play(-1)

formulario = Inicio(PANTALLA,10, 200, 500, 600, True, r"texturas\Menu\nada.png")
#nivel_actual = NivelTres(PANTALLA)


while True:
    RELOJ.tick(FPS)
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == QUIT:
            pygame.quit()
            sys.exit(0)
        if evento.type == pygame.MOUSEBUTTONDOWN: #Ubicacion en la pantalla
            print(evento.pos)

    #nivel_actual.update(eventos)
    PANTALLA.blit(fondo, (0, 0))
    formulario.update(eventos)

    pygame.display.update()

pygame.quit()
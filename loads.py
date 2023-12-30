import pygame

pygame.mixer.init()
#Voltear las imagenes a gusto
def girar_imagenes(lista_original, flip_x, flip_y):
    lista_girada = []

    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))

    return lista_girada

#Ajusta las imagenes
def reescalar_imagenes(diccionario_animaciones, ancho, alto):
    for clave in diccionario_animaciones:

        for i in range(len(diccionario_animaciones[clave])):
            img = diccionario_animaciones[clave][i]
            diccionario_animaciones[clave][i] = pygame.transform.scale(img, (ancho, alto))

#Para crear la plataforma
#############################
def crear_plataforma(visible, esPremio, esSuelo, esMuro, esAtravesable, tamaño, x, y, path = ""):
    plataforma = {}

    if visible:
        plataforma["superficie"] = pygame.image.load(path)
        plataforma["superficie"] = pygame.transform.scale(plataforma["superficie"], tamaño)
    else:
        plataforma["superficie"] = pygame.Surface(tamaño)

    plataforma["rectangulo"] = plataforma["superficie"].get_rect()
    plataforma["rectangulo"].x = x
    plataforma["rectangulo"].y = y
    plataforma["esPremio"] = esPremio
    plataforma["esMuro"] = esMuro
    plataforma["esSuelo"] = esSuelo
    plataforma["esAtravesable"] = esAtravesable

    return plataforma
#############################

#Icono del juego
icono = (pygame.image.load(r"texturas\flor.png"))

#MANZANICA
manzana = r"texturas\manzana.png"

#MANZANICA
vida_xp = r"texturas\vida.png"

#MANZANICA
coin = r"texturas\coin.png"

#Imagenes del personaje
personaje_quieto = [pygame.image.load(r"texturas\aru_quieto_1.png"),
                    pygame.image.load(r"texturas\aru_quieto_1.png"),
                    pygame.image.load(r"texturas\aru_quieto_1.png"),
                    pygame.image.load(r"texturas\aru_quieto_1.png"),
                    pygame.image.load(r"texturas\aru_quieto_2.png"),
                    pygame.image.load(r"texturas\aru_quieto_2.png"),
                    pygame.image.load(r"texturas\aru_quieto_2.png"),]
personaje_camina_derecha = [pygame.image.load(r"texturas\caminando_1.png"),
                            pygame.image.load(r"texturas\caminando_2.png"),
                            pygame.image.load(r"texturas\caminando_3.png")]
personaje_camina_izquierda = [pygame.image.load(r"texturas\caminando_1.png"),
                            pygame.image.load(r"texturas\caminando_2.png"),
                            pygame.image.load(r"texturas\caminando_3.png")]
#personaje_camina_izquierda = girar_imagenes(personaje_camina_derecha, True, False)
personaje_camina_izquierda = [pygame.transform.flip(img, True, False) for img in personaje_camina_izquierda]  # invertir izquierda
personaje_salta = [pygame.image.load(r"texturas\saltando.png")]
#Personaje muriendo animacion
personaje_muriendo = [pygame.image.load(r"texturas\aru_muerte_1.png"),
                            pygame.image.load(r"texturas\aru_muerte_2.png"),
                            pygame.image.load(r"texturas\aru_muerte_3.png")]
personaje_muerto = [pygame.image.load(r"texturas\aru_muerte_3.png")]

#Superpoderes
personaje_poderoso_quieto = [pygame.image.load(r"texturas\aru_mago_baculo_quieto.png"),
                            pygame.image.load(r"texturas\aru_mago_baculo_quieto.png"),
                            pygame.image.load(r"texturas\aru_mago_baculo_quieto.png"),
                            pygame.image.load(r"texturas\aru_frente_respirando_mago_2.png"),
                            pygame.image.load(r"texturas\aru_frente_respirando_mago_2.png"),
                            pygame.image.load(r"texturas\aru_frente_respirando_mago_2.png"),
                            pygame.image.load(r"texturas\aru_frente_respirando_mago_2.png")]
personaje_poderoso_derecha = [pygame.image.load(r"texturas\aru_mago_caminando1.png"),
                            pygame.image.load(r"texturas\aru_mago_caminando2.png"),
                            pygame.image.load(r"texturas\aru_mago_caminando3.png")]
personaje_poderoso_izquierda = [pygame.image.load(r"texturas\aru_mago_caminando1.png"),
                            pygame.image.load(r"texturas\aru_mago_caminando2.png"),
                            pygame.image.load(r"texturas\aru_mago_caminando3.png")]
personaje_poderoso_izquierda = girar_imagenes(personaje_poderoso_derecha,True, False)
#personaje_poderoso_izquierda = [pygame.transform.flip(img, True, False) for img in personaje_poderoso_izquierda]  # invertir izquierda
personaje_poderoso_salta = [pygame.image.load(r"texturas\aru_mago_salta.png")]

#Imagenes de los enemigos
enemigo_camina_izquierda = [pygame.image.load(r"texturas\enemigo_camina.png"),
                        pygame.image.load(r"texturas\enemigo_camina1.png"),
                        pygame.image.load(r"texturas\enemigo_camina2.png")]

enemigo_camina_derecha = [pygame.image.load(r"texturas\enemigo_camina.png"),
                        pygame.image.load(r"texturas\enemigo_camina1.png"),
                        pygame.image.load(r"texturas\enemigo_camina2.png")]
enemigo_camina_derecha = girar_imagenes(enemigo_camina_derecha,True, False)

enemigo_aplasta = [pygame.image.load(r"texturas\enemigo_camina2.png"),
                     pygame.image.load(r"texturas\muriendo1.png"),
                        pygame.image.load(r"texturas\muriendo2.png")]


jefe_camina_derecha = [pygame.image.load(r"texturas\Boss_1.png"),
                            pygame.image.load(r"texturas\Boss_2.png"),
                            pygame.image.load(r"texturas\Boss_3.png"),
                            pygame.image.load(r"texturas\Boss_4.png"),
                            pygame.image.load(r"texturas\Boss_5.png")]

jefe_camina_izquierda = [pygame.image.load(r"texturas\Boss_1.png"),
                            pygame.image.load(r"texturas\Boss_2.png"),
                            pygame.image.load(r"texturas\Boss_3.png"),
                            pygame.image.load(r"texturas\Boss_4.png"),
                            pygame.image.load(r"texturas\Boss_5.png")]
enemigo_camina_izquierda = girar_imagenes(enemigo_camina_izquierda,True, False)

jefe_muere = [pygame.image.load(r"texturas\aru_mago_baculo_quieto.png"),
                            pygame.image.load(r"texturas\aru_mago_baculo_quieto.png"),
                            pygame.image.load(r"texturas\aru_mago_baculo_quieto.png"),
                            pygame.image.load(r"texturas\aru_frente_respirando_mago_2.png"),
                            pygame.image.load(r"texturas\aru_frente_respirando_mago_2.png"),
                            pygame.image.load(r"texturas\aru_frente_respirando_mago_2.png"),
                            pygame.image.load(r"texturas\aru_frente_respirando_mago_2.png")]

hombrecito = pygame.image.load(r"texturas\hombrecito.png")
hombrecito = pygame.transform.scale(hombrecito, (50, 50))


coin = pygame.mixer.Sound(r"texturas\sound_coin.mp3")
sound_vida = pygame.mixer.Sound(r"texturas\sound_vida.mp3")
salto = pygame.mixer.Sound(r"texturas\salto.mp3")
finalizo_game = pygame.mixer.Sound(r"texturas\finalizo_game.mp3")
muerte_personaje = pygame.mixer.Sound(r"texturas\muere_mago.mp3")
golpe_enemigo = pygame.mixer.Sound(r"texturas\golpe_enemigo.mp3")
proyectil = pygame.mixer.Sound(r"texturas\sound_proyectil.mp3")
impacto = pygame.mixer.Sound(r"texturas\impact.mp3")
finalizo_game = pygame.mixer.Sound(r"texturas\finalizo_game.mp3")

fuente_system_enorme = pygame.font.SysFont("Swis721 Blk BT", 80)

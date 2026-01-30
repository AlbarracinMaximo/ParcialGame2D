import pygame

pygame.mixer.init()
pygame.font.init()
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
icono = (pygame.image.load(r"texturas\Icono\image.png"))

#MANZANICA
manzana = r"texturas\Mapas\Articulos\manzana.png"

#VIDA
vida_xp = r"texturas\Mapas\Articulos\vida.png"

#COIN
coin = r"texturas\Mapas\Articulos\coin.png"


#Imagenes del personaje
personaje_quieto = [pygame.image.load(r"texturas\Aru\Normal\aru_quieto_1.png"),
                    pygame.image.load(r"texturas\Aru\Normal\aru_quieto_1.png"),
                    pygame.image.load(r"texturas\Aru\Normal\aru_quieto_1.png"),
                    pygame.image.load(r"texturas\Aru\Normal\aru_quieto_1.png"),
                    pygame.image.load(r"texturas\Aru\Normal\aru_quieto_1.png"),
                    pygame.image.load(r"texturas\Aru\Normal\aru_quieto_1.png"),
                    pygame.image.load(r"texturas\Aru\Normal\aru_quieto_2.png"),
                    pygame.image.load(r"texturas\Aru\Normal\aru_quieto_2.png"),
                    pygame.image.load(r"texturas\Aru\Normal\aru_quieto_2.png"),
                    pygame.image.load(r"texturas\Aru\Normal\aru_quieto_2.png"),
                    pygame.image.load(r"texturas\Aru\Normal\aru_quieto_2.png"),]
personaje_camina_derecha = [pygame.image.load(r"texturas\Aru\Normal\caminando_1.png"),
                            pygame.image.load(r"texturas\Aru\Normal\caminando_2.png"),
                            pygame.image.load(r"texturas\Aru\Normal\caminando_3.png")]
personaje_camina_izquierda = [pygame.image.load(r"texturas\Aru\Normal\caminando_1.png"),
                            pygame.image.load(r"texturas\Aru\Normal\caminando_2.png"),
                            pygame.image.load(r"texturas\Aru\Normal\caminando_3.png")]
#personaje_camina_izquierda = girar_imagenes(personaje_camina_derecha, True, False)
personaje_camina_izquierda = [pygame.transform.flip(img, True, False) for img in personaje_camina_izquierda]  # invertir izquierda
personaje_salta = [pygame.image.load(r"texturas\Aru\Normal\saltando.png")]
#Personaje muriendo animacion
personaje_muriendo = [pygame.image.load(r"texturas\Aru\Normal\aru_muerte_1.png"),
                      pygame.image.load(r"texturas\Aru\Normal\aru_muerte_1.png"),
                      pygame.image.load(r"texturas\Aru\Normal\aru_muerte_1.png"),
                        pygame.image.load(r"texturas\Aru\Normal\aru_muerte_2.png"),
                        pygame.image.load(r"texturas\Aru\Normal\aru_muerte_2.png"),
                        pygame.image.load(r"texturas\Aru\Normal\aru_muerte_2.png"),
                        pygame.image.load(r"texturas\Aru\Normal\aru_muerte_3.png")]
personaje_muerto = [pygame.image.load(r"texturas\Aru\Normal\aru_muerte_3.png")]


#Superpoderes
personaje_poderoso_quieto = [pygame.image.load(r"texturas\Aru\Mago\aru_mago_baculo_quieto.png"),
                            pygame.image.load(r"texturas\Aru\Mago\aru_mago_baculo_quieto.png"),
                            pygame.image.load(r"texturas\Aru\Mago\aru_mago_baculo_quieto.png"),
                            pygame.image.load(r"texturas\Aru\Mago\aru_frente_respirando_mago_2.png"),
                            pygame.image.load(r"texturas\Aru\Mago\aru_frente_respirando_mago_2.png"),
                            pygame.image.load(r"texturas\Aru\Mago\aru_frente_respirando_mago_2.png"),
                            pygame.image.load(r"texturas\Aru\Mago\aru_frente_respirando_mago_2.png")]
personaje_poderoso_derecha = [pygame.image.load(r"texturas\Aru\Mago\aru_mago_caminando1.png"),
                            pygame.image.load(r"texturas\Aru\Mago\aru_mago_caminando2.png"),
                            pygame.image.load(r"texturas\Aru\Mago\aru_mago_caminando3.png")]
personaje_poderoso_izquierda = [pygame.image.load(r"texturas\Aru\Mago\aru_mago_caminando1.png"),
                            pygame.image.load(r"texturas\Aru\Mago\aru_mago_caminando2.png"),
                            pygame.image.load(r"texturas\Aru\Mago\aru_mago_caminando3.png")]
personaje_poderoso_izquierda = girar_imagenes(personaje_poderoso_derecha,True, False)
#personaje_poderoso_izquierda = [pygame.transform.flip(img, True, False) for img in personaje_poderoso_izquierda]  # invertir izquierda
personaje_poderoso_salta = [pygame.image.load(r"texturas\Aru\Mago\aru_mago_salta.png")]


#Imagenes de los enemigos
enemigo_camina_izquierda = [pygame.image.load(r"texturas\Enemigo\Terrestres\enemigo_camina.png"),
                            pygame.image.load(r"texturas\Enemigo\Terrestres\enemigo_camina.png"),
                        pygame.image.load(r"texturas\Enemigo\Terrestres\enemigo_camina.png"),
                        pygame.image.load(r"texturas\Enemigo\Terrestres\enemigo_camina1.png"),
                        pygame.image.load(r"texturas\Enemigo\Terrestres\enemigo_camina1.png"),
                        pygame.image.load(r"texturas\Enemigo\Terrestres\enemigo_camina1.png"),
                        pygame.image.load(r"texturas\Enemigo\Terrestres\enemigo_camina2.png"),
                        pygame.image.load(r"texturas\Enemigo\Terrestres\enemigo_camina2.png"),
                        pygame.image.load(r"texturas\Enemigo\Terrestres\enemigo_camina2.png")]

enemigo_camina_derecha = [pygame.image.load(r"texturas\Enemigo\Terrestres\enemigo_camina.png"),
                            pygame.image.load(r"texturas\Enemigo\Terrestres\enemigo_camina.png"),
                        pygame.image.load(r"texturas\Enemigo\Terrestres\enemigo_camina.png"),
                        pygame.image.load(r"texturas\Enemigo\Terrestres\enemigo_camina1.png"),
                        pygame.image.load(r"texturas\Enemigo\Terrestres\enemigo_camina1.png"),
                        pygame.image.load(r"texturas\Enemigo\Terrestres\enemigo_camina1.png"),
                        pygame.image.load(r"texturas\Enemigo\Terrestres\enemigo_camina2.png"),
                        pygame.image.load(r"texturas\Enemigo\Terrestres\enemigo_camina2.png"),
                        pygame.image.load(r"texturas\Enemigo\Terrestres\enemigo_camina2.png")]
enemigo_camina_derecha = girar_imagenes(enemigo_camina_derecha,True, False)

enemigo_aplasta = [pygame.image.load(r"texturas\Enemigo\Terrestres\enemigo_camina2.png"),
                     pygame.image.load(r"texturas\Enemigo\Terrestres\muriendo1.png"),
                     pygame.image.load(r"texturas\Enemigo\Terrestres\muriendo1.png"),
                     pygame.image.load(r"texturas\Enemigo\Terrestres\muriendo1.png"),
                     pygame.image.load(r"texturas\Enemigo\Terrestres\muriendo1.png"),
                     pygame.image.load(r"texturas\Enemigo\Terrestres\muriendo2.png"),
                     pygame.image.load(r"texturas\Enemigo\Terrestres\muriendo2.png"),
                     pygame.image.load(r"texturas\Enemigo\Terrestres\muriendo2.png"),
                     pygame.image.load(r"texturas\Enemigo\Terrestres\muriendo2.png"),
                        pygame.image.load(r"texturas\Enemigo\Terrestres\muriendo2.png")]

#Enemigo volador
enemigo_volado_izquierda = [pygame.image.load(r"texturas\Enemigo\Aereos\enemigo_volador_2.png"),
                     pygame.image.load(r"texturas\Enemigo\Aereos\enemigo_volador_2.png"),
                     pygame.image.load(r"texturas\Enemigo\Aereos\enemigo_volador_2.png"),
                     pygame.image.load(r"texturas\Enemigo\Aereos\enemigo_volador_3.png"),
                     pygame.image.load(r"texturas\Enemigo\Aereos\enemigo_volador_3.png"),
                        pygame.image.load(r"texturas\Enemigo\Aereos\enemigo_volador_3.png")]
enemigo_volador_derecha = [pygame.image.load(r"texturas\Enemigo\Aereos\enemigo_volador_2.png"),
                     pygame.image.load(r"texturas\Enemigo\Aereos\enemigo_volador_2.png"),
                     pygame.image.load(r"texturas\Enemigo\Aereos\enemigo_volador_2.png"),
                     pygame.image.load(r"texturas\Enemigo\Aereos\enemigo_volador_3.png"),
                     pygame.image.load(r"texturas\Enemigo\Aereos\enemigo_volador_3.png"),
                        pygame.image.load(r"texturas\Enemigo\Aereos\enemigo_volador_3.png")]
enemigo_volador_derecha = girar_imagenes(enemigo_volador_derecha,True, False)
enemigo_volador_muerto = [pygame.image.load(r"texturas\Enemigo\Aereos\enemigo_volador_2.png"),
                     pygame.image.load(r"texturas\Enemigo\Aereos\enemigo_volador_2.png"),
                        pygame.image.load(r"texturas\Enemigo\Aereos\enemigo_volador_2.png")]




#BOSS
jefe_camina_derecha = [pygame.image.load(r"texturas\Enemigo\Boss\Boss_1.png"),
                            pygame.image.load(r"texturas\Enemigo\Boss\Boss_2.png"),
                            pygame.image.load(r"texturas\Enemigo\Boss\Boss_3.png"),
                            pygame.image.load(r"texturas\Enemigo\Boss\Boss_4.png"),
                            pygame.image.load(r"texturas\Enemigo\Boss\Boss_5.png")]

jefe_camina_izquierda = [pygame.image.load(r"texturas\Enemigo\Boss\Boss_1.png"),
                            pygame.image.load(r"texturas\Enemigo\Boss\Boss_2.png"),
                            pygame.image.load(r"texturas\Enemigo\Boss\Boss_3.png"),
                            pygame.image.load(r"texturas\Enemigo\Boss\Boss_4.png"),
                            pygame.image.load(r"texturas\Enemigo\Boss\Boss_5.png")]
jefe_camina_izquierda = girar_imagenes(jefe_camina_izquierda,True, False)

jefe_ataca = [pygame.image.load(r"texturas\Enemigo\Boss\boss ataque 1.png"),
                            pygame.image.load(r"texturas\Enemigo\Boss\boss ataque 2.png"),
                            pygame.image.load(r"texturas\Enemigo\Boss\boss ataque 3.png"),
                            pygame.image.load(r"texturas\Enemigo\Boss\boss ataque 4.png"),
                            pygame.image.load(r"texturas\Enemigo\Boss\boss ataque 5.png"),
                            pygame.image.load(r"texturas\Enemigo\Boss\boss ataque 6.png")]

jefe_daño = [pygame.image.load(r"texturas\Enemigo\Boss\boss daño 1.png"),
                            pygame.image.load(r"texturas\Enemigo\Boss\boss daño 1.png"),
                            pygame.image.load(r"texturas\Enemigo\Boss\boss daño 1.png"),
                            pygame.image.load(r"texturas\Enemigo\Boss\boss daño 2.png"),
                            pygame.image.load(r"texturas\Enemigo\Boss\boss daño 2.png"),
                            pygame.image.load(r"texturas\Enemigo\Boss\boss daño 2.png"),
                            pygame.image.load(r"texturas\Enemigo\Boss\boss daño 3.png"),
                            pygame.image.load(r"texturas\Enemigo\Boss\boss daño 3.png"),
                            pygame.image.load(r"texturas\Enemigo\Boss\boss daño 3.png")]

jefe_mueriendo = [pygame.image.load(r"texturas\Enemigo\Boss\boss muriendo 1.png"),
                            pygame.image.load(r"texturas\Enemigo\Boss\boss muriendo 2.png"),
                            pygame.image.load(r"texturas\Enemigo\Boss\boss muriendo 3.png"),
                            pygame.image.load(r"texturas\Enemigo\Boss\boss muriendo 4.png"),
                            pygame.image.load(r"texturas\Enemigo\Boss\boss muriendo 5.png"),
                            pygame.image.load(r"texturas\Enemigo\Boss\boss muriendo 6.png"),
                            pygame.image.load(r"texturas\Enemigo\Boss\boss muriendo 7.png")]

jefe_muerto = [pygame.image.load(r"texturas\Enemigo\Boss\boss muriendo 7.png")]


hombrecito = pygame.image.load(r"texturas\hombrecito.png")
hombrecito = pygame.transform.scale(hombrecito, (50, 50))

efectos_sonido = {
    'coin': pygame.mixer.Sound(r"texturas\Sounds\Efectos\sound_coin.mp3"),
    'vida': pygame.mixer.Sound(r"texturas\Sounds\Efectos\sound_vida.mp3"),
    'proyectil': pygame.mixer.Sound(r"texturas\Sounds\Efectos\sound_proyectil.mp3"),
    'impacto': pygame.mixer.Sound(r"texturas\Sounds\Efectos\impact.mp3"),
    'finalizo_game': pygame.mixer.Sound(r"texturas\Sounds\Efectos\finalizo_game.mp3"),
    'salto': pygame.mixer.Sound(r"texturas\Sounds\Personajes\salto.mp3"),
    'muerte_personaje': pygame.mixer.Sound(r"texturas\Sounds\Personajes\muere_mago.mp3"),
    'golpe_enemigo': pygame.mixer.Sound(r"texturas\Sounds\Enemigos\golpe_enemigo.mp3")
}

def activar_sonidos(efectos_sonido):
    for sonido in efectos_sonido.values():
        sonido.set_volume(1.0)

def desactivar_sonidos(efectos_sonido):
    for sonido in efectos_sonido.values():
        sonido.set_volume(0.0)

fuente_system_enorme = pygame.font.SysFont("Swis721 Blk BT", 80)

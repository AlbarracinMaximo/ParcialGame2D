from loads import *
from plataforma_movible import plataformas_movible
from trampa import *


#NIVEL UNO
#Plataforma, suelo
piso_bajo_uno = crear_plataforma(False, False, True, False, False, (228, 10), 168, 640)
piso_bajo_dos = crear_plataforma(False, False, True, False, False, (455, 10), 569, 636)
piso_medio = crear_plataforma(False, False, True, False, False, (171, 10), 0, 448)
piso_alto = crear_plataforma(False, False, True, False, False, (160, 10), 347, 192)
piso_alto_dos = crear_plataforma(False, False, True, False, False, (160, 10), 347, 319)

#Muros
muro_medio_derecho = crear_plataforma(False, False, False, True, False, (10, 192), 158, 458)
muro_alto_izquierdo = crear_plataforma(False, False, False, True, False, (10, 117), 341, 202)
muro_alto_derecho = crear_plataforma(False, False, False, True, False, (10, 117), 502, 202)

#Plataformas atravesables
piso_medio_apoyo = crear_plataforma(False, False, True, False, False, (113, 10), 172, 448)
piso_alto_apoyo_atravesable = crear_plataforma(False, False, False, False, True, (113, 10), 228, 295)

#Plataforma movible
trampa_baja = PlataformaTrampa((80, 40), 420, 325, 100, 0,(325, 380,0,0), 10000, r"texturas\Mapas\Articulos\plataforma_trampa.png")
plataforma_movimiento = plataformas_movible((100, 20), 650, 450, 0, 10,(0,0,610,800),500,r"texturas\Mapas\Articulos\plataforma_trampa.png")


#NIVEL DOS

piso_cueva_bajo_uno = crear_plataforma(False, False, True, False, False, (191, 10), 114, 630)
piso_cueva_bajo_dos = crear_plataforma(False, False, True, False, False, (142, 10), 881, 630)

piso_cueva_media_dos = crear_plataforma(False, False, True, False, False, (169, 10), 338, 468)

piso_cueva_alta = crear_plataforma(False, False, True, False, False, (311, 15), 669, 384)

piso_casa = crear_plataforma(False, False, True, False, False, (67, 10), 0, 487)

piso_inmovil = PlataformaTrampa((177, 30), 130, 350, 1, 0,(290, 380,0,0), 0, r"texturas\Mapas\Articulos\plataforma_trampa.png")
plataforma_dos = plataformas_movible((100, 20), 430, 573, 0, 4,(0,0,430,770),0,r"texturas\Mapas\Articulos\movil.png")
#piso_cueva_media_dos = crear_plataforma(False, False, True, False, False, (142, 10), 590, 573)

#Nivel TRES
boss_pltaforma = crear_plataforma(False, False, True, False, False, (1023, 10), 0, 555)

piso_inmovil_boss = PlataformaTrampa((177, 30), 640, 372, 0, 0,(290, 380,0,0), 0, r"texturas\Mapas\Articulos\plataforma_trampa.png")

piso_inmovil_boss_dos = PlataformaTrampa((177, 30), 130, 372, 0, 0,(290, 380,0,0), 0, r"texturas\Mapas\Articulos\plataforma_trampa.png")
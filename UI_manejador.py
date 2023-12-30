from class_nivel1 import *
from class_nivel2 import *
from class_nivel3 import*

class ManejadorNiveles:
    def __init__(self, pantalla) -> None:
        self._slave = pantalla
        self.niveles = {"Nivel_1": NivelUno, "Nivel_2": NivelDos,"Nivel_3": NivelTres}

    def get_nivel(self, nombre_nivel):
        return self.niveles[nombre_nivel](self._slave)


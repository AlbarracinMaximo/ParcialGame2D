# Cargar progresos
import json

def cargar_progresos():
    try:
        with open("progreso.json", "r") as archivo_progreso:
            return json.load(archivo_progreso)
    except FileNotFoundError:
        # Si el archivo no existe, crea uno nuevo con valores predeterminados
        progreso_inicial = {
            "progresos": [
                {"nivel": 1, "desbloqueado": True, "puntaje": 0},
                {"nivel": 2, "desbloqueado": False, "puntaje": None},
                {"nivel": 3, "desbloqueado": False, "puntaje": None}
            ]
        }
        with open("progreso.json", "w") as archivo_progreso:
            json.dump(progreso_inicial, archivo_progreso)
        return progreso_inicial
# Guardar progresos
def guardar_progreso(progreso):
    with open("progreso.json", "w") as archivo_progreso:
        json.dump(progreso, archivo_progreso)

def resetear_progreso():
    progreso_inicial = {
        "progresos": [
            {"nivel": 1, "desbloqueado": True, "puntaje": 0},
            {"nivel": 2, "desbloqueado": False, "puntaje": None},
            {"nivel": 3, "desbloqueado": False, "puntaje": None}
        ]
    }
    with open("progreso.json", "w") as archivo_progreso:
        json.dump(progreso_inicial, archivo_progreso)
    return progreso_inicial

def obtener_puntaje_nivel(numero_nivel):
    with open("progreso.json", "r") as archivo_progreso:
        progreso = json.load(archivo_progreso)
        progresos = progreso["progresos"]
        for progreso_nivel in progresos:
            if progreso_nivel["nivel"] == numero_nivel:
                return progreso_nivel["puntaje"]
    return None  # Retornar None si no se encuentra el nivel
# # Ejemplo de uso
# progresos = cargar_progresos()
# progresos["progresos"][0]["desbloqueado"] = True  # Desbloquear nivel 1
# progresos["progresos"][0]["puntaje"] = 1000  # Establecer puntaje para nivel 1
# guardar_progresos(progresos)
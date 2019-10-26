import Dominio.EspacioEstados as EspacioEstados
import Dominio.Cubo as Cubo
import math

class Problema:
    def __init__(self, json):
        self.espacioEstados = EspacioEstados(json)
        self.estadoInicial = Cubo(json)

    def esObjetivo(self, Estado):
        if not Estado.listaPendientes:
            return True
        else:
            return False
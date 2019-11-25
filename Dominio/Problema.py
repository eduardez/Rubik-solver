from Dominio.EspacioEstados import EspacioEstados
from Dominio.Cubo import Cubo
import math, copy

class Problema:
    def __init__(self, cubo):
        self.espacioEstados = EspacioEstados()
        self.estadoInicial = cubo
        self.estadoInicial.updateEstado()

    def esObjetivo(self, NodoArbolActual):
        cuboActual = [NodoArbolActual.cubo.back, NodoArbolActual.cubo.down, 
                      NodoArbolActual.cubo.front, NodoArbolActual.cubo.left, 
                      NodoArbolActual.cubo.right, NodoArbolActual.cubo.up]
        for cara in cuboActual:
            for i in range(0, NodoArbolActual.cubo.getCuboSize()):
                for j in range(0, NodoArbolActual.cubo.getCuboSize()):
                    if cara[0][0] != cara[i][j]:
                        return False
        return True          

        
            
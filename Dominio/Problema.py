from Dominio.EspacioEstados import EspacioEstados
from Dominio.Cubo import Cubo
import math, copy

class Problema:
    def __init__(self, json):
        self.espacioEstados = EspacioEstados(json)
        self.estadoInicial = Cubo(json)
        self.estadoInicial.updateEstado()
        self.estadoObjetivo = self.getCuboObjetivo(self.estadoInicial)

    def esObjetivo(self, NodoArbolActual):
        if self.estadoObjetivo == NodoArbolActual.cubo.idHash:
            return True
        else:
            return False
    
    def getCuboObjetivo(self, cubo_original):
        mapa_colores = {'BACK':3,'DOWN':1,'FRONT':2,'LEFT':4,'RIGHT':5,'UP':0}
        cubo_objetivo = copy.deepcopy(cubo_original)
        longitud = cubo_objetivo.getCuboSize() 
        for i in range(0, longitud):
            for j in range(0, longitud):    #Original #Profesores
                cubo_objetivo.back[i][j] = 2 #3 #2
                cubo_objetivo.down[i][j] = 5 #1 #5
                cubo_objetivo.front[i][j] = 3 #2 #3
                cubo_objetivo.left[i][j] = 1 #4 #1
                cubo_objetivo.right[i][j] = 0 #5 #0
                cubo_objetivo.up[i][j] = 4 #0 #4
        cubo_objetivo.updateEstado()
        return cubo_objetivo.idHash
    
    
    def __str__(self):
        cadena = f'Estado inicial: {str(self.estadoInicial.idHash)}\nEstado objetivo: {str(self.estadoObjetivo)}'
        return cadena
                
            
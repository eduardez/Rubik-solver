#!/usr/bin/python3
# -*- coding: utf-8 -*-
import copy
import Dominio.utils as utils, cmd, sys
from Dominio.Cubo import Cubo

class EspacioEstados:
    def __init__(self, json):
        # self.cubo = Cubo(json)
        pass
    
    '''Este método genera tripetas (Acción realizada, New_Objeto_Cubo, CosteAcción = 1)
    que son añadidas a la lista de sucesores, total de tripletas generadas es igual a
    el número de movimientos (estático) multiplicado por el numero de filas del cubo,
    es decir todas las acciones posibles'''
    def sucesores(self, NodoArbolActual):
        listaSucesores = []
        for x in range(0, NodoArbolActual.cubo.getCuboSize()):
            new_cubo = copy.deepcopy(NodoArbolActual.cubo)
            new_cubo.desplazamientoB(x)
            listaSucesores.append(("Desplazamiento B" + str(x), new_cubo, 1))

            new_cubo = copy.deepcopy(NodoArbolActual.cubo)
            new_cubo.desplazamientob(x)
            listaSucesores.append(("Desplazamiento b" + str(x), new_cubo, 1))

            new_cubo = copy.deepcopy(NodoArbolActual.cubo)
            new_cubo.desplazamientoL(x)
            listaSucesores.append(("Desplazamiento L" + str(x), new_cubo, 1))

            new_cubo = copy.deepcopy(NodoArbolActual.cubo)
            new_cubo.desplazamientol(x)
            listaSucesores.append(("Desplazamiento l" + str(x), new_cubo, 1))

            new_cubo = copy.deepcopy(NodoArbolActual.cubo)
            new_cubo.desplazamientoD(x)
            listaSucesores.append(("Desplazamiento D" + str(x), new_cubo, 1))

            new_cubo = copy.deepcopy(NodoArbolActual.cubo)
            new_cubo.desplazamientod(x)
            listaSucesores.append(("Desplazamiento d" + str(x), new_cubo, 1))
        return listaSucesores


#!/usr/bin/python3
# -*- coding: utf-8 -*-
import copy
import cmd, sys
from Dominio.Cubo import Cubo

class EspacioEstados:
   
    def sucesores(self, NodoArbolActual):
        '''Este método genera tripetas (Acción realizada, New_Objeto_Cubo, CosteAcción = 1)
        que son añadidas a la lista de sucesores, total de tripletas generadas es igual a
        el número de movimientos (estático) multiplicado por el numero de filas del cubo,
        es decir, todas las acciones posibles'''
        
        listaSucesores = []
        for x in range(0, NodoArbolActual.cubo.getCuboSize()):
            new_cubo = copy.deepcopy(NodoArbolActual.cubo)
            new_cubo.desplazamientoB(x)
            listaSucesores.append(("B" + str(x), new_cubo, 1))

        for x in range(0, NodoArbolActual.cubo.getCuboSize()):
            new_cubo = copy.deepcopy(NodoArbolActual.cubo)
            new_cubo.desplazamientob(x)
            listaSucesores.append(("b" + str(x), new_cubo, 1))

        for x in range(0, NodoArbolActual.cubo.getCuboSize()):
            new_cubo = copy.deepcopy(NodoArbolActual.cubo)
            new_cubo.desplazamientoD(x)
            listaSucesores.append(("D" + str(x), new_cubo, 1))

        for x in range(0, NodoArbolActual.cubo.getCuboSize()):
            new_cubo = copy.deepcopy(NodoArbolActual.cubo)
            new_cubo.desplazamientod(x)
            listaSucesores.append(("d" + str(x), new_cubo, 1))

        for x in range(0, NodoArbolActual.cubo.getCuboSize()):
            new_cubo = copy.deepcopy(NodoArbolActual.cubo)
            new_cubo.desplazamientoL(x)
            listaSucesores.append(("L" + str(x), new_cubo, 1))

        for x in range(0, NodoArbolActual.cubo.getCuboSize()):
            new_cubo = copy.deepcopy(NodoArbolActual.cubo)
            new_cubo.desplazamientol(x)
            listaSucesores.append(("l" + str(x), new_cubo, 1))

        return listaSucesores


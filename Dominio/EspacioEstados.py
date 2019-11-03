#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Dominio.utils as utils, copy, cmd, sys
from Dominio.Cubo import Cubo

class EspacioEstados:
    def __init__(self, json):
        # self.cubo = Cubo(json)
        pass
    
    '''Este método genera tripetas (Acción realizada, New_Objeto_Cubo, CosteAcción = 1)
    que son añadidas a la lista de sucesores, total de tripletas generadas es igual a
    el número de movimientos (estático) multiplicado por el numero de filas del cubo,
    es decir todas las acciones posibles'''
    def sucesores(self, cubo):
        listaSucesores = []
        for x in range(0, cubo.getCuboSize()-1):
            new_cubo = copy.deepcopy(cubo)
            listaSucesores.append(("Desplazamiento B" + str(x), new_cubo.desplazamientoB(x), 1))

            new_cubo = copy.deepcopy(cubo)
            listaSucesores.append(("Desplazamiento b" + str(x), new_cubo.desplazamientob(x), 1))

            new_cubo = copy.deepcopy(cubo)
            listaSucesores.append(("Desplazamiento L" + str(x), new_cubo.desplazamientoL(x), 1))

            new_cubo = copy.deepcopy(cubo)
            listaSucesores.append(("Desplazamiento l" + str(x), new_cubo.desplazamientol(x), 1))

            new_cubo = copy.deepcopy(cubo)
            listaSucesores.append(("Desplazamiento D" + str(x), new_cubo.desplazamientoD(x), 1))

            new_cubo = copy.deepcopy(cubo)
            listaSucesores.append(("Desplazamiento d" + str(x), new_cubo.desplazamientod(x), 1))

        return listaSucesores

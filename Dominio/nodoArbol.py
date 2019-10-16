#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import Dominio.Cubo

class nodoArbol:
    def __init__(self, cubo):
        self.estado = cubo
        self.coste = 1
        self.accion = ''
        self.profundidad = 0
        self.f = random.random() * 1000
       # self.f = self.getF()


    # def getF(self, algoritmo):
    #     if algoritmo == 'anchura':
    #         self.f=self.coste
    #         pass
    #     elif algoritmo == 'profundidad':
    #         self.f = 1/(self.profundidad+1)
    #         pass
    #     elif algoritmo == 'estrella':
    #         self.f = self.coste + self.heuristica
    #         pass
    #     elif algoritmo == 'coste':
    #         self.f = self.profundidad
    #         pass
    #     return f

    def calcularHeuristica(self):
        pass
    
    def __str__(self):
        return ('\nID: ' + str(self.estado.idHash) + '\nF: ' + str(self.f) + '\n')

 


    

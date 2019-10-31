#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import Dominio.Cubo

class NodoArbol:

    def __init__(self, nodoPadre, Cubo, profundidad,coste,f):
        self.cubo = Cubo
        self.nodoPadre = None
        self.f = f
        if nodoPadre == None:
            self.accion = 'Cubo Inicial'
            self.profundidad = 0
            self.coste = 0
        else:
            self.nodoPadre=nodoPadre
            self.profundidad=profundidad
            self.coste = coste
            self.accion = "     "+nodoPadre.cubo.nodoActual + "->" + self.cubo.nodoActual + " | " +" f:"+ str(self.f) + " p: " + str(profundidad) +" |"
     
    def calcularHeuristica(self):
        pass
    
    def __str__(self):
        return ('\nID: ' + str(self.cubo.idHash) + '\nF: ' + str(self.f) + '\n')


 


    

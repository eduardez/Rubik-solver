#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import Dominio.Cubo

class NodoArbol:

    def __init__(self, nodoPadre, Cubo, profundidad,coste,f):
        if nodoPadre == None:
            self.nodoPadre = None
            self.cubo = Cubo
            self.profundidad = 0
            self.coste = 0
            self.accion = 'Cubo Inicial'
            self.f = f
        else:
            self.nodoPadre=nodoPadre
            self.cubo = Cubo
            self.profundidad=profundidad
            self.coste = coste
            self.accion = None
            self.f = f
            
    def calcularHeuristica(self):
        pass
    
    
    def __lt__(self, otro_nodo):
        '''Metodo _comparable_ de python para que el nodo arbol pueda
        meterse sin problemas en la priority queue.'''
        return self.f < otro_nodo.f

    def __str__(self):
        return ('\nAcción: ' + self.accion +
                '\nID: ' + str(self.cubo.idHash) + 
                '\nF: ' + str(self.f) +
                '\nProfundidad: ' + str(self.profundidad) +
                '\nCosto Accion: ' + str(self.coste) +
                '\n'+ str(self.cubo) +'\n')


 


    

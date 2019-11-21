#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import Dominio.Cubo

class NodoArbol:

    def __init__(self, nodoPadre, Cubo, profundidad,coste,f, identidad):
        self.cubo = Cubo
        self.f = f
        self.id = identidad
        if nodoPadre == None:
            self.nodoPadre = None
            self.profundidad = 0
            self.coste = 0
            self.accion = 'Cubo Inicial'
        else:
            self.nodoPadre=nodoPadre
            self.profundidad=profundidad
            self.coste = coste
            self.accion = None
            
    def calcularHeuristica(self):
        pass
    
    
    def __lt__(self, otro_nodo):
        '''Metodo _comparable_ de python para que el nodo arbol pueda
        meterse sin problemas en la priority queue.'''
        # if self.f < otro_nodo.f:
        #     return self
        # elif self.f > otro_nodo.f:
        #     return otro_nodo
        # elif self.f == otro_nodo.f:
        #     if self.id < otro_nodo.id:
        #         return self
        #     else:
        #         return otro_nodo
        if not self.f == otro_nodo.f:
            return self.f < otro_nodo.f
        else:
            return self.id < otro_nodo.id



    def __str__(self):
        return ('\nAcción: ' + self.accion +
                '\nEstado: ' + str(self.cubo.idHash) + 
                '\nF: ' + str(self.f) + '   |   ID:' + str(self.id) +
                '\nProfundidad: ' + str(self.profundidad) +
                '\nCosto Accion: ' + str(self.coste) +
                '\n'+ str(self.cubo) +'\n')


 


    

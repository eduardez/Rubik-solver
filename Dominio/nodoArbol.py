#!/usr/bin/python3
# -*- coding: utf-8 -*-

class nodoArbol:

    def __init__(self):
        self.estado = cubo
        self.coste = 1
        self.accion = ''
        self.profundidad = 0
        self.f = getF(self)

    def getF(self, algoritmo):
        if algoritmo == 'anchura':
            self.f=self.coste
            pass
        elif algoritmo == 'profundidad':
            self.f = 1/(self.profundidad+1)
            pass
        elif algoritmo == 'estrella':
            pass
        elif algoritmo == 'coste':
            self.f = self.profundidad
            pass
        return f




    

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random, math
import Dominio.Cubo

class NodoArbol:

    def __init__(self, nodoPadre, Cubo, profundidad,coste,f, identidad):
        '''Constructor del objeto nodo'''
        self.cubo = Cubo
        self.f = f
        self.id = identidad
        self.heuristica = 0
        self.nodoPadre=nodoPadre
        self.profundidad=profundidad
        self.coste = coste
        self.accion = None
            
   
    def __lt__(self, otro_nodo):
        '''Metodo _comparable_ de python para que el nodo arbol pueda
        meterse sin problemas en la lista.'''
        if not self.f == otro_nodo.f:
            return self.f < otro_nodo.f
        else:
            return self.id < otro_nodo.id
        

    def __repr__(self):
        return (f'[{self.id}]([{str(self.accion)}]{self.cubo.idHash}, c={self.coste}, '
                +f'p={self.profundidad}, h={round(self.heuristica, 2)}, f={round(self.f, 2)})')

    def __str__(self):
        return ('\nAcción: ' + self.accion +
                '\nEstado: ' + str(self.cubo.idHash) + 
                '\nF: ' + str(self.f) + '   |   ID:' + str(self.id) +
                '\nProfundidad: ' + str(self.profundidad) +
                '\nCosto Accion: ' + str(self.coste) +
                '\n'+ str(self.cubo) +'\n')

    def calcularHeuristica(self):
        '''
        Metodo que calcula la heurística, siendo esta la suma de la entropía de todas las caras,
        siendo la entropia de la cara como:
          entropía=0
            for c= 0  to 5:
                if contador[c]>0.0:
                    entropía = entropía + contador[c]/(N*N) * math.log(contador[c]/(N*N),6)

        Siendo el desorden máximo con valor -1 y un mínimo de 0 (si toda la cara es del mismo color)

        '''
        cuboActual = [self.cubo.back, self.cubo.down, self.cubo.front, self.cubo.left, 
                    self.cubo.right, self.cubo.up]
        heur = 0.0
        N = self.cubo.getCuboSize()
        for cara in cuboActual:
            colors = [0.0,0.0,0.0,0.0,0.0,0.0]
            # Contar los colores de la cara
            for row in cara:
                for tile in row:
                    colors[tile] += 1.0
            # Calcular la entropia de la cara
            entropía = 0.0
            for c in colors:
                if c > 0.0:
                    entropía = entropía + c/(N*N) * math.log(c/(N*N),6)
            # Sumar la entropia de todas las caras
            heur += (-entropía)
        self.heuristica = heur
        
 


    

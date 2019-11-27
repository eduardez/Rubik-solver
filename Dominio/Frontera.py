#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np, hashlib, heapq
import Dominio.NodoArbol as NodoArbol
from queue import PriorityQueue


class Frontera:
    def __init__(self):
        self.frontera = []
        # self.visitados = dict({})# Formato -> {'id':0}
        self.idUltimoNodo = 0

    def insertarNodo(self, nodo):
        nodo.id = self.idUltimoNodo
        self.idUltimoNodo += 1
        heapq.heappush(self.frontera, nodo)

    def insertarLista(self, listaNodos):
        if not listaNodos is None:
            for nodoArbol in listaNodos:
                    self.insertarNodo(nodoArbol)

    def pop(self):
        if not self.isEmpty():
            return heapq.heappop(self.frontera)
        else:
            return 0
        
    def isVisitado(self, nodo):
        return nodo.cubo.idHash in self.visitados
    
    def isEmpty(self):
        return len(self.frontera) < 1 
        
    def __len__(self):
        return len(self.frontera)

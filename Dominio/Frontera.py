#!/usr/bin/python3
# -*- coding: utf-8 -*-

import hashlib
import heapq
from queue import PriorityQueue

import numpy as np

import Dominio.NodoArbol as NodoArbol


class Frontera:
    def __init__(self):
        self.frontera = []
        self.idUltimoNodo = 0
        self.num_total = 0

    def __len__(self):
        return len(self.frontera)

    def insertarLista(self, listaNodos):
        '''
        Introduce la lista de los nodos hijos del nodo actual en la frontera.
        '''
        if not listaNodos is None:
            for nodoArbol in listaNodos:
                self.insertarNodo(nodoArbol)

    def insertarNodo(self, nodo):
        ''' 
        Introduce nodo a nodo en la frontera
        '''
        nodo.id = self.idUltimoNodo
        self.num_total += 1
        self.idUltimoNodo += 1
        heapq.heappush(self.frontera, nodo)

    def isEmpty(self):
        return len(self.frontera) < 1

    def pop(self):
        if not self.isEmpty():
            return heapq.heappop(self.frontera)
        else:
            return 0

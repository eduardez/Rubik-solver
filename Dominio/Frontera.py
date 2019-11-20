import numpy as np, hashlib
import Dominio.NodoArbol as NodoArbol
from queue import PriorityQueue

class Frontera:
    def __init__(self):
        self.frontera = PriorityQueue()
        self.visitados = dict({"id":0})
        self.idUltimoNodo = 0

    def insertarNodo(self, nodo):
        nodo.id = self.idUltimoNodo
        self.idUltimoNodo += 1
        self.frontera.put(nodo, nodo.f)

    def insertarLista(self, listaNodos):
        optimizacion = True
        for nodoArbol in listaNodos:
            if optimizacion:
                if not self.isVisitado(nodoArbol): 
                    self.insertarNodo(nodoArbol)
                # elif self.isVisitado(nodoArbol) and (nodoArbol.f < self.visitados[nodoArbol.cubo.idHash]):
                #     self.insertarNodo(nodoArbol)
                #     del self.visitados[nodoArbol.cubo.idHash]

            else:
                self.insertarNodo(nodoArbol)

    def pop(self):
        if not self.isEmpty():
            return self.frontera.get()
        else:
            return 0
        
    def isVisitado(self, nodo):
        return nodo.cubo.idHash in self.visitados
    
    def isEmpty(self):
        return self.frontera.empty()
        
    def __len__(self):
        return len(self.frontera.queue)

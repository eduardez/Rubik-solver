import numpy as np, hashlib
import Dominio.NodoArbol as NodoArbol
from queue import PriorityQueue

class Frontera:
    def __init__(self):
        self.frontera = PriorityQueue()
        self.visitados = dict({"id":"0"})

    def insertarNodo(self, nodo):
        self.frontera.put(nodo)

    def insertarLista(self, listaNodos):
        optimizacion = True
        for nodoArbol in listaNodos:
            if optimizacion:
                if not(nodoArbol.cubo.idHash in self.visitados): 
                    self.insertarNodo(nodoArbol)
                    self.visitados.update({str(nodoArbol.cubo.idHash):str(nodoArbol.f)})
                elif nodoArbol.cubo.idHash in self.visitados and abs(nodoArbol.f) < abs(float(self.visitados.get(nodoArbol.cubo.idHash))):
                    self.insertarNodo(nodoArbol)
                    self.visitados.update({str(nodoArbol.cubo.idHash):str(nodoArbol.f)})
            else:
                self.insertarNodo(nodoArbol)

    def pop(self):
        if not self.isEmpty():
            return self.frontera.get()
        else:
            return 0

    def isEmpty(self):
        return self.frontera.empty()
        
    def __len__(self):
        return len(self.frontera.queue)

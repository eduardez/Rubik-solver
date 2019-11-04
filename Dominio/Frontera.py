import numpy as np, hashlib
import Dominio.NodoArbol as NodoArbol
from queue import PriorityQueue

class Frontera:
    def __init__(self):
        #self.frontera = np.array(dtype=NodoArbol)
        self.frontera = PriorityQueue()

    def insertarNodo(self, nodo):
        self.frontera.put(nodo)

    def insertarLista(self, listaNodos):
        for nodoArbol in listaNodos:
            self.insertarNodo(nodoArbol)
        # if hoja.estado.identificador == NodoArbol.estado.identificador :
        #     self.frontera.pop(i)

    def delete(self):
        if not self.isEmpty():
            return self.frontera.get()
        else:
            return 0

    def isEmpty(self):
        return self.frontera.empty()
        
    def __len__(self):
        return len(self.frontera.queue)

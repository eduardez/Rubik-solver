import numpy as np, hashlib
import Dominio.NodoArbol as NodoArbol

class Frontera:
    def __init__(self):
        #self.frontera = np.array(dtype=NodoArbol)
        self.frontera = []

    def insertarNodo(self, nodo):
        self.frontera.insert(0,nodo)

    def insertarLista(self, listaNodos):
        i = 0
        for nodoArbol in listaNodos:
            for hoja in self.frontera:
                if  nodoArbol.f <= hoja.f:
                    self.frontera.insert(i, nodoArbol)
                i=i+1
        # if hoja.estado.identificador == NodoArbol.estado.identificador :
        #     self.frontera.pop(i)
        
    def insercionInicial(self, listaNodos):
        i = 0
        for nodo in listaNodos:
            self.frontera.insert(i, nodo)
            i += 1
            
            
    def delete(self):
        if not self.isEmpty():
            return self.frontera.pop(0)
        else:
            return 0

    def isEmpty(self):
        if(not self.frontera):
            return True
        else:
            return False

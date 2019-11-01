import numpy as np, hashlib
import Dominio.NodoArbol as NodoArbol

class Frontera:
    def __init__(self):
        #self.frontera = np.array(dtype=NodoArbol)
        self.frontera = []

    def insertarLista(self, listaNodos):
        i = 0
        for hoja in self.frontera:
            for nodoArbol in listaNodos:
            
                if  nodoArbol.f <= hoja.f:
                    self.frontera.insert(nodoArbol, i)
                    break
                i=i+1
        # if hoja.estado.identificador == NodoArbol.estado.identificador :
        #     self.frontera.pop(i)

    def delete(self):
        if(not self.isEmpty()):
            return self.frontera.pop(0)
        else:
            return 0

    def isEmpty(self):
        if(not self.frontera):
            return True
        else:
            return False
            
    def isNotEmpty(self):
        if self.frontera:
            return False
        else:
            return True

class Frontera:
    def __init__(self):
        self.frontera = []

    def insert(self, NodoArbol):
        i = 0
        for hoja in self.frontera:
            if  NodoArbol.f <= hoja.f:
                self.frontera.insert(NodoArbol, i)
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

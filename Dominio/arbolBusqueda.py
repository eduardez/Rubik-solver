#!/usr/bin/python3
# -*- coding: utf-8 -*-

#https://www.quora.com/Whose-time-complexity-is-better-an-array-or-a-linked-list
#https://pandas.pydata.org/pandas-docs/stable/reference/series.html
# - - - -- - - - -  -- - - -- --- - -  - -
#Se ha decidido usar una lista porque aunque es más lento a la hora de buscar un nodo en memoria
#no hay que volver a colocar todos los elementos a la derecha de donde se modifique


#import pandas as pd

class arbolBusqueda:

    def __init__(self):
        self.frontera = []

    def insertar(self, nodoArbol, frontera):
        pass

    def eliminar(self, frontera):
        if estaVacia(self) is False:
            frontera.remove[0]
        pass

    def estaVacia(self, frontera):
        if frontera.len() == 0:
            return True
        elif frontera.len() >0:
            return False
        pass
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import Dominio.utils
import copy
import numpy as np
import hashlib


class Cubo:
    """Objeto cubo a partir de un objeto JSON (add doc)"""

    def __init__(self, json_data):
        '''
        El constructor de esta clase tomará como argumentos
        un archivo JSON, el cual se procesará para obtener 
        las distintas caras del cubo (Back, left, down...)
        '''
        self.back = np.array(json_data['BACK'], np.uint8)
        self.left = np.array(json_data['LEFT'], np.uint8)
        self.down = np.array(json_data['DOWN'], np.uint8)
        self.right = np.array(json_data['RIGHT'], np.uint8)
        self.up = np.array(json_data['UP'], np.uint8)
        self.front = np.array(json_data['FRONT'], np.uint8)
        self.idHash = self.updateEstado()  # Id del cubo (Hash)

    def updateEstado(self):
        '''
        Calcula el hash del cubo en su estado actual
        '''
        h = hashlib.md5(self.cuboToStr().encode('utf-8'))
        self.idHash = h.hexdigest()

    def desplazamientoB(self, fila):
        '''Moveremos la cara del cubo 90º, generando un cubo nuevo tras la modificación'''
        arr1 = copy.copy(self.left[fila])
        arr2 = copy.copy(self.down[fila])
        arr3 = copy.copy(self.right[fila])
        arr4 = copy.copy(self.up[fila])
        self.left[fila] = arr4
        self.down[fila] = arr1
        self.right[fila] = arr2
        self.up[fila] = arr3
        # extremo izq
        if fila == 0:
            self.back = np.rot90(self.back, 3)
        elif fila == len(self.back) - 1:
            self.front = np.rot90(self.front, 3)
        # centros
        else:
            pass
        self.updateEstado()

    def desplazamientob(self, fila):
        arr1 = copy.copy(self.left[fila])
        arr2 = copy.copy(self.down[fila])
        arr3 = copy.copy(self.right[fila])
        arr4 = copy.copy(self.up[fila])
        self.left[fila] = arr2
        self.down[fila] = arr3
        self.right[fila] = arr4
        self.up[fila] = arr1
        if fila == 0:
            self.back = np.rot90(self.back, 1)
        elif fila == len(self.back) - 1:
            self.front = np.rot90(self.front, 1)
        # centros
        else:
            pass
        self.updateEstado()

    def desplazamientoL(self, fila):
        # Indice de la cara UP ya que el posicionamiento va a la inversa del resto de las caras
        fila_prima = len(self.up) - fila - 1
        arr1 = self.getColumna(self.up, fila_prima)
        arr2 = self.getColumna(self.front, fila)
        arr3 = self.getColumna(self.down, fila)
        arr4 = self.getColumna(self.back, fila)
        # Hay que cambiar las filas por columna
        self.setColumnaInversa(self.up, fila_prima, arr4)
        self.setColumnaInversa(self.front, fila, arr1)
        self.setColumna(self.down, fila, arr2)
        self.setColumna(self.back, fila, arr3)
        if fila == 0:
            self.left = np.rot90(self.left, 3)
        # extremo drcho
        elif fila == len(self.back) - 1:
            self.right = np.rot90(self.right, 3)
        else:
            pass
        self.updateEstado()

    def desplazamientol(self, fila):
        # Indice de la cara UP ya que el posicionamiento va a la inversa del resto de las caras
        fila_prima = len(self.up) - fila - 1
        arr1 = self.getColumna(self.up, fila_prima)
        arr2 = self.getColumna(self.front, fila)
        arr3 = self.getColumna(self.down, fila)
        arr4 = self.getColumna(self.back, fila)
        # Hay que cambiar las filas por columnas
        self.setColumnaInversa(self.up, fila_prima, arr2)
        self.setColumna(self.front, fila, arr3)
        self.setColumna(self.down, fila, arr4)
        self.setColumnaInversa(self.back, fila, arr1)
        if fila == 0:
            self.left = np.rot90(self.left, 1)
        # extremo drcho
        elif fila == len(self.back) - 1:
            self.right = np.rot90(self.right, 1)
        else:
            pass
        self.updateEstado()

    def desplazamientoD(self, fila):
        # Indice de la cara UP ya que el posicionamiento va a la inversa del resto de las caras
        fila_prima = len(self.up) - fila - 1
        arr1 = self.getColumna(self.left, fila_prima)
        arr2 = copy.copy(self.back[fila_prima])
        arr3 = self.getColumna(self.right, fila)
        arr4 = copy.copy(self.front[fila])
        self.setColumna(self.left, fila_prima, arr4)
        self.back[fila_prima] = arr1[::-1]
        self.setColumna(self.right, fila, arr2)
        self.front[fila] = arr3[::-1]
        if fila == 0:
            self.down = np.rot90(self.down, 3)
        # extremo drcho
        elif fila == len(self.back) - 1:
            self.up = np.rot90(self.up, 3)
        # centros
        else:
            pass
        self.updateEstado()

    def desplazamientod(self, fila):
        fila_prima = len(self.up) - fila - 1
        arr1 = self.getColumna(self.left, fila_prima)
        arr2 = copy.copy(self.back[fila_prima])
        arr3 = self.getColumna(self.right, fila)
        arr4 = copy.copy(self.front[fila])
        self.setColumnaInversa(self.left, fila_prima, arr2)
        self.back[fila_prima] = arr3
        self.setColumnaInversa(self.right, fila, arr4)
        self.front[fila] = arr1
        if fila == 0:
            self.down = np.rot90(self.down, 1)
        # extremo drcho
        elif fila == len(self.back) - 1:
            self.up = np.rot90(self.up, 1)
        # centros
        else:
            pass
        self.updateEstado()

    def getColumna(self, cara, fila):
        column = []
        for x in range(0, len(cara)):
            column.append(cara[x][fila])
        return np.array(column, np.uint8)

    def setColumna(self, cara, fila, columna):
        for x in range(0, len(cara)):
            cara[x][fila] = columna[x]

    def setColumnaInversa(self, cara, fila, columna):
        for x in range(0, len(cara)):
            cara[(len(cara)-1)-x][fila] = columna[x]

    def __str__(self):
        tam = len(self.back)
        #stringCubo = '\nCubo de {0}x{0}x{0}'
        #stringCubo = stringCubo.format(tam) + '\n      [BACK]\n[LEFT][DOWN][RIGHT][UP]\n      [FRONT]\n\n'
        # Como la representacion sera vertical y maximo hay 3
        # caras, pues el tamaño del cubo por el numero de caras
        espacios = '  ' * tam + ' '
        cubo_str = ''
        for i in range(0, tam):
            cubo_str += (espacios + str(self.back[i]) + '\n')
        for i in range(0, tam):
            cubo_str += (str(self.left[i]) + str(self.down[i]) +
                         str(self.right[i]) + str(self.up[i]) + '\n')
        for i in range(0, tam):
            cubo_str += (espacios + str(self.front[i]) + '\n')
        stringCubo = str(cubo_str)
        return stringCubo

    def getCuboSize(self):
        return len(self.back)

    def getCuboMatrix(self):
        matriz = []
        matriz.append(self.back)
        matriz.append(self.down)
        matriz.append(self.front)
        matriz.append(self.left)
        matriz.append(self.right)
        matriz.append(self.up)
        return matriz

    def cuboToStr(self):
        string = ''
        for face in self.getCuboMatrix():
            for i in range(0, self.getCuboSize()):
                for j in range(0, self.getCuboSize()):
                    string += str(face[i][j])
        return string

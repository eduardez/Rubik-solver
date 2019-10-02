#!/usr/bin/python3
# -*- coding: utf-8 -*-
import utils, copy
import numpy as np

class Cubo():
      """Objeto cubo a partir de un objeto JSON (add doc)"""
      def __init__(self, json_data):
            self.back = np.array(json_data['BACK'], np.uint8)
            self.left = np.array(json_data['LEFT'], np.uint8)
            self.down = np.array(json_data['DOWN'], np.uint8)
            self.right = np.array(json_data['RIGHT'], np.uint8)
            self.up = np.array(json_data['UP'], np.uint8)
            self.front = np.array(json_data['FRONT'], np.uint8)
            self.estado = None


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
            #extremo izq
            
            if fila == 0:
                  self.back = np.rot90(self.back, 3)

            elif fila == len(self.back) -1 :   
                  self.front = np.rot90(self.front, 3)
            #centros
            else: 
                  pass
      
      def desplazamientob(self, fila):
            #'''Moveremos la cara del cubo 90º, generando un cubo nuevo tras la modificación'''
            #extremo izq

            arr1 = copy.copy(self.left[fila])
            arr2 = copy.copy(self.down[fila])
            arr3 = copy.copy(self.right[fila])
            arr4 = copy.copy(self.up[fila])
                  
            self.left[fila] = arr2
            self.down[fila] = arr3
            self.right[fila] = arr4
            self.up[fila] = arr1
                  
            if fila == 0: 
                  self.back = np.rot90(self.back,1)

            elif fila == len(self.back) - 1 :
                  self.front = np.rot90(self.front, 1)

            #centros
            else: 
                  pass
      
      def desplazamientoL(self, fila):
            #Moveremos la cara del cubo -90º, generando un cubo nuevo tras la modificación'''
            arr1 = self.getColumna(self.up, fila)
            arr2 = self.getColumna(self.front,fila)
            arr3 = self.getColumna(self.down,fila)
            arr4 = self.getColumna(self.back,fila)
            #Hay que cambiar las filas por columnas
            self.setColumna(self.up,fila,arr4)
            self.front[fila] = arr1
            self.down[fila] = arr2
            self.back[fila] = arr3
            if fila==0:
                  self.back = np.rot90(self.back,3)
            #extremo drcho
            elif fila == len(self.back) -1: 
                  self.front = np.rot90(self.front,3)
            else:
                  pass

      def desplazamientol(self, fila):
            arr1 = copy.copy(self.up[fila])
            arr2 = copy.copy(self.front[fila])
            arr3 = copy.copy(self.down[fila])
            arr4 = copy.copy (self.back[fila])
            #Hay que cambiar las filas por columnas
            self.up[fila] = arr2
            self.front[fila] = arr3
            self.down[fila] = arr4
            self.back[fila] = arr1

            if fila == 0:
                  self.left = np.rot90(self.left,1)
            elif fila == len(self.back) -1:
                  self.right = np.rot90(self.right,1)
            else:
                  pass

      def desplazamientoD(self, fila):
                  #Moveremos la cara del cubo -90º, generando un cubo nuevo tras la modificación'''
            arr1 = copy.copy(self.left[fila])
            arr2 = copy.copy(self.back[fila])
            arr3 = copy.copy(self.right[fila])
            arr4 = copy.copy (self.front[fila])
            self.left[fila] = arr4
            self.back[fila] = arr1
            self.right[fila] = arr2
            self.front[fila] = arr3
            if fila==0:
                  self.down = np.rot90(self.down,3)
            #extremo drcho
            elif fila == len(self.back) -1:
                  self.up = np.rot90(self.up,3)

            #centros
            else:
                  pass

      def desplazamientod(self, fila):
            #Moveremos la cara del cubo -90º, generando un cubo nuevo tras la modificación'''
            arr1 = copy.copy(self.left[fila])
            arr2 = copy.copy(self.back[fila])
            arr3 = copy.copy(self.right[fila])
            arr4 = copy.copy (self.front[fila])
            self.left[fila] = arr2
            self.back[fila] = arr3
            self.right[fila] = arr4
            self.front[fila] = arr1
            if fila==0:
                  self.down = np.rot90(self.down,1)

            #extremo drcho
            elif fila == len(self.back) -1:
                  self.up = np.rot90(self.up,1)
                  
            #centros
            else:
                  pass
      
      def getColumna(self, cara, fila):
            column = []
            for x in range(0, len(cara)):
                  column.append(cara[x][fila])
            return column
            
      def setColumna(self, cara, fila, columna):
            for x in range(0, len(cara)):
                  cara[x][fila] = columna[x]
      
      def __str__(self):
            tam = len(self.back)
            caras = '\nCubo de {0}x{0}x{0}'
            caras = caras.format(tam) + '\n      [BACK]\n[LEFT][DOWN][RIGHT][UP]\n      [FRONT]\n\n'
            #Como la representacion sera vertical y maximo hay 3 
            #caras, pues el tamaño del cubo por el numero de caras
            espacios = '   ' * tam
            #foo = self.json_data
            cubo_str = ''
            for i in range(0, tam):
                  cubo_str += (espacios + str(self.back[i]) + '\n')
            for i in range(0, tam):
                   cubo_str += (str(self.left[i]) + str(self.down[i]) + str(self.right[i]) + str(self.up[i]) + '\n')
            for i in range(0, tam):
                   cubo_str += (espacios + str(self.front[i]) + '\n')
            return caras + str(cubo_str)
        
      def getCuboSize(self):
            return len(self.back)



        
# #Posición-Número
# '''
# Back = 3
# Left = 4
# Down = 1
# Right = 5
# Up = 0
# Front = 2
# '''

# #Codificación de cubo 3x3
# '''
#       [BACK]
# [LEFT][DOWN][RIGHT][UP]
#       [FRON]

#             [[3, 3, 3],
#              [3, 3, 3],
#              [3, 3, 3]]
# [[4, 4, 4], [[1, 1, 1], [[5, 5, 5], [[0, 0, 0],
#  [4, 4, 4],  [1, 1, 1],  [5, 5, 5],  [0, 0, 0],
#  [4, 4, 4]]  [1, 1, 1]]  [5, 5, 5]]  [0, 0, 0]]
#             [[2, 2, 2],    
#              [2, 2, 2],
#              [2, 2, 2]
# '''

# #Método Generar Identificador
# '''Tras generarse un cubo se le ha de asignar el identificador correspondiente'''

# #Método Importar Cubo JSON
# '''Realizaremos la lectura de un archivo JSON y se creará el cubo inicial'''

# #Método Mostrar Cubo
# '''Tomaremos un cubo existente y lo mostraemos por pantalla'''

# #Método Mover L
# '''Moveremos la cara del cubo 90º, generando un cubo nuevo tras la modificación'''

# '''    
#             [[1, 3, 3],
#              [1, 3, 3],
#              [1, 3, 3]]
# [[4, 4, 4], [[2, 1, 1], [[5, 5, 5], [[0, 0, 0],
#  [4, 4, 4],  [2, 1, 1],  [5, 5, 5],  [0, 0, 0],
#  [4, 4, 4]]  [2, 1, 1]]  [5, 5, 5]]  [0, 0, 0]]
#             [[3, 2, 2],    
#              [3, 2, 2],
#              [3, 2, 2]
# Hay que tener en cuenta que la rotación si es en L0 o en LN donde N es la ultima fila haría que se rotase la matriz 
# '''
  
# #Método Mover d
# '''Moveremos la cara del cubo -90º, generando un cubo nuevo tras la modificación'''


# #Método Mover b
# '''Moveremos la cara del cubo -90º, generando un cubo nuevo tras la modificación'''

#Método Girar 90º
def girarHorario(cara):
      return np.rot90(cara, 1)
      
#Método Girar 270º ó -90º
def girarAntiHorario(cara):
      return np.rot90(cara, 3)
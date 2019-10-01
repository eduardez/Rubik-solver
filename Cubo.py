#!/usr/bin/python3
# -*- coding: utf-8 -*-
import utils

class Cubo():
      """Objeto cubo a partir de un objeto JSON (add doc)"""
      def __init__(self, json_data):
            self.json_data = json_data
            self.back = np.array(json_data['BACK'], np.uint8)
            self.left = np.array(json_data['LEFT'], np.uint8)
            self.down = np.array(json_data['DOWN'], np.uint8)
            self.right = np.array(json_data['RIGHT'], np.uint8)
            self.up = np.array(json_data['UP'], np.uint8)
            self.front = np.array(json_data['FRONT'], np.uint8)
            self.estado = None
            
      
      # def girar(self, tipoGiro):
      #       giros = {
      #             1: "giro",
      #             2: "giro",
      #             3: "giro"
      #             }
      #       print(giros.get(tipoGiro, ""))
                 
            

      def __repr__(self):
            return utils.getJSONConFormato(self.json_data)
      
      def __str__(self):
            tam = len(self.json_data['BACK'])
            caras = '\nCubo de {0}x{0}x{0}'
            caras = caras.format(tam) + '\n      [BACK]\n[LEFT][DOWN][RIGHT][UP]\n      [FRONT]\n\n'
            #Como la representacion sera vertical y maximo hay 3 
            #caras, pues el tamaño del cubo por el numero de caras
            espacios = '   ' * tam
            foo = self.json_data
            cubo_str = ''
            for i in range(0, tam):
                  cubo_str += (espacios + str(foo['BACK'][i]) + '\n')
            for i in range(0, tam):
                   cubo_str += (str(foo['LEFT'][i]) + str(foo['DOWN'][i]) + str(foo['RIGHT'][i]) + str(foo['UP'][i]) + '\n')
            for i in range(0, tam):
                   cubo_str += (espacios + str(foo['FRONT'][i]) + '\n')
            return caras + str(cubo_str)
        
      def getCuboSize(self):
            return len(self.json_data['BACK'])
        
#Posición-Número
'''
Back = 3
Left = 4
Down = 1
Right = 5
Up = 0
Front = 2
'''

#Codificación de cubo 3x3
'''
      [BACK]
[LEFT][DOWN][RIGHT][UP]
      [FRON]

            [[3, 3, 3],
             [3, 3, 3],
             [3, 3, 3]]
[[4, 4, 4], [[1, 1, 1], [[5, 5, 5], [[0, 0, 0],
 [4, 4, 4],  [1, 1, 1],  [5, 5, 5],  [0, 0, 0],
 [4, 4, 4]]  [1, 1, 1]]  [5, 5, 5]]  [0, 0, 0]]
            [[2, 2, 2],    
             [2, 2, 2],
             [2, 2, 2]
'''

#Método Generar Identificador
'''Tras generarse un cubo se le ha de asignar el identificador correspondiente'''

#Método Importar Cubo JSON
'''Realizaremos la lectura de un archivo JSON y se creará el cubo inicial'''

#Método Mostrar Cubo
'''Tomaremos un cubo existente y lo mostraemos por pantalla'''

#Método Mover L
'''Moveremos la cara del cubo 90º, generando un cubo nuevo tras la modificación'''
      def rotateL(cubo, columna):
            if columna == cube
            return cubo
'''    
            [[1, 3, 3],
             [1, 3, 3],
             [1, 3, 3]]
[[4, 4, 4], [[2, 1, 1], [[5, 5, 5], [[0, 0, 0],
 [4, 4, 4],  [2, 1, 1],  [5, 5, 5],  [0, 0, 0],
 [4, 4, 4]]  [2, 1, 1]]  [5, 5, 5]]  [0, 0, 0]]
            [[3, 2, 2],    
             [3, 2, 2],
             [3, 2, 2]
Hay que tener en cuenta que la rotación si es en L0 o en LN donde N es la ultima fila haría que se rotase la matriz 
'''

#Método Mover l
'''Moveremos la cara del cubo -90º, generando un cubo nuevo tras la modificación'''

#Método Mover D
'''Moveremos la cara del cubo 90º, generando un cubo nuevo tras la modificación'''

#Método Mover d
'''Moveremos la cara del cubo -90º, generando un cubo nuevo tras la modificación'''

#Método Mover B
'''Moveremos la cara del cubo 90º, generando un cubo nuevo tras la modificación'''

#Método Mover b
'''Moveremos la cara del cubo -90º, generando un cubo nuevo tras la modificación'''

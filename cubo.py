class Cubo():
    cara = None
    def __init__(self, cara):
        self.cara
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

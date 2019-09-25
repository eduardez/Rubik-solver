'''Intalaremos con pip install numpy la librería para poder rotar las matrices'''
import numpy as np
matriz = np.array([[3, 2, 2],[3, 2, 2],[3, 2, 2]], int)
print(matriz)
matriz = np.rot90(matriz, 1)
print(matriz)
matriz = np.rot90(matriz, 3)
print(matriz)
'''He realizado la siguiente comprobación para ver si se podian realizar operaciones de manera "normal"
porque tienen un aspecto distinto a como se muestran las matrices en python pero funciona correctamente
además de que esta librería nos proporciona la opción de girar las matrices también parece que usa una
estructura que tiene apariencia de ser más pequeña, porque las matrices de python puedes meterle lo que 
quieras y en esta cuando la creas tienes que decir que tipo de estructura vas a meter'''
print(matriz * [[3, 2, 2],[3, 2, 2],[3, 2, 2]])
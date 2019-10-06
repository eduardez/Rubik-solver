#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''Intalaremos con pip install numpy la librería para poder rotar las matrices'''
import numpy as np
matriz = np.array([[1, 2, 4],[3, 0, 0],[5, 0, 0]], int)
print(matriz)
print(matriz[2])
print("matriz[0:2]: \n"+str(matriz[0:2]))
print("matriz[:,0] : \n"+str(matriz[:,0]))
print("matriz[:] : \n"+str(matriz[:]))
matriz2 = np.array([1,2,3])
print(matriz2)
print(matriz2.reverse())
#print(matriz)
#matriz = np.rot90(matriz, 3)
#print(matriz)
# '''He realizado la siguiente comprobación para ver si se podian realizar operaciones de manera "normal"
# porque tienen un aspecto distinto a como se muestran las matrices en python pero funciona correctamente
# además de que esta librería nos proporciona la opción de girar las matrices también parece que usa una
# estructura que tiene apariencia de ser más pequeña, porque las matrices de python puedes meterle lo que 
# quieras y en esta cuando la creas tienes que decir que tipo de estructura vas a meter'''
# print(matriz * [[3, 2, 2],[3, 2, 2],[3, 2, 2]])
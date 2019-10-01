#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Testeo del uso de matrices sin tipo determinado
import numpy as np

class CuboMatriz:
    def __init__(self):
        self.back = [[3, 3, 3],[3, 3, 3],[3, 3, 3]]
        self.left = [[4, 4, 4],[4, 4, 4],[4, 4, 4]]
        self.down = [[1, 1, 1],[1, 1, 1],[1, 1, 1]]
        self.right = [[5, 5, 5],[5, 5, 5],[5, 5, 5]]
        self.up = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
        self.front = [[2, 2, 2],[2, 2, 2],[2, 2, 2]]

class CuboNumPy:
    def __init__(self):
        self.back = np.array([[3, 3, 3],[3, 3, 3],[3, 3, 3]], np.uint8)
        self.left = np.array([[4, 4, 4],[4, 4, 4],[4, 4, 4]], np.uint8)
        self.down = np.array([[1, 1, 1],[1, 1, 1],[1, 1, 1]], np.uint8)
        self.right = np.array([[5, 5, 5],[5, 5, 5],[5, 5, 5]], np.uint8)
        self.up = np.array([[0, 0, 0],[0, 0, 0],[0, 0, 0]], np.uint8)
        self.front = np.array([[2, 2, 2],[2, 2, 2],[2, 2, 2]], np.uint8)

if __name__ == "__main__":
    vector = []
    i = 0
    while i < 10000000:
        vector.append(CuboNumPy.__init__)
        if i == 50000:
            print("Hello World")
        i= i +1

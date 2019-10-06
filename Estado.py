#!/usr/bin/python3
# -*- coding: utf-8 -*-
import hashlib

class Estado():
    def __init__(self, cubo, idH):
        self.cubo = cubo #Estado actual del azulejo
        self.idHash = idH #Id del cubo (Hash)
        
    def generarId(self):
        h = hashlib.md5()
        h.update(self.cubo.encode())
        
        self.cubo
    
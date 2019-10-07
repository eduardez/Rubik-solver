#!/usr/bin/python3
# -*- coding: utf-8 -*-
import hashlib

class Estado():
    def __init__(self, cubo):
        self.cubo = cubo #Estado actual del azulejo
        self.idHash = self.generarId() #Id del cubo (Hash)
        
    def generarId(self):
        h = hashlib.md5(self.cubo.cuboToStr().encode('utf-8'))
        return h.hexdigest()


    
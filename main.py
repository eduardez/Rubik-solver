#!/usr/bin/python3
# -*- coding: utf-8 -*-

import utils, copy
import GUI.VIEW_rubiks as Gui
from Cubo import Cubo as Objeto_Cubo

def main():
    utils.jsonFolderCreate()
    json_file = utils.jsonRead('cube.json')
    
    orig_cubo = Objeto_Cubo(json_file)
    new_cubo = copy.deepcopy(orig_cubo)
    print(str(orig_cubo))
    
    new_cubo.desplazamientoB(2) #Esta bien
    print('Desp B\n' + str(new_cubo))
    new_cubo.desplazamientob(2) #esta bien
    print('Desp b\n' + str(new_cubo))
    new_cubo.desplazamientoL(2) #esta bien
    print('Desp L\n' + str(new_cubo))
    new_cubo.desplazamientol(2) #esta bien
    print('Desp l\n' + str(new_cubo))
    new_cubo.desplazamientoD(2)
    print('Desp D\n' + str(new_cubo))
    new_cubo.desplazamientod(2)
    print('Desp d\n' + str(new_cubo))
   # print(str(foo_cubo))
        
    utils.jsonWrite('prueba',json_file)
    
    #Gui.start()    
    pass

if __name__ == "__main__":
    print('''
--------------------------------          
    Rubik Resolver v.0.0.1.
--------------------------------    
    ''')
    main()
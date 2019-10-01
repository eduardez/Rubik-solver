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
    new_cubo.desplazamientoB(2)
    
    print(str(orig_cubo))
    print(str(new_cubo))

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
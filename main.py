#!/usr/bin/python3
# -*- coding: utf-8 -*-

import utils 
from cubo import Cubo as Objeto_Cubo

def main():
    utils.jsonFolderCreate()
    json_file = utils.jsonRead('cube.json')
    
    foo_cubo = Objeto_Cubo(json_file)
    print(repr(foo_cubo))
    
    print(str(foo_cubo))
        
    utils.jsonWrite('prueba',json_file)

if __name__ == "__main__":
    print('''
--------------------------------          
    Rubik Resolver v.0.0.1.
--------------------------------    
    ''')
    main()
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import utils, copy, cmd
import FormarCubo.construirImagen as GenerarImagen
import GUI.VIEW_rubiks as Gui
from Cubo import Cubo as Objeto_Cubo



cubo_actual = Objeto_Cubo(utils.jsonRead('cuboSolucionado.json'))
generar_imagenes = True

    
class CubeShell(cmd.Cmd):
    intro = 'Shell del cubo de Rubik. ? o Help para ayuda\n'
    prompt = '(Cubo)> '
    
    def do_ver_cubo(self, arg):
        '''Imprimir el objeto cubo actual'''
        print(str(cubo_actual))

    
    def do_mezclar(self, arg):
        '''Mezclar el objeto cubo actual'''
        moverCubo(cubo_actual, 'B', 1)
        moverCubo(cubo_actual, 'l', 2)
        
        
    def do_probar_giros(self,arg):        
        new_cubo = copy.deepcopy(cubo_actual) 
        new_cubo.desplazamientob(2) #Está todo bien
        new_cubo.updateEstado()
        print(str(new_cubo))
    
    
    def do_borrar_res(self, arg):   
        '''Vaciar las carpetas de recursos (./res)'''    
        utils.emptyFolder(utils.PATHS.get('image_folder'))
        utils.emptyFolder(utils.PATHS.get('json_folder'))
        
    
    def do_generar_imagenes(self, arg):
        '''Generar imagenes de cada accion hecha con el cubo 
        Syntax: (Cubo)> generar_imagenes <true/false>
        '''
        # print('Valor actual: ' + str(generar_imagenes) + '\n')
        try:
            opt = eval(arg)
            if isinstance(opt, bool):
                generar_imagenes = opt
        except NameError:
            print('Error en los argumentos.')
        pass
        
        
    def do_iniciar_gui(self, arg):
        '''Iniciar entorno grafico (En construccion)'''
        Gui.start()    


def moverCubo(cubo, movimiento, fila):
    if movimiento == 'B' : cubo.desplazamientoB(fila)
    if movimiento == 'b' : cubo.desplazamientob(fila)
    if movimiento == 'L' : cubo.desplazamientoL(fila)
    if movimiento == 'l' : cubo.desplazamientol(fila)
    if movimiento == 'D' : cubo.desplazamientoD(fila)
    if movimiento == 'd' : cubo.desplazamientod(fila)
    cubo.updateEstado()
    if generar_imagenes:
        GenerarImagen.createImage(cubo)
    

def initResources():
    utils.createFolder(utils.PATHS.get('image_folder'))
    utils.createFolder(utils.PATHS.get('json_folder'))
    cubo_actual.updateEstado()

if __name__ == "__main__":
    print('''
--------------------------------          
    Rubik Resolver v.0.0.1.
--------------------------------    
    ''')
    initResources()
    CubeShell().cmdloop()

    
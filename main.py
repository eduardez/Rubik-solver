#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Dominio.utils as utils, copy, cmd, sys
import Dominio.construirImagen as GenerarImagen
import Presentacion.VIEW_rubiks as Gui
from Dominio.Cubo import Cubo as Objeto_Cubo



cubo_actual = Objeto_Cubo(utils.jsonRead('res/json_files/cuboSolucionado.json'))
generar_imagenes = False
    
class CubeShell(cmd.Cmd):
    intro = 'Shell del cubo de Rubik. ? o Help para ayuda\n'
    prompt = '(Cubo)> '
    
    def do_ver_cubo(self, arg):
        '''Imprimir el objeto cubo actual'''
        print(str(cubo_actual))
    
    def do_mezclar_prueba(self, arg):
        '''Prueba del cubo 10x10 con los movimientos que nos proporcionan en el JSON'''
        cubo_actual = Objeto_Cubo(utils.jsonRead('res/json_files/cubo10x10.json'))
        moverCubo(cubo_actual, 'l', 3)
        print(str(cubo_actual) + '\nl3')
        moverCubo(cubo_actual, 'D', 1)
        print(str(cubo_actual)+ '\nD1')
        moverCubo(cubo_actual, 'l', 1)
        print(str(cubo_actual)+ '\nl1')
        moverCubo(cubo_actual, 'd', 0)
        print(str(cubo_actual)+ '\nd0')
        moverCubo(cubo_actual, 'B', 0)
        print(str(cubo_actual)+'\nB0')
        moverCubo(cubo_actual, 'b', 5)
        print(str(cubo_actual)+'\nb5')
        moverCubo(cubo_actual, 'l', 2)
        print(str(cubo_actual)+'\nl2')
        moverCubo(cubo_actual, 'd', 1)
        print(str(cubo_actual)+'\nd1')

    
    def do_mezclar(self, arg):
        '''Mezclar el objeto cubo actual'''
        moverCubo(cubo_actual, 'l', 1)


        
       # moverCubo(cubo_actual, 'b', 2)
        
        
    def do_probar_giros(self,arg):        
        new_cubo = copy.deepcopy(cubo_actual) 
        new_cubo.desplazamientob(2) #Está todo bien
        new_cubo.updateEstado()
        print(str(new_cubo))
    
    
    def do_borrar_res(self, arg):   
        '''Vaciar las carpetas de recursos (./res)'''    
        utils.emptyFolder(utils.PATHS.get('image_folder'))
        #utils.emptyFolder(utils.PATHS.get('json_folder'))
        
    
    def do_generar_imagenes(self, arg):
        '''[EN DESARROLLO]\nGenerar imagenes de cada accion hecha con el cubo 
        Syntax: (Cubo)> generar_imagenes <true/false>
        '''
        # print('Valor actual: ' + str(generar_imagenes) + '\n')
        # try:
        #     opt = eval(arg)
        #     if isinstance(opt, bool):
        #         generar_imagenes = opt
        # except NameError:
        #     print('Error en los argumentos.')
        pass
        
    def do_test(self,arg):
        
        hacerTest(cubo_actual, 0)
        
        
    def do_iniciar_gui(self, arg):
        '''Iniciar entorno grafico (En construccion)'''
        Gui.start()    
        
    def do_muerete(self, arg):
        print('Adieoooooooooooooooooooooooooooooooooos........')
        sys.exit(0)


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
    

def hacerTest(cubo, numId):
    new_cubo = copy.deepcopy(cubo)
    numId += 1
    print(str(numId) + '\n')
    moverCubo(new_cubo, 'L', 0)
    hacerTest(new_cubo, numId)
    
    
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

    
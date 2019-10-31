#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Dominio.utils as utils, cmd, sys, Dominio.Problema as problema
import Presentacion.VIEW_rubiks as Gui
from Dominio.Cubo import Cubo as Objeto_Cubo


cubo_actual = Objeto_Cubo(utils.jsonRead('res/json_files/cuboSolucionado.json'))
    
class CubeShell(cmd.Cmd):
    intro = 'Shell del cubo de Rubik. ? o Help para ayuda\n'
    prompt = '(Cubo)> '
    
    def do_ver_cubo(self, arg):
        '''Imprimir el objeto cubo actual'''
        print(str(cubo_actual))
    
    def do_prueba_rendimiento(self, args):
        '''Pruebas de rendimiento con diferentes estructuras de datos.
        Estructuras: Cola, List (python), Array (numpy)'''
        arr_nodos = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
        seguir = 1
        for num_nodos in arr_nodos:
            if num_nodos > 1000000:
                 seguir = int(input('Quieres seguir con ' + str(num_nodos) + ' nodos? (0 = no | 1 = si)'))
            if seguir:
                print('\n---------------------------------\n' + str(num_nodos) + ' nodos.')
                utils.pruebaRendimiento(num_nodos,cubo_actual)
            else:
                break
    
    def do_problema(self, arg):
        prob = problema()
    
    def do_mezclar_prueba(self, arg):
        '''Prueba del cubo 10x10 con los movimientos que nos proporcionan en el JSON'''
        cubo_actual = Objeto_Cubo(utils.jsonRead('res/json_files/cubo10x10.json'))
        utils.moverCubo(cubo_actual, 'l', 3)
        print(str(cubo_actual) + '\nl3')
        utils.moverCubo(cubo_actual, 'D', 1)
        print(str(cubo_actual)+ '\nD1')
        utils.moverCubo(cubo_actual, 'l', 1)
        print(str(cubo_actual)+ '\nl1')
        utils.moverCubo(cubo_actual, 'd', 0)
        print(str(cubo_actual)+ '\nd0')
        utils.moverCubo(cubo_actual, 'B', 0)
        print(str(cubo_actual)+'\nB0')
        utils.moverCubo(cubo_actual, 'b', 5)
        print(str(cubo_actual)+'\nb5')
        utils.moverCubo(cubo_actual, 'l', 2)
        print(str(cubo_actual)+'\nl2')
        utils.moverCubo(cubo_actual, 'd', 1)
        print(str(cubo_actual)+'\nd1')
    
    
    def do_mezclar(self, arg):
        '''Mezclar el objeto cubo actual'''
        utils.mezclar_aleatorio(1, cubo_actual)

    
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
        utils.hacerTest(cubo_actual)
        
    def do_iniciar_gui(self, arg):
        '''Iniciar entorno grafico (En construccion)'''
        Gui.start()    
        
    def do_exit(self, arg):
        print('Adioooooooooooooooooooooooooooooooooos........')
        sys.exit(0)


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

    
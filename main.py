#!/usr/bin/python3
# -*- coding: utf-8 -*-
import Dominio.utils as utils, cmd, sys
import Presentacion.VIEW_rubiks as Gui
from Dominio.Cubo import Cubo as Objeto_Cubo
from Dominio.Problema import Problema

cubo_actual = Objeto_Cubo(utils.jsonRead('res/json_files/problema2.json'))
problema = None


class CubeShell(cmd.Cmd):
    intro = 'Shell del cubo de Rubik. ? o Help para ayuda\n'
    prompt = '(Cubo)> '

    def do_resolver(self, args):
        '''Menu guiado donde se resolvera el cubo por medio de los metodos vistos en clase.'''
        global cubo_actual
        problema = Problema(cubo_actual)
        # cubo_resuelto = utils.resolverCubo(problema)
        # if cubo_resuelto is not None:
        #     cubo_actual = cubo_resuelto
        utils.resolverCubo(problema)
    
    def do_resolver_all(self, args):
        '''Probar todos los algoritmos de busqueda implementados hasta ahora, sin 
        imprimir la solucion como tal pero si el tiempo'''
        problema = Problema(cubo_actual)
        utils.resolverAll(problema)
    
    def do_ver_cubo(self, arg):
        '''Imprimir el objeto cubo actual'''
        print(str(cubo_actual))

    def do_mezclar_prueba(self, arg):
        '''Prueba del cubo 10x10 con los movimientos que nos proporcionan en el JSON'''
        cubo_actual = Objeto_Cubo(utils.jsonRead('res/json_files/cubo10x10.json'))
        cubo_actual.updateEstado()
        movimientos = [('l',3),('D',1),('l',1),('d',0),('b',0),('B',0),('b',0),('l',2),('d',1)]
        utils.mezclarCuboTupla(movimientos, cubo_actual)

    def do_resolver_profesores(self, arg):
        cubo_actual = Objeto_Cubo(utils.jsonRead('res/json_files/problema.json'))
        cubo_actual.updateEstado()
        movimientos = [('b',0),('D',0),('d',1),('B',0),('B',0)]
        utils.mezclarCuboTupla(movimientos, cubo_actual)

    def do_mezclar(self, arg):
        '''Mezclar el objeto cubo actual'''
        utils.mezclar_aleatorio(1, cubo_actual)

    def do_borrar_res(self, arg):   
        '''Vaciar las carpetas de recursos (./res)'''    
        utils.emptyFolder(utils.PATHS.get('image_folder'))
        # utils.emptyFolder(utils.PATHS.get('json_folder'))

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
       
    def do_iniciar_gui(self, arg):
        '''Iniciar entorno grafico (En construccion)'''
        Gui.start()    

    def do_exit(self, arg):
        print('Adioooooooooooooooooooooooooooooooooos........')
        sys.exit(0)


def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))


def initResources():
    utils.createFolder(utils.PATHS.get('image_folder'))
    utils.createFolder(utils.PATHS.get('json_folder'))
    cubo_actual.updateEstado()


if __name__ == "__main__":
    print('''
--------------------------------          
    Rubik Resolver v.0.39.7.
--------------------------------    
    ''')
    initResources()
    CubeShell().cmdloop()

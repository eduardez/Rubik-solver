#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cmd
import sys

import Dominio.utils as utils
import Presentacion.VIEW_rubiks as Gui
from Dominio.construirImagen import createImage
from Dominio.Cubo import Cubo as Objeto_Cubo
from Dominio.Problema import Problema

# Ruta del archivo JSON que contenga el cubo a resolver
ruta_json = 'res/json_files/ejemplo6x6.json'
cubo_actual = Objeto_Cubo(utils.jsonRead(ruta_json))
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
        '''Ejecuta todos los algoritmos de busqueda implementados hasta ahora, sin 
        imprimir la solucion como tal pero si el tiempo'''
        problema = Problema(cubo_actual)
        utils.resolverAll(problema)

    def do_ver_cubo(self, arg):
        '''Imprimir el objeto cubo actual por consola'''
        print(str(cubo_actual))

    def do_mover_especifico(self, args):
        '''Realiza el movimiento que le indiques al cubo actual'''
        mov = str(input('Tipo de movimiento: '))
        fila = None
        cubo_actual = Objeto_Cubo(utils.jsonRead(ruta_json))

        try:
            if not isinstance(mov, str):
                raise ArithmeticError
            fila = int(input('Fila/columna en la que hacerlo: '))
            if not isinstance(fila, int):
                raise ArithmeticError
        except ArithmeticError:
            print('Datatype missmatch')
        utils.moverCubo(cubo_actual, mov, fila)

    def do_mezclar_todos(self, args):
        '''Realiza todos los movimientos posibles dado un cubo NxN'''
        movimientos = ['B', 'b', 'D', 'd', 'L', 'l', ]
        cubo_actual = Objeto_Cubo(utils.jsonRead(ruta_json))
        for tipo in movimientos:
            for x in range(0, cubo_actual.getCuboSize()):
                cubo_actual = Objeto_Cubo(utils.jsonRead(ruta_json))
                movim = (tipo, x)
                utils.mezclarCuboTupla(movim, cubo_actual)

    def do_mezclar(self, arg):
        '''Mezclar el objeto cubo actual de forma aleatoria'''
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
        '''Método para salir del programa'''
        print('El programa ha finalizado')
        sys.exit(0)


def initResources():
    '''Inicializar las carpetas de imagenes y JSONs,
    actualizar estado actual del cubo'''
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

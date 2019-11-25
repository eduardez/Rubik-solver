#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os, json, datetime, random, threading, copy, time, Dominio.busquedas as busquedas
from Dominio.NodoArbol import NodoArbol
from Dominio.construirImagen import createImage
from Dominio.Frontera import Frontera
from Dominio.Problema import Problema
from Dominio.EspacioEstados import EspacioEstados
from pprint import pprint

PATHS = {
    'json_folder' : './res/json_files/',
    'image_folder' : './res/img_cubes/'
}

generar_imagenes = False


# --------------- Utils cubos -----------------

def mezclar_aleatorio(num_movimientos, cubo):
    tipoMov = ['B','b','L','l','D','d']
    for x in range(0, num_movimientos):
        cara = random.choice(tipoMov)
        fila = random.randrange(cubo.getCuboSize())
        #print('\nMovimiento: ' + str(cara) + str(fila))
        moverCubo(cubo, cara, fila)


def moverCubo(cubo, movimiento, fila):
    if movimiento == 'B' : cubo.desplazamientoB(fila)
    if movimiento == 'b' : cubo.desplazamientob(fila)
    if movimiento == 'L' : cubo.desplazamientoL(fila)
    if movimiento == 'l' : cubo.desplazamientol(fila)
    if movimiento == 'D' : cubo.desplazamientoD(fila)
    if movimiento == 'd' : cubo.desplazamientod(fila)
    cubo.updateEstado()
    if generar_imagenes:
        createImage(cubo)
    
    
def mezclarCuboTupla(movimientos, cubo):
    """Mezclar el cubo con movimientos definidos en un array de tuplas."""
    for mov in movimientos:
        moverCubo(cubo, mov[0], mov[1])
        print(str(mov) + "\n" + str(cubo) + '\n')
        

def resolverCubo(problema):
    '''Menu de eleccion de tipo de busquedas.'''
    listaSolucion = []
    optEstrategias = dict({1:"profundidad", 2:"anchura", 3:"costo", 4:"Aestrella", 5:"voraz"})
    opt = int(input("¿Cómo quieres resolver el cubo:\n 1.Profundidad\n 2.Anchura\n 3.Costo\n 4.A*\n 5.Voraz\n0.Cancelar\n"))
    estrategia = optEstrategias.get(opt)
    if estrategia is not None:
        print("¿Máxima profundidad?")
        profMax = int(input())
        if 1 <= opt <= 5: # Si opt esta entre 1 y 3 la busqueda sera no informada
            t_inicial = time.time()
            listaSolucion = busquedas.busquedaAcotada(problema, estrategia, profMax, opti=True)
            print(f'Tiempo transcurrido: {time.time() - t_inicial}')
        if listaSolucion == None:
            print("El algoritmo de busqueda no ha llegado a una solución posible")
            return None
        else:
            busquedas.mostrarSolucion(listaSolucion)
            return listaSolucion[len(listaSolucion)-1].cubo
    else:
        print('Opcion no encontrada')
        
def resolverAll(problema):
    optEstrategias =["profundidad", "anchura", "costo", "Aestrella", "voraz"]
    optimizacion = True
    try:
        profMax = int(input('Profundidad maxima: '))
        opt = int(input('¿Activar optimizacion?(def = Si/0= no)'))
        if opt == 0:
            optimizacion = False
    except Exception:
        print('MAL INTRODUCIDO')
        return 0

    for estrategia in optEstrategias:
        print('\n-----------------------------------------------\nEjecutando busqueda en ' + estrategia)
        t_inicial = time.time()
        listaSolucion = busquedas.busquedaAcotada(problema, estrategia, profMax, opti=optimizacion)
        print(f'Tiempo transcurrido: {time.time() - t_inicial}')
        if listaSolucion == None:
            print("El algoritmo de busqueda no ha llegado a una solución posible")
        else:
            busquedas.mostrarSolucionCorta(listaSolucion)


            
# --------------- Utils generales ------------------
def getTimestampedName(name):
    td = datetime.datetime.now().strftime("[%H-%M-%S.%f")[:-2]
    td += ']'
    return td + name 


def createFolder(name):
    """Crea una carpeta (si no existe) para contener
    todos los archivos JSON generados.

    Argumentos:
        Nothing
    Returns:
        Nothing   
    """
    try:
        os.makedirs(name)
    except FileExistsError:
        pass


def emptyFolder(name):
    for arch in os.listdir(name):
        ruta = os.path.join(name, arch)
        try:
            if os.path.isfile(ruta):
                os.unlink(ruta)
            #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)


# --------------- Utils de los archivos JSON ------------------
def jsonRead(path):
    """Abre un archivo JSON y devuelve los datos del archivo.

    Argumentos:
        path (str): Ruta relativa hacia el archivo.
    Returns:
        data (Any): Datos contenidos en el JSON.   
    """
    with open(path) as json_file:
        try:
            data = json.load(json_file)
            #pprint(data)
            return data
        except FileNotFoundError:
            print('\nArchivo JSON no encontrado.')

    
def jsonWrite(name, json_data):
    """Escribe un archivo JSON en la carpeta json_files.

    Argumentos:
        name (str): Nombre del archivo,
        json_data (Any): Datos del archivo JSON.
    Returns:
        Nothing.   
    """
    with open(PATHS.get('json_folder') + getTimestampedName(name) + '.json', 'w') as salida:
        salida.write(getJSONConFormato(json_data))


def getJSONConFormato(json):
    """Prettify para JSON. Da un formato bonito para
    luego escribirlo en los ficheros JSON escritos
    por el programa.

    Argumentos:
        json (str): Datos del archivo JSON.
    Returns:
        formatted_json (str): Datos formateados del archivo JSON.   
    """
    formatted_json= '{'
    for caras in json:
        formatted_json += '\n"' + caras +'":['
        for stick in json[caras]:
            formatted_json += str(stick) + ','
        formatted_json = formatted_json[:-1]
        formatted_json += '],'
    formatted_json = formatted_json[:-1]
    formatted_json += '\n}'
    return(formatted_json)
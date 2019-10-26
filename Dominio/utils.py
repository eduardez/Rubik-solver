#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os, json, datetime, random, threading, copy
import Dominio.nodoArbol as Nodo
from Dominio.construirImagen import createImage
from pprint import pprint

PATHS = {
    'json_folder' : './res/json_files/',
    'image_folder' : './res/img_cubes/'
}

generar_imagenes = False


# --------------- Utils cubos ------------------
def generarCubo(tam):
    pass


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
    
# --------------- Utils petar memoria ------------

def hacerTest(cubo):
    import psutil, time
    arbolada = []
    # maxThreads = 50
    # for x in range(0, maxThreads):
    #     thread_petar = threading.Thread(target=petar, args=(arbolada, cubo)).start()
    thread_petar = threading.Thread(target=petar, args=(arbolada, cubo)).start()
    
    #mem = psutil.memory_info().rss
    while 1:    
        print(f'''------------------------------
    Numero de nodos: {len(arbolada)} 
    + Memoria Virtual > {'null'}
    + CPU >  Carga: {'s'}, Frec: {psutil.cpu_freq()}, Uso: {psutil.cpu_percent()}
            ''')
        time.sleep(2.0)
        
def petar(arbolada, cubo):
    while 1:
        new_cubo = copy.deepcopy(cubo)  
        nodo = Nodo.nodoArbol(new_cubo)
        #print(str(len(arbolada)) + '\n')
        mezclar_aleatorio(1, new_cubo)
        arbolada.append(new_cubo)
        for x in range(0, cubo.getCuboSize()):
            moverCubo(cubo, 'B', x)
            moverCubo(cubo, 'b', x)
            moverCubo(cubo, 'D', x)
            moverCubo(cubo, 'd', x)
            moverCubo(cubo, 'L', x)
            moverCubo(cubo, 'l', x)
        


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



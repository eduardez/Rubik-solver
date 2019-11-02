#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os, json, datetime, random, threading, copy, time
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
# --------------- Busquedas Incremental ------------------
def busquedaIncremental(Problema, estrategia, profMax, profInc):
    profActual = profInc
    solucion = []
    while solucion == []  and profActual<=profMax:
        solucion = busquedaAcotada(Problema,estrategia,profActual, profMax)
        profActual = profActual + profInc
    return solucion 

def busquedaAcotada(Problema, estrategia, profActual, profMax):
    listaNodos = []
    frontera = Frontera()
    frontera.insertarNodo(NodoArbol(None, Problema.estadoInicial,0,0,0))
    solucion = False
    '''Si no hay solución y la frontera está vacía se detiene
    si hay solución y la frontera sigue llena se para la ejecución'''
    while solucion == False and frontera.isNotEmpty:
        NodoArbolActual = frontera.delete
        print(NodoArbolActual)

        if Problema.esObjetivo(NodoArbolActual):
            solucion = True
        else:
            listaSucesores = EspacioEstados.sucesores(NodoArbolActual.cubo)
            listaNodos = NodoArbol.crearListaNodosArbol(listaSucesores,NodoArbolActual,profMax,estrategia)
            frontera.insertarLista(listaNodos)
        if solucion == True:
            return crearSolucion(NodoArbolActual)
        
def crearListaNodosArbol(listaSucesores,NodoArbolActual,profMax,estrategia):
    listaNodosArbol = []
    for sucesor in listaSucesores:
        nuevoNodoArbol = NodoArbol(NodoArbolActual, sucesor[1], NodoArbolActual.profundidad + 1, NodoArbolActual.coste + sucesor[2], 0)
        if estrategia == "anchura":
            nuevoNodoArbol.f = nuevoNodoArbol.profundidad
        elif estrategia == "profundidad" or estrategia == "profundidad_iterativa":
            nuevoNodoArbol.f = 1/nuevoNodoArbol.profundidad
        elif estrategia == "costo":
            nuevoNodoArbol.f = nuevoNodoArbol.coste

        if estrategia == "profundidad" and nuevoNodoArbol.profundidad >= profMax:
            pass
        else:    
            listaNodosArbol.append(nuevoNodoArbol)

    return listaNodosArbol

def crearSolucion(NodoArbolActual):
    listaSolucion = []
    # Lo pongo así porque existe la posibilidad de que el nodo padre sea el primero y único
    listaSolucion.insert(0, NodoArbolActual)
    while NodoArbolActual.nodoPadre == None:
        NodoArbolActual = NodoArbolActual.nodoPadre
        listaSolucion.insert(0, NodoArbolActual)
    return listaSolucion

def mostrarSolucion(listaSolcion):
    for i in listaSolcion:
        print(i.accion)


# --------------- Utils cubos -----------------
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

# def hacerTest(cubo):
#     import psutil, time
#     arbolada = []
#     # maxThreads = 50
#     # for x in range(0, maxThreads):
#     #     thread_petar = threading.Thread(target=petar, args=(arbolada, cubo)).start()
#     thread_petar = threading.Thread(target=petar, args=(arbolada, cubo)).start()
#     #mem = psutil.memory_info().rss
#     while 1:    
#         print(f'''------------------------------
#         Numero de nodos: {len(arbolada)} 
#         + Memoria Virtual > {'null'}
#         + CPU >  Carga: {'s'}, Frec: {psutil.cpu_freq()}, Uso: {psutil.cpu_percent()}
#         ''')
#         time.sleep(2.0)
        
def petar(arbolada, cubo):
    while 1:
        new_cubo = copy.deepcopy(cubo)  
        nodo = NodoArbol.nodoArbol(new_cubo)
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
   
def pruebaRendimiento(num_nodos, cubo):
    tiempos = []
    t_ini = time.time()
    pila = []
    for x in range(num_nodos):
        new_cubo = copy.deepcopy(cubo)  
        mezclar_aleatorio(random.randint(0,cubo.getCuboSize()), new_cubo)
        pila.append(new_cubo)
    t_total = time.time() - t_ini
    tiempos.append(('Pila',t_total))
    #--------------------------- 
    t_ini = time.time()
    lista = []
    for x in range(num_nodos):
        new_cubo = copy.deepcopy(cubo)  
        mezclar_aleatorio(random.randint(0,cubo.getCuboSize()), new_cubo)
        lista.insert(x, new_cubo)
    t_total = time.time() - t_ini
    tiempos.append(('Lista',t_total))
    #--------------------------- 
    t_ini = time.time()
    import numpy as np
    numpyarray = np.asarray([])
    if not num_nodos >= 1000000:
        for x in range(num_nodos):
            new_cubo = copy.deepcopy(cubo)  
            mezclar_aleatorio(random.randint(0,cubo.getCuboSize()), new_cubo)
            numpyarray = np.append(numpyarray, new_cubo)
        t_total = time.time() - t_ini
    else:
         t_total = 999999.0
    tiempos.append(('NumPy Array',t_total))
    printTestResult(tiempos, num_nodos)
    printBest(tiempos)


def printTestResult(tiempos, num_nodos):
    for estructura in tiempos:
        print(f'     +Tipo de estructura: {estructura[0]}, tiempo de insercion: {estructura[1]}s') 


def printBest(tiempos):
    mejor = 999999999999
    indice = 12
    for index in range(0, len(tiempos) -1):
        if tiempos[index][1] < mejor:
            mejor = tiempos[index][1]
            indice = index
    print('\nMejor resultado: ' + tiempos[indice][0] + ', %.5fs' % (tiempos[indice][1]))

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




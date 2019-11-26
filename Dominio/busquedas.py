#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Dominio.NodoArbol import NodoArbol
from Dominio.Frontera import Frontera
from Dominio.Problema import Problema
from Dominio.EspacioEstados import EspacioEstados
import time, datetime


def busquedaAcotada(problema, estrategia, profMax, opti):
    listaNodos = []
    frontera = Frontera()
    # Crear nodo padre e insertarlo en la frontera
    nodo_padre = NodoArbol(None, problema.estadoInicial, 0, 0, 0, 0)
    nodo_padre.accion = 'Cubo Inicial'
    if estrategia == "Aestrella":
        nodo_padre.calcularHeuristica()
        nodo_padre.f = nodo_padre.coste + nodo_padre.heuristica
    elif estrategia == "voraz":
        nodo_padre.calcularHeuristica()
        nodo_padre.f = nodo_padre.heuristica
        
    frontera.insertarNodo(nodo_padre)
    esp_estados = EspacioEstados()
    num_nodos = 1
    #t_inicial = time.time()

    '''Si no hay solución y la frontera está vacía se detiene
    si hay solución y la frontera sigue llena se para la ejecución'''
    while not frontera.isEmpty():
        NodoArbolActual = frontera.pop()
        if not frontera.isVisitado(NodoArbolActual):
            if problema.esObjetivo(NodoArbolActual):
                return crearSolucion(NodoArbolActual)
            else:
                listaSucesores = esp_estados.sucesores(NodoArbolActual)
                listaNodos = crearListaNodosArbol(listaSucesores,NodoArbolActual,profMax,estrategia)
                frontera.insertarLista(listaNodos, optimizacion=opti)
                frontera.visitados.update({NodoArbolActual.cubo.idHash:NodoArbolActual.f})
                num_nodos += len(listaSucesores)
                #rendimientoPrint(len(frontera),num_nodos, t_inicial, 5)
        
def crearListaNodosArbol(listaSucesores,NodoArbolActual,profMax,estrategia):
    listaNodosArbol = []
    for sucesor in listaSucesores:
        nuevoNodoArbol = NodoArbol(NodoArbolActual, sucesor[1], NodoArbolActual.profundidad + 1, NodoArbolActual.coste + sucesor[2], 0, 0)
        nuevoNodoArbol.accion = sucesor[0]
        if estrategia == "anchura":
            nuevoNodoArbol.f = nuevoNodoArbol.profundidad
        elif estrategia == "profundidad":
            nuevoNodoArbol.f = -(nuevoNodoArbol.profundidad)
        elif estrategia == "costo":
            nuevoNodoArbol.f = nuevoNodoArbol.coste
        elif estrategia == "Aestrella":
            nuevoNodoArbol.calcularHeuristica()
            nuevoNodoArbol.f = nuevoNodoArbol.coste + nuevoNodoArbol.heuristica
        elif estrategia == "voraz":
            nuevoNodoArbol.calcularHeuristica()
            nuevoNodoArbol.f = nuevoNodoArbol.heuristica



        if not nuevoNodoArbol.profundidad > profMax: 
            listaNodosArbol.append(nuevoNodoArbol)
    return listaNodosArbol


def crearSolucion(NodoArbolActual):
    listaSolucion = []
    # Lo pongo así porque existe la posibilidad de que el nodo padre sea el primero y único
    listaSolucion.append(NodoArbolActual)
    while NodoArbolActual.nodoPadre is not None:
        NodoArbolActual = NodoArbolActual.nodoPadre
        listaSolucion.insert(0,NodoArbolActual)
    return listaSolucion


def mostrarSolucion(listaSolucion, tipo=0):
    """Muestra la solucion a un problema 
    dada una lista de nodos que forman el 
    camino solucion.

    Argumentos:
        listaSolucion: camino solucion
        tipo: Tipo de representacion 0->str, 1->repr
    Returns:
        Nothing   
    """
    for i in listaSolucion:
        if tipo==0:
            print(str(i))
        else:
            print(repr(i))
        
        
# ----------------- METODOS QUE NO BUSCAN ---------------------
def rendimientoPrint(long_frontera, num_nodos, tiempo_inicial, periodo):
    cadena = f'''------------------
Longitud frontera: {long_frontera}
Numero de nodos creados: {num_nodos}
Tiempo transcurrido: {time.time() - tiempo_inicial}
          '''
    datatiempo = datetime.datetime.now()
    second = int(datatiempo.strftime("%S"))
    mili = int(datatiempo.strftime("%f")[:-3])
    if (second % periodo == 0) and (0 < mili < 50):
        print(cadena)
        
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
import time

from Dominio.EspacioEstados import EspacioEstados
from Dominio.Frontera import Frontera
from Dominio.NodoArbol import NodoArbol
from Dominio.Problema import Problema


def busquedaAcotada(problema, estrategia, prof_max, opti):
    '''
    Metodo principal de busqueda de solucion. General para todos los tipos
    de busqueda ya que solo se modifica el valor de F de cada noto dependiendo
    del tipo de busqueda.

    Argumentos:
        problema: instancia de la clase donde se comprueba si un nodo es objetivo
        estrategia: tipo de busqueda realizada
        prof_max: profundidad limite para explorar el arbol
        opti: poda del arbol de nodos
    Returns:
        crearSolucion(): lista con los nodos que componen el camino solucion   
    '''
    esp_estados = EspacioEstados()
    visitados = dict({})
    frontera = Frontera()
    frontera.insertarNodo(crearNodoPadre(estrategia, problema))
    while(1):
        if (frontera.isEmpty()):
            return None
        nodo_actual = frontera.pop()
        if (problema.esObjetivo(nodo_actual)):
            print(f'Numero total de nodos: {str(frontera.num_total)}')

            return crearSolucion(nodo_actual)
        if (nodo_actual.cubo.idHash in visitados) and opti:
            if(abs(visitados[nodo_actual.cubo.idHash]) > abs(nodo_actual.f)):
                visitados.update({nodo_actual.cubo.idHash: nodo_actual.f})
                listaSucesores = esp_estados.sucesores(nodo_actual)
                listaNodos = crearListaNodosArbol(
                    listaSucesores, nodo_actual, prof_max, estrategia)
                frontera.insertarLista(listaNodos)
        else:
            visitados.update({nodo_actual.cubo.idHash: nodo_actual.f})
            listaSucesores = esp_estados.sucesores(nodo_actual)
            listaNodos = crearListaNodosArbol(
                listaSucesores, nodo_actual, prof_max, estrategia)
            frontera.insertarLista(listaNodos)


def crearNodoPadre(estrategia, problema):
    '''
    Crea un nodo padre en funcion de la estrategia.

    Argumentos:
        problema: instancia de la clase de donde se recupera el estado inicial (nodo padre).
        estrategia: Segun la estrategia, el valor de f sera distinto.
    Returns:
        nodo: objeto NodoArbol con la informacion del nodo padre.  
    '''
    nodo = NodoArbol(None, problema.estadoInicial, 0, 0, 0, 0)
    if estrategia == "Aestrella":
        nodo.calcularHeuristica()
        nodo.f = nodo.coste + nodo.heuristica
    elif estrategia == "voraz":
        nodo.calcularHeuristica()
        nodo.f = nodo.heuristica
    return nodo


def crearListaNodosArbol(lista_sucesores, nodo_actual, prof_max, estrategia):
    '''Crea una lista objetos NodoArbol los cuales
    son los sucesores del nodo introducido.
    Antes de crear esta lista, se comprueba que la
    profundidad de los sucesores no sea mayor a la 
    profundidad limite.

    Argumentos:
        lista_sucesores: Lista de ESTADOS sucesores (no son NodosArbol).
        nodo_actual: Nodo padre de los sucesores.
        prof_max: Profundidad limite del arbol.
        estrategia: Segun la estrategia, el valor de f sera distinto.
    Returns:
        lista_nodos_arbol: Lista de objetos NodoArbol
        que contiene los sucesores creados.   
    '''
    lista_nodos_arbol = []
    if not nodo_actual.profundidad >= prof_max:
        for sucesor in lista_sucesores:
            nuevoNodoArbol = NodoArbol(
                nodo_actual, sucesor[1], nodo_actual.profundidad + 1, nodo_actual.coste + sucesor[2], 0, 0)
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
            lista_nodos_arbol.append(nuevoNodoArbol)
    return lista_nodos_arbol


def crearSolucion(nodo_solucion):
    """Crea un array de objetos NodoArbol
    que representa el camino solucion del problema.
    La solucion se crea obteniendo el padre del nodo
    soluion, y su padre, y su padre... asi hasta que el 
    nodo no tenga padre.

    Argumentos:
        nodo_solucion: Nodo solucion del problema
    Returns:
        lista_solucion: Lista de objetos NodoArbol
        que representa el camino solucion.   
    """
    lista_solucion = []
    # Lo pongo así porque existe la posibilidad de que el nodo padre sea el primero y único
    lista_solucion.append(nodo_solucion)
    while nodo_solucion.nodoPadre is not None:
        nodo_solucion = nodo_solucion.nodoPadre
        lista_solucion.insert(0, nodo_solucion)
    return lista_solucion


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
    if not listaSolucion is None:
        for i in listaSolucion:
            if tipo == 0:
                print(str(i))
            else:
                print(repr(i))

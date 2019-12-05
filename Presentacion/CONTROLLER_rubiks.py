#!/usr/bin/python3
# -*- coding: utf-8 -*-
from Dominio.Cubo import Cubo as Objeto_Cubo
from Dominio.Problema import Problema
from Dominio.construirImagen import createImage
import Dominio.utils as utils, cmd, sys, copy
from Dominio.NodoArbol import NodoArbol
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem,QFileDialog


class Controller:
    def __init__(self):
        self.json = None
        self.cubo_actual = None
        # --- GUI ---
        self.debug_area = None
        self.max_column = None
        self.node_table = None
        self.gui_historial_nodos = None
        self.radio_btn_array = None
        self.spinner_fila = None
        # --- Persist ---
        self.nodo_actual = None #nodo visualizado
        self.last_node = None
        self.historial_nodos = []

        
    def printPrueba(self, string):
        print(str(string))
    
    def debugPrint(self, cadena):
        self.debug_area.append('\n' + cadena)
    
    def cambiarCubo(self, json):
        self.clearHistorial()
        self.json = json
        self.cubo_actual = Objeto_Cubo(utils.jsonRead(self.json))
        self.cubo_actual.updateEstado()

        self.debugPrint(f'Creado objeto cubo: \n{str(self.cubo_actual)}')
        self.max_column = self.cubo_actual.getCuboSize() - 1
        nodo = NodoArbol(None, self.cubo_actual ,0,0,0,0)
        self.updateNode(nodo)
        
    def getMovement(self):
        movimiento = None
        for rdio_button in self.radio_btn_array:
            if rdio_button[0].isChecked():
                movimiento = (rdio_button[1], self.spinner_fila.value())
                break
        return movimiento

    def moverCubo(self):
        #copiamos  el cubo actual al historial
        mov = self.getMovement()
        self.debugPrint(f'Realizando movimient {mov}')
        utils.mezclarCuboTupla(mov, self.nodo_actual.cubo)
        self.nodo_actual = NodoArbol(self.nodo_actual, self.nodo_actual.cubo, self.nodo_actual.profundidad + 1, self.nodo_actual.coste + 1, 0, self.nodo_actual.id +1)
        self.nodo_actual.accion = str(mov)
        self.updateHistorial(self.nodo_actual)
        self.updateNodeTable(self.historial_nodos[len(self.historial_nodos)-1])

    def updateNode(self, nodo):
        self.nodo_actual = nodo
        self.updateNodeTable(self.nodo_actual)
        self.updateHistorial(self.nodo_actual)
                
    def updateNodeTable(self, nodo):
        self.node_table.setItem(0,1, QTableWidgetItem(str(nodo.id)))
        self.node_table.setItem(1,1, QTableWidgetItem(str(nodo.accion)))
        self.node_table.setItem(2,1, QTableWidgetItem(str(nodo.cubo.idHash)))
        self.node_table.setItem(3,1, QTableWidgetItem(str(nodo.coste)))
        self.node_table.setItem(4,1, QTableWidgetItem(str(nodo.profundidad)))
        self.node_table.setItem(5,1, QTableWidgetItem(str(nodo.heuristica)))
        self.node_table.setItem(6,1, QTableWidgetItem(str(nodo.f)))

    def updateHistorial(self, nodo):
        new_nodo = copy.deepcopy(nodo)
        self.historial_nodos.append(new_nodo)
        self.gui_historial_nodos.clear()
        labels = []
        for mov in self.historial_nodos:
            labels.append(str(mov.accion))
        str_ultima_accion = labels[len(labels)-1] + ' (último movimiento)'
        labels[len(labels)-1] = str_ultima_accion
        self.gui_historial_nodos.addItems(labels)
    
    def historialClicado(self):
        index = [x.row() for x in self.gui_historial_nodos.selectedIndexes()]
        index = index[0]
        self.updateNodeTable(self.historial_nodos[index])
    
    def clearHistorial(self):
        self.historial_nodos = []
        self.gui_historial_nodos.clear()
    
    def resolver(self):
        pass
#!/usr/bin/python3
# -*- coding: utf-8 -*-
from Dominio.Cubo import Cubo as Objeto_Cubo
from Dominio.Problema import Problema
from Dominio.construirImagen import createImage
from Dominio.busquedas import busquedaAcotada
import Dominio.utils as utils, cmd, sys, copy, PyQt5.QtGui as QtGui, time
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
        self.pic_container = None
        self.paneles_a_manejar = []
        # --- Persist ---
        self.nodo_actual = None #nodo visualizado
        self.last_node = None
        self.historial_nodos = []
        self.lista_solucion = []


    def debugPrint(self, cadena):
        self.debug_area.append(utils.getTimestampedName(' ' + cadena))
    
    def cambiarCubo(self, json):
        self.clearHistorial()
        self.json = json
        self.cubo_actual = Objeto_Cubo(utils.jsonRead(self.json))
        self.cubo_actual.updateEstado()
        self.max_column = self.cubo_actual.getCuboSize() - 1
        nodo = NodoArbol(None, self.cubo_actual ,0,0,0,0)
        nodo.accion = 'Nodo padre'
        self.updateNode(nodo)
        self.updateHistorial(self.nodo_actual)
        self.activarPaneles(True)

        
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
        self.debugPrint(f'Realizando movimiento {mov}')
        utils.mezclarCuboTupla(mov, self.nodo_actual.cubo)
        self.nodo_actual = NodoArbol(self.nodo_actual, self.nodo_actual.cubo, self.nodo_actual.profundidad + 1, self.nodo_actual.coste + 1, 0, self.nodo_actual.id +1)
        self.nodo_actual.accion = str(mov)
        self.updateHistorial(self.nodo_actual)
        self.updateNodeTable(self.historial_nodos[len(self.historial_nodos)-1])
        self.updateCubePic()

    def updateCubePic(self):
        createImage(self.nodo_actual.cubo)
        self.pic_container.setPixmap(QtGui.QPixmap(f'res/img_cubes/{self.nodo_actual.cubo.idHash}.png'))
        self.pic_container.show() # You were missing this.


    def updateNode(self, nodo):
        self.nodo_actual = nodo
        self.updateNodeTable(self.nodo_actual)
        self.updateCubePic()

                
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
        self.updateNode(self.historial_nodos[index])
    
    def clearHistorial(self):
        self.historial_nodos = []
        self.gui_historial_nodos.clear()
    
    def rebootCubo(self):
        self.cambiarCubo(self.json)
        self.debugPrint('Cubo reseteado')
    
    def limpiarImagenes(self):
        utils.emptyFolder(utils.PATHS.get('image_folder'))

        
    def resolver(self, optimizacion, profundidad, estrategia):
        self.debugPrint(f'Realizando busqueda "{estrategia}"(Optimizacion: {str(optimizacion)} | max. prof: {str(profundidad)})')
        self.activarPaneles(False)
        problema = Problema(self.cubo_actual)
        opt_estrategias = dict({"Profundidad": "profundidad", "Anchura": "anchura", 
                               "Costo uniforme": "costo", "A Estrella": "Aestrella", 
                               "Voraz": "voraz"})
        lista_solucion = None
        t_inicial = time.time()
        lista_solucion = busquedaAcotada(problema, opt_estrategias.get(estrategia), profundidad, optimizacion)
        self.debugPrint(f'Tiempo transcurrido: {time.time() - t_inicial}')
        if lista_solucion is None:
            pass
        else:
            self.clearHistorial()
            for nodo in lista_solucion:
                self.nodo_actual = copy.deepcopy(nodo)
                self.updateHistorial(self.nodo_actual)
                self.updateNodeTable(self.historial_nodos[len(self.historial_nodos)-1])
                self.updateCubePic()
                self.activarPaneles(True)
                
    def activarPaneles(self, enabled):
        for pnl in self.paneles_a_manejar:
            pnl.setEnabled(enabled)

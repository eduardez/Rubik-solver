#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import GUI.CONTROLLER_rubiks as Controller, sys


class MainFrame(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def initVisual(self, frm_principal):
        self.initFrame(frm_principal)
        self.initWidgets()
        self.beautifyFrame()
        self.initNames()
        self.initProperties()
        self.retranslateUi(frm_principal)
        self.setActions()
        
    def initFrame(self, frm_principal):
        frm_principal.setObjectName("frm_principal")
        frm_principal.resize(800, 700)
        frm_principal.setTabShape(QtWidgets.QTabWidget.Rounded)
        
        
    def initWidgets(self):
        self.pnl_central = QtWidgets.QWidget(frm_principal)
        self.frm_cubo = QtWidgets.QFrame(self.pnl_central)
        self.lst_movimientos_realizados = QtWidgets.QListView(self.pnl_central)
        #---- botones -----
        self.btn_1 = QtWidgets.QPushButton(self.pnl_central)
        self.btn_2 = QtWidgets.QPushButton(self.pnl_central)
        self.btn_3 = QtWidgets.QPushButton(self.pnl_central)
        self.btn_4 = QtWidgets.QPushButton(self.pnl_central)
        self.debug_area = QtWidgets.QTextBrowser(self.pnl_central)
        self.btn_movimiento_retroceder = QtWidgets.QPushButton(self.pnl_central)
        self.btn_movimiento_avanzar = QtWidgets.QPushButton(self.pnl_central)
        #---- menu bar -----
        self.menubar = QtWidgets.QMenuBar(frm_principal)
        self.menuCargar_cubo = QtWidgets.QMenu(self.menubar)
        self.actionGuardar_Cubo = QtWidgets.QAction(frm_principal)
        self.actionCargar_Cubo = QtWidgets.QAction(frm_principal)
        self.actionPreferencias = QtWidgets.QAction(frm_principal)
        self.statusbar = QtWidgets.QStatusBar(frm_principal)


    def beautifyFrame(self):
        self.frm_cubo.setGeometry(QtCore.QRect(0, 0, 600, 500))
        self.frm_cubo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_cubo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lst_movimientos_realizados.setGeometry(QtCore.QRect(600, 0, 200, 250))
        self.btn_1.setGeometry(QtCore.QRect(50, 530, 131, 41))
        self.btn_2.setGeometry(QtCore.QRect(200, 530, 131, 41))
        self.btn_3.setGeometry(QtCore.QRect(50, 590, 131, 41))
        self.btn_4.setGeometry(QtCore.QRect(200, 590, 131, 41))
        self.debug_area.setGeometry(QtCore.QRect(600, 250, 200, 250))
        self.btn_movimiento_retroceder.setGeometry(QtCore.QRect(610, 530, 88, 34))
        self.btn_movimiento_avanzar.setGeometry(QtCore.QRect(710, 530, 88, 34))
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))

        frm_principal.setCentralWidget(self.pnl_central)
        frm_principal.setMenuBar(self.menubar)
        frm_principal.setStatusBar(self.statusbar)

        self.menuCargar_cubo.addAction(self.actionGuardar_Cubo)
        self.menuCargar_cubo.addAction(self.actionCargar_Cubo)
        self.menuCargar_cubo.addSeparator()
        self.menuCargar_cubo.addAction(self.actionPreferencias)
        self.menubar.addAction(self.menuCargar_cubo.menuAction())
        
        
    def initNames(self):
        self.pnl_central.setObjectName("pnl_central")
        self.frm_cubo.setObjectName("frm_cubo")
        self.lst_movimientos_realizados.setObjectName("lst_movimientos_realizados")
        self.btn_1.setObjectName("btn_1")
        self.btn_2.setObjectName("btn_2")
        self.btn_3.setObjectName("btn_3")
        self.btn_4.setObjectName("btn_4")
        self.debug_area.setObjectName("debug_area")
        self.btn_movimiento_retroceder.setObjectName("btn_movimiento_retroceder")
        self.btn_movimiento_avanzar.setObjectName("btn_movimiento_avanzar")
        self.menubar.setObjectName("menubar")
        self.menuCargar_cubo.setObjectName("menuCargar_cubo")
        self.statusbar.setObjectName("statusbar")
        self.actionGuardar_Cubo.setObjectName("actionGuardar_Cubo")
        self.actionCargar_Cubo.setObjectName("actionCargar_Cubo")
        self.actionPreferencias.setObjectName("actionPreferencias")
        self.retranslateUi(frm_principal)

    def initProperties(self):        
        self.btn_1.setDefault(False)
        self.btn_1.setFlat(False)
        self.btn_3.setDefault(False)
        self.btn_3.setFlat(False)        
        self.btn_2.setDefault(False)
        self.btn_2.setFlat(False)
        self.btn_4.setDefault(False)
        self.btn_4.setFlat(False)
        self.debug_area.setEnabled(True)
        self.debug_area.setReadOnly(True)
        #QtCore.QMetaObject.connectSlotsByName(frm_principal)

    def retranslateUi(self, frm_principal):
        _translate = QtCore.QCoreApplication.translate
        frm_principal.setWindowTitle(_translate("frm_principal", "Rubik\'s Resolver"))
        self.btn_1.setText(_translate("frm_principal", "Boton 1"))
        self.btn_3.setText(_translate("frm_principal", "Boton 3"))
        self.btn_2.setText(_translate("frm_principal", "Boton 2"))
        self.btn_4.setText(_translate("frm_principal", "Boton 4"))
        self.btn_movimiento_retroceder.setText(_translate("frm_principal", "Retroceder"))
        self.btn_movimiento_avanzar.setText(_translate("frm_principal", "Avanzar"))
        self.menuCargar_cubo.setTitle(_translate("frm_principal", "Opciones"))
        self.actionGuardar_Cubo.setText(_translate("frm_principal", "Guardar Cubo"))
        self.actionCargar_Cubo.setText(_translate("frm_principal", "Cargar Cubo"))
        self.actionPreferencias.setText(_translate("frm_principal", "Preferencias..."))
        
    def setActions(self):
       # self.btn_1.clicked.connect(Controller.printPrueba('Hola mundanal ruido'))
        self.btn_1.clicked.connect(lambda: Controller.printPrueba('Sole que te meto con el mechero'))
    
    def printSomething(self):
        print('Something')
        
        
        
        
app = QtWidgets.QApplication(sys.argv)
frm_principal = QtWidgets.QMainWindow()
ui = MainFrame()

def start():
    ui.initVisual(frm_principal)
    frm_principal.show()
    sys.exit(app.exec_())

#!/usr/bin/python3 # -*- coding: utf-8 -*-
import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QMessageBox 
import math

class Example(QMainWindow):
    

    
    def __init__(self):
        super().__init__()
        uic.loadUi("bases.ui",self)
        self.btnCalcular.clicked.connect(self.mostrar)
          
    def mostrar(self):
        self.label_5.setText("el resultado es"+str(self.fiboRange(int(self.txtPrimero.text()),int(self.txtSegundo.text()))))


    #hecho por definicion de 
    def fiboRange(self,numeroInicial,numeroFinal):
        n=1
        anUno=1
        anDos=1
        anTres=0
        lista=[]
        print("1")
        print("1")
        while(n<=numeroFinal):
            anTres=anUno+anDos
            anUno=anDos
            anDos=anTres
            if (n>=numeroInicial):
                lista.append(anTres)
            n=n+1
        return(lista)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
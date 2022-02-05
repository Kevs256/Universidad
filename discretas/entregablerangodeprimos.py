#!/usr/bin/python3 # -*- coding: utf-8 -*-
import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QMessageBox 
import math

class Example(QMainWindow):
    
    divisores=2
    siguiente=0
    resultados =[]
    
    def __init__(self):
        super().__init__()
        uic.loadUi("primos.ui",self)
        self.btnCalcular.clicked.connect(self.mostrar)
    def mostrar(self):
        self.labSalida.setText("el resultado es"+str(self.calcularPrimo(int(self.txtRangodos.text()),int(self.txtRangouno.text()))))
        self.labSalida_2.setText("hay esta cantidad de elementos: "+str(len((self.calcularPrimo(int(self.txtRangodos.text()),int(self.txtRangouno.text()))))))
    def calcularPrimo(self,final,inicial):
        divisores=2
        resultados =[]
        for i in range(0,final-inicial+1):
            numero=inicial+i
            raizcadauno=math.sqrt(numero)
            if (divisores>math.sqrt(numero)):
                primo=1
            while (divisores<=raizcadauno):
                primo=1
                if numero%divisores == 0:
                    primo=0
                    break
                divisores=divisores + 1
            divisores=2
            if (primo == 1 and inicial+i != 1):
                resultados.append(inicial+i)
        return resultados

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

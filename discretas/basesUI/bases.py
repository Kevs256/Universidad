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
        self.label_5.setText("el resultado es"+str(self.resultado(self.txtNumero.text(),self.txtBaseuno.text(),self.txtBasedos.text())))

    def tentoOther(self,numero,baseFinal):
        numero=int(numero)
        baseFinal=int(baseFinal)
        dividendo=numero
        divisor=baseFinal
        residuo=1
        cociente=1
        numeros=[]
        while(dividendo>=divisor):
            residuo=dividendo%divisor
            cociente=dividendo//divisor
            dividendo=cociente
            numeros.append(residuo)
        numeros.append(cociente)
        numeros.reverse()
        return numeros
    
    def othertoTen(self,numero,baseInicial):
        
        digitos=len(str(numero))
        baseInicial=int(baseInicial)
        uno=1
        resultado=0
        for n in str(numero):
            numeroFinal=int(n)*baseInicial**(digitos-uno)
            resultado=resultado+numeroFinal
            uno=uno+1
        return resultado
    
    def revisor(self,numero,baseInicial):
        
        for n in numero:
            if (int(n)>=int(baseInicial)):
                validacion=1
                break
            else:
                validacion=0
        return validacion
    
    def resultado(self,numero,baseInicial,baseFinal):
        
        if (self.revisor(numero,baseInicial)==0):
            if (baseInicial == "10"):
                resultado=self.tentoOther(numero,baseFinal)
                return resultado
            elif (baseInicial != "10"):
                preresultado=self.othertoTen(numero,baseInicial)
                resultado=self.tentoOther(preresultado,baseFinal)
                return resultado
        else:
            resultado="que ha introducido un numero invalido"
            return resultado
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
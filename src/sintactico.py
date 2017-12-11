from lexico import *
from componentes import *
from AST import *

class Sintactico:

    def __init__(self, lexico):
        self.lexico = lexico
        self.componente = self.lexico.siguiente()

    def analizaLinea(self):
        arbol=self.analizaExpresion()
        if self.componente.cat == "nl":
            self.componente = self.lexico.siguiente()
            return arbol
        else:
            print "Error de linea"

    def analizaExpresion(self):
        arbol = self.analizaTermino()
        while self.componente.cat in ['Suma', 'Resta']:
            if self.componente.cat == 'Suma':
                self.componente= self.lexico.siguiente()
                dcho = self.analizaTermino()
                arbol = NodoSuma(arbol, dcho)
            else:
                self.componente= self.lexico.siguiente()
                dcho = self.analizaTermino()
                arbol = NodoResta(arbol, dcho)
        return arbol


    def analizaTermino(self):
        arbol= self.analizaFactor()
        while self.componente.cat in ['Producto', 'Division']:
            if self.componente.cat == 'Producto':
                self.componente= self.lexico.siguiente()
                dcho= self.analizaFactor()
                arbol= NodoProducto(arbol, dcho)
            else:
                self.componente= self.lexico.siguiente()
                dcho= self.analizaFactor()
                arbol = NodoDivision(arbol, dcho)
        return arbol

    def analizaFactor(self):
        if self.componente.cat == 'Entero':
            arbol = NodoEntero(self.componente.valor)
            self.componente = self.lexico.siguiente()
            return arbol
        elif self.componente.cat == 'Apar':
            self.componente = self.lexico.siguiente()
            arbol = self.analizaExpresion()
            if self.componente.cat == 'Cpar':
                self.componente = self.lexico.siguiente()
                return arbol
        else:
            print "Error Factor"


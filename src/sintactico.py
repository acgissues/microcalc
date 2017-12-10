from lexico import *
#from componentes import *
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
            print "Error"

    def analizaExpresion(self):
        arbol= self.analizaTermino()
        while self.componente.cat ==  'Suma':
            self.componente= self.lexico.siguiente()
            dcho= self.analizaTermino()
            arbol= NodoSuma(arbol, dcho)
        return arbol


    def analizaTermino(self):
        arbol= self.analizaFactor()
        while self.componente.cat ==  'Producto':
            self.componente= self.lexico.siguiente()
            dcho= self.analizaFactor()
            arbol= NodoProducto(arbol, dcho)
        return arbol

    def analizaFactor(self):
        if self.componente.cat == 'Entero':
            arbol = NodoEntero(self.componente.valor)
            self.componente = self.lexico.siguiente()
            return arbol
        else:
            print "Error Factor"


from sintactico import Sintactico
from lexico import Lexico
from AST import *
from sys import stdin
from errores import *

if __name__ == '__main__':
    while True:
        linea = stdin.readline()

        if linea == '\n':
            break

        try:
            lexico = Lexico(linea)
            sintactico = Sintactico(lexico)

            expresion = sintactico.analizaLinea()
            print "La expresion es : " + str(expresion) + " = " + str(expresion.evalua())
        except Exception:
            print "Error en ejecucion"

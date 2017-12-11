import argparse
from sintactico import Sintactico
from lexico import Lexico
from AST import *
from sys import stdin
from errores import *

def parseArgs():
    parser = argparse.ArgumentParser(description='Calculadora con funciones basicas, mediante el la estructura de arbol con gramatica limitada.');
    parser.add_argument('-t', '--tokens', action='store_true', help='Muestra los tokens ingresados en cada linea.', required=False);
    parser.add_argument('-e', '--expresiones', action='store_true', help='Muestra como se separan las expresiones de la linea.', required=False);
    return parser.parse_args();

if __name__ == '__main__':
    args = parseArgs()

    if args.tokens == True:
        while True:
            linea = stdin.readline()

            if linea == '\n':
                break

            lexico = Lexico(linea)

            while True:
                try:
                    componente = lexico.siguiente()
                    print componente

                    if componente.cat == 'eof':
                        break
                except Exception:
                    print "Error de ejecucion. (Tokens)"

    elif args.expresiones == True:
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
                print "Error en Ejecucion. (Expresiones)"
    else:
        while True:
            linea = stdin.readline()

            if linea == '\n':
                break

            try:
                lexico = Lexico(linea)
                sintactico = Sintactico(lexico)

                expresion = sintactico.analizaLinea()
                print "Resultado: " + str(expresion.evalua())
            except Exception:
                print "Error de Ejecucion"

<<<<<<< HEAD
=======
import argparse
>>>>>>> master
from sintactico import Sintactico
from lexico import Lexico
from AST import *
from sys import stdin
from errores import *

<<<<<<< HEAD
if __name__ == '__main__':
=======
def main():
    args = parseArgs()

>>>>>>> master
    while True:
        linea = stdin.readline()

        if linea == '\n':
            break

<<<<<<< HEAD
        try:
            lexico = Lexico(linea)
            sintactico = Sintactico(lexico)

            expresion = sintactico.analizaLinea()
            print "La expresion es : " + str(expresion) + " = " + str(expresion.evalua())
        except Exception:
            print "Error en ejecucion"
=======
        if args.tokens:
            print printTokens(linea)
        elif args.expresiones:
            print "Expresion: " + getExpresion(linea)
            print "Resultado = " + str(getResultado(linea))
        else:
            print "Resultado = " + str(getResultado(linea))

# Devuelve el resultado de la expresion
def getResultado(linea):
        try:
            lexico = Lexico(linea)
            sintactico = Sintactico(lexico)
            expresion = sintactico.analizaLinea()

            return expresion.evalua()
        except Exception:
            print "Error de Ejecucion. (Resultado)"

# Devuelva la cadena que muestra la jerarquia de la expresion
def getExpresion(linea):
        try:
            lexico = Lexico(linea)
            sintactico = Sintactico(lexico)
            expresion = sintactico.analizaLinea()

            return str(expresion)
        except Exception:
            print "Error en Ejecucion. (Expresiones)"

# Devuelve los tokens separados por saltos de linea
def printTokens(linea):
    lexico = Lexico(linea)
    tokens = ''

    while True:
        try:
            componente = lexico.siguiente()
            tokens = tokens + '\n' + str(componente)

            if componente.cat == 'eof':
                break
        except Exception:
            print "Error de ejecucion. (Tokens)"

    return tokens

def parseArgs():
    parser = argparse.ArgumentParser(description='Calculadora con funciones basicas, mediante una estructura de arbol con gramatica limitada.');
    parser.add_argument('-t', '--tokens', action='store_true', help='Muestra los tokens ingresados en cada linea.', required=False);
    parser.add_argument('-e', '--expresiones', action='store_true', help='Muestra como se separan las expresiones de la linea.', required=False);
    return parser.parse_args();

if __name__ == '__main__':
    main()
>>>>>>> master

from lexico import *

if __name__ == '__main__':
    lexico= Lexico('2+3*4\n')

    while True:
        componente = lexico.siguiente()
        print componente
        if componente.cat == 'eof':
            break
    print "Fin del programa"

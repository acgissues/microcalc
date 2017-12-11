from componentes import *
from errores import *

class Lexico:   

    def __init__(self,cadena):
        self.cadena = cadena
        self.pos = 0

    def siguiente(self):
        while True:
            if self.pos >= len(self.cadena):
                return Eof()
            elif self.cadena[self.pos] in [' ', '\t']:
                self.pos = self.pos + 1
            elif self.cadena[self.pos] == '(':
                self.pos = self.pos + 1
                return Apar()
            elif self.cadena[self.pos].isdigit(): 
                numero = ''
                while(self.cadena[self.pos].isdigit()):
                    numero = numero + str(self.cadena[self.pos])
                    self.pos = self.pos + 1
                return Entero(int(numero))
            elif self.cadena[self.pos] == ')':
                self.pos = self.pos + 1
                return Cpar()
            elif self.cadena[self.pos] == '+':
                self.pos = self.pos + 1 
                return Suma()
            elif self.cadena[self.pos] == '-':
                self.pos = self.pos + 1 
                return Resta()
            elif self.cadena[self.pos] == '*':
                self.pos = self.pos + 1
                return Producto()
            elif self.cadena[self.pos] == '/':
                self.pos = self.pos + 1
                return Division()
            elif self.cadena[self.pos] == '\n':
                self.pos = self.pos + 1
                return Nl()
            else:
                ErrorLexico()

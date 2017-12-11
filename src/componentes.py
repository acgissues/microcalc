import json

class Suma:

  def __init__(self):
    self.cat = "Suma"

  def __str__(self):
    return self.cat

class Resta:

  def __init__(self):
    self.cat = "Resta"

  def __str__(self):
    return self.cat

class Producto:

  def __init__(self):
    self.cat = "Producto"

  def __str__(self):
    return self.cat

class Division:

  def __init__(self):
    self.cat = "Division"

  def __str__(self):
    return self.cat

class Entero:

  def __init__(self,valor):
    self.cat = "Entero"
    self.valor = valor

  def __str__(self):
    return self.cat + " (valor : " + str(self.valor) + " )"

class Cadena:

  def __init__(self, texto):
    self.cat = "Cadena"
    self.texto = json.dumps(texto)

  def __str__(self):
    return self.cat + " (texto : " + str(self.texto) + " )"

class Apar:

  def __init__(self):
    self.cat = "Apar"

  def __str__(self):
    return self.cat

class Cpar:

  def __init__(self):
    self.cat = "Cpar"

  def __str__(self):
    return self.cat

class Nl:

  def __init__(self):
    self.cat = "nl"
    
  def __str__(self):
    return self.cat


class Eof:

  def __init__(self):
    self.cat = "eof"
  
  def __str__(self):
    return self.cat

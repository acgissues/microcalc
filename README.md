# Microcalc

Proyecto obtenido de la Universitat Jaume I y utilizado en nuestro curso de
Lenguajes Formales. El resultado del mismo, es una calculadora sencilla que
utiliza la estructura de árbol para definir su gramática y resolverla.

Hasta el momento se ejecuta con **Python 2.7**.

## Uso

- `python microcalc.py`: permite insertar 'n' cantidad de líneas con expresiones
  y devuelve el resultado de cada una.

- `python microcalc.py -t`: separa cada una de las expresiones en tokens e
  imprime los mismos en líneas separadas.

- `python microcalc.py -e`: permite visualizar cómo se separa cada una de las
  expresiones, separándolas por paréntesis. Esto ayuda a tener una idea de la
  jerarquía en que se evalúa la expresión.

## To-do

- [ ] Añadir soporte de cadenas
- [ ] Añadir operador de 'barra'

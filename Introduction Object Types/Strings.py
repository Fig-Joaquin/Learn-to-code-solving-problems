# Librería de matemáticas
import math
# Importe de librería de generación de un número aleatorio
import random
# importe de re
import re

# Ayuda... Despliega con métodos disponibles para usar !!
""" print(dir(spam)) # Muestra los métodos que se pueden utilizar con el string. """
# Ayuda... Despliega info lo que hace el método usado
""" print(help(spam.replace)) # Muestra la ayuda del método replace. """

## Inmutabilidad : 
""" Cadenas de textos o strings y las tuplas son inmutables. (No puedens er modificados una vez creado) """

# Contando digitos
print('Número de digitos: ',len(str(4*4)))

# Numero pi
print('Número PI: ',math.pi)

# Numero random
print('Número random: ',random.random())
# Numero random con rango
print('Número random con rango: (1,2,3,4): ', random.choice([1,2,3,4]))

# Strings #

# Ver tamaño de la palabra.
palabra = 'Hola Mundo'
print(len(palabra))

# Verificar una letra de la palabra.
print(palabra[5])

# Verificar una letra de la palabra con valor negativo .
print(palabra[-1]) # Último valor.

# Impresión de letras.
print(palabra[0:4]) # Hola.

# Multiplicación de letras.
print((palabra[5:10])*2)

# Agregar una letra a una palabra.
palabra = 'Bienvenidos al ' + palabra
print(palabra)

# Busqueda de la posición de una palabra.
print(palabra.find('Hola'))

# Reemplazar una palabra por otra
palabra = palabra.replace('Hola','hola')
print(palabra)

# Separar un string y a través de un caracter.
line = 'aaa, bbb, cccc, dd'
print(line.split(',')) # ['aaa', ' bbb', ' cccc', ' dd']    

# .isdigit 
""" Comprueba si el string solo existen números."""
numero = '123'
print(numero.isdigit()) # Si contiene un caracter da false. Si es un número da true.

# .isalpha 
""" Comprueba si un string contiene solamente palabras. """
spam = 'spam'
print(spam.isalpha())

print('%s, eggs, and %s ' % ('spam', 'SPAM!')) # spam, eggs, and SPAM!  Formato 1
print('{0}, eggs, and {1}'.format('spam', 'SPAM!')) # spam, eggs, and SPAM! Formato 2

### Pattern Matching
""" busqueda de palabra que ha de comenzar en Hello y termina en world. Muestra todo lo de al medio """
match = re.match('Hello[ \t]*(.*)world', 'Hello Python 3 world')
print(match.group(1))

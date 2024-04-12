# Librería de matemáticas
import math
# Importe de librería de generación de un número aleatorio
import random


# Contando digitos
print('Número de digitos: ',len(str(4*4)))

# Numero pi
print('Número PI: ',math.pi)

# Numero random
print('Número random: ',random.random())
# Numero random con rango
print('Número random con rango: (1,2,3,4): ', random.choice([1,2,3,4]))

# Strings #

# Ver tamaño de la palabra
palabra = 'Hola Mundo'
print(len(palabra))
# Verificar una letra de la palabra
print(palabra[5])
# Verificar una letra de la palabra con valor negativo 
print(palabra[-1]) # Último valor
# Impresión de letras
print(palabra[0:4]) # Hola
# Multiplicación de letras
print((palabra[5:10])*2)
# Agregar una letra a una palabra
palabra = 'Bienvenidos al ' + palabra
print(palabra)
# Busqueda de la posición de una palabra
print(palabra.find('Hola'))
# Reemplazar una palabra por otra
palabra = palabra.replace('Hola','hola')
print(palabra)
# Listas
""" Son colecciones ordenadas, no tienen un tamaño definido
    # Las listas son mutables a diferencia de los strings
    # Las listas pueden contener cualquier tipo de objeto
    """

lista = [123, '321', 1.23] # Lista con diferentes tipos de datos.
print(lista)  # Cantidad de datos en la lista.

print(lista[1]) # Mostrando la posición 1 de la lista.
print(lista[:-1]) # Mostrando la lista sin el último valor.

print(lista + [4,5,6]) # Agregando valores a la lista. Sin añadirlos a la lista original


"""
Agregando valores a una lista 
"""
# Método append()
lista.append('7') # Agregando valores a la lista (Se agregaran al final)
print(lista)

lista += [7,'8',9] # Agregando valores a la lista (Se agregaran en orden)
print(lista)

"""
Eliminar un valor de la lista
"""

lista.pop(4) # Eliminando el valor de la posición 4. (Valor número 7 quitado de la lista.)
print(lista) 

lista_nueva = ['b', 'a', 'c', 'e', 'd', 'g', 'f']   
# El valor de la lista se ordena alfabéticamente.
lista_nueva.sort() 
print(lista_nueva)

# Orndear la lista en reversa (De atrás hacia adelante).
lista_nueva.reverse()
print(lista_nueva)

""" No se puede agregar un elemento a la lista en una posición mayor a la que está permitida.
    ¡Si la lista tiene 5 espacios solamente se puede añadir un elemento al espacio 6!
"""

# Representación de una matriz

matriz=[[1,2,3],
        [4,5,6],
        [7,8,9]]

""" 
Las vectores y matrizas empiezan desde la posición 0 
En el ejemplo tenemos una matriz de 3x3, lo que en código se representa como 2x2
"""

print('Impresión de la matriz: ',matriz)
print(matriz[1]) # Impresión de la matriz en la posición 2.
print(matriz[1][2]) # Impresión de la matriz en la posición fila 1 columna 2.

col2 = [row[1] for row in matriz] # Recorre la matriz y muestra la fila 2. row[1] = Fila 2
print(col2)
col2 = [row[1] * 2 for row in matriz] # Recorre la matriz y muestra la columna 2 multiplicada por 2.
print(col2)
""" 
Recorre la matriz y muestra el último valor de cada fila.
"""

"""
Diagonal de la matriz
"""
diagonal = [matriz[i][i] for i in [0, 1, 2]] # Recorre la matriz y muestra la diagonal de la matriz.
print(diagonal)

"""
Suma de los valores de la matriz dado a su posición [0][0] [0][1] [0][2] [1][0] [1][1] [1][2] [2][0] [2][1] [2][2
"""
print(list(map(sum, matriz))) # Suma los valores de cada lista en la matriz.

print(matriz[0][0] + matriz[0][1] + matriz[0][2]) # Ejemplo anterior # Lista 1

"""
Creando un set en cada lista
"""
# Calcula la suma de los valores de la matriz dandole un valor a cada lista
print({i:sum(matriz[i]) for i in range(3)} )

# Diccionarios.
"""
Reconocidos mapeos también son colecciones de otros objetos, 
pero almacenan objetos por clave en lugar de por posición relativa. 
De hecho, los mapeos no mantienen ningún orden confiable de izquierda a derecha; 
simplemente asignan claves a valores asociados. 
Los diccionarios, el único tipo de mapeo en el conjunto de objetos principales de Python, 
también son mutables: pueden cambiar en su lugar y pueden crecer y encogerse según demanda, 
al igual que las listas.
"""

# Operacionesm de mapeo.
plato1 = {'nombre':'Hamburguesa','precio':5000}

# Suma de números
suma = (3+5)
print(suma)

# Resta de números
resta = (3-5)
print(resta)

# Multipliación de números
multiplicacion = (3*5)
print(multiplicacion)

# División de números con resultado decimal
division = (8/2)
print(division)

# División de números con resultado entero
division = (8//2)
print(division)

# Potencia de números
potencia = (2**4)
print(potencia)

# Módulo o residuo de una división
modulo = (3%5)
print(modulo)

# Suma y multiplicacion Ejemplo 1
ejemplo1 = 3 + 5 * 2 # 5*2 = 10 | 3+10 = 13
print(ejemplo1)

# Suma y multipliación Ejemplo 2
ejemplo2 = (3+5) * 2 # (3+5) = 8 | 8*2 = 16
print(ejemplo2)

# Calculo de bits utilizados el ejemplo1
print(ejemplo1.bit_length()) # 1111 = 4 bits


# Calculo de bits utilizados el ejemplo2
print(ejemplo2.bit_length()) # 10000 = 5 bits

# Suma de variables
ejemplo_suma = ejemplo1 + ejemplo2
print(ejemplo_suma)

# Resta de variables
ejemplo_resta = ejemplo1 - ejemplo2
print(ejemplo_resta)

# Conversión de String a número
string_number = '27017'
# print(string_number+5) ERROR PORQUE NO SE SUMA NUMBER CON STRING
print(int(string_number)) # Se convierte a número
# print(int(string_number)+5) # Se suma el número

#string_to_number= int(input("Ingrese un numero: "))
#print(string_to_number) # Se convierte a número entero

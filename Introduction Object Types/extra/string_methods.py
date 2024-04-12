# String operator

# Para la concatenación tenemos:
hello = 'Hello '+'There'
print ('1. ', hello)
# Multipliación de String:
underline = '_'*15
print ('2. ', underline)
# String en Mayúsculas en su totalidad:
mayus = hello.upper()
print ('3. ', mayus)

# Recortar un caracter que esté en el inicio y final (Se eliminan ambos) string #
yesterday_original = 'yesterday'
print('Example: ',yesterday_original)
yesterday = 'yesterday'.strip('y')
print ('4. ', yesterday)

# Recortar un espacio:
spacing_original = '            goodbye'
print ('Example: ', spacing_original)
spacing = (spacing_original.strip())
print ('5. ', spacing)

# Contando las letras de un string
count_spacing = spacing_original.count(' ')
print('6. Contando la letra o de la palabra 5 son: ',count_spacing)

# Contando una palabra existente
count_words = 'hello hello hello goodbye'
print('Example',count_words)
print ('7. ', count_words.count('hello'))

# Contando las letras de la palabra completa
print('8. ', count_words.count(''))

# Contando el total de palabras
line = 'Please have a nice day'
total_words = line.count(' ') + 1 # Se agrega un +1 ya que empieza a contar desde 0
print('9. ', total_words)


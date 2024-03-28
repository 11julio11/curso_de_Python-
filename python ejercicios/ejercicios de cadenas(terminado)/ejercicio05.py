'''
Escribir un programa que pida al usuario que introduzca una frase en la 
consola y
 muestre por pantalla la frase invertida
'''

# Solicitar entrada al usuario
# Usamos la función `input()` para obtener la entrada del usuario
frase = input("Escribe una frase: ")

# Convertir la entrada en una lista de palabras
# Dividimos la cadena de entrada en una lista de palabras usando el método `split()`
usuario = frase.split()

# Invertir el orden de la lista de palabras
# Invirtamos el orden de la lista de palabras usando el método `reverse()`
usuario.reverse()

# Unir la lista de palabras en una sola cadena
# Volvamos a unir la lista de palabras en una sola cadena usando el método `join()`
inverted_sentence = ' '.join(usuario)

# Imprimir la cadena invertida
# Imprimimos la cadena invertida usando la función `print()`
print("Frase invertida:", inverted_sentence)
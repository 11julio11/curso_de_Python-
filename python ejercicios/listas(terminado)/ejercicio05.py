'''
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden
 inverso separados por comas.
'''
#creamos la lista de numeros
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#join  es una función built-in que permite concatenar elementos de una lista en una cadena con un carácter especificado
#map  para invertir el orden de la lista 
print("Lista de numeros: ", ",".join(map(str, reversed(lista_numeros))))

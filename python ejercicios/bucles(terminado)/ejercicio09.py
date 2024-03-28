'''
Escribir un programa que pida al usuario una palabra
 y luego muestre por pantalla una a una las letras 
de la palabra introducida empezando por la última.
'''

#solicitamos la palabras
palabra = input("Introduce una palabra: ")

#recorremo la palabras a lo contrario
for i in range(len(palabra)-1, -1 ,-1):
    print(palabra[i])
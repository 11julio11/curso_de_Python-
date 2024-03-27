'''
Escribir un programa que pida al usuario una palabra y
 la muestre por pantalla 10 veces.
'''
 # Solicita al usuario que ingrese una palabra
frase = input("Introduce una frase: ")


 #solicitamos la cantidad de veces que se repite la palabra

cantidad = int(input("intruce la cantidad de veces que se repite la palabra: "))

 #imprimimos por pantalla la palabra introducida

for i in range (cantidad):
    print (frase)


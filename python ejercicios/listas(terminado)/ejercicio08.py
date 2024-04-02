'''
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
'''

#pedimos la palabra al usuario
palabra = input(f"Ingrese una palabra: ") 

#creamos otra varible para las vocales 
vocales = ['a', 'e', 'i','o','u'] 

# calculamos la cantidadde vocales 
cantidad_vocales = {
                  #con el metodo count() contamos cuantas veces aparece cada vocal en la palabra
    vocal: palabra.count(vocal) for vocal in  vocales
}

print(cantidad_vocales)
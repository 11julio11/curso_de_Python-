'''
Escribe una función que tome un diccionario como entrada y devuelva una lista de tuplas donde cada tupla contenga una clave y su valor correspondiente.
'''

def diccionario_a_lista_de_tuplas(diccionario):
    lista_de_tuplas = [(clave, valor) for clave, valor in diccionario.items()]
    return lista_de_tuplas

# Ejemplo de uso:
nombre_Y_edades = {
    "horacio": 10,
    "maria": 5,
    "juan": 7
}

resultado = diccionario_a_lista_de_tuplas(nombre_Y_edades)
print(resultado)

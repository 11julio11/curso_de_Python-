'''
Escribe un programa que muestre la cantidad de elementos que tiene una tupla dada.
'''


def contar_elementos(tupla):
    """
    Función que recibe como parámetro una tupla y devuelve el número de elementos que contiene.
    
    Parámetros:
        - tupla (tuple): La tupla cuya longitud se desea conocer.
        
    Devuelve:
        - int: El número de elementos en la tupla.
    """
    return len(tupla)

# Test del código
mi_tupla = ("Hola ", "¿Cómo estás?", 1, True, None)
print("La tupla 'mi_tupla' tiene {} elemento(s).".format(contar_elementos(mi_tupla)))
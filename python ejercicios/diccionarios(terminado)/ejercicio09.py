'''
 Escribe un programa que tome un diccionario de nombres y edades y lo imprima ordenado alfabéticamente por nombre.
'''

def imprimir_diccionario_ordenado(diccionario):
    for nombre in sorted(diccionario.keys()):
        print(f"{nombre}: {diccionario[nombre]}")

# Diccionario de nombres y edades
nombre_Y_edades = {
    "Ana": 30,
    "Carlos": 25,
    "Elena": 35,
    "David": 28
}

# Llamada a la función para imprimir el diccionario ordenado
imprimir_diccionario_ordenado(nombre_Y_edades)

'''
 Escribe un programa que imprima cada clave y su valor correspondiente en el diccionario en líneas separadas.
'''

nombre_Y_edades = {
    "horacio": 10,
    "maria": 5,
    "juan": 7
} 

# Imprimir cada clave y valor en líneas separadas
for clave, valor in nombre_Y_edades.items():
    print(clave + ":", valor)

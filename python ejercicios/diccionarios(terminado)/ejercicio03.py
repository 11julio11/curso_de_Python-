'''
 Agrega una nueva entrada al diccionario que represente a una persona adicional junto con su edad.
'''

nombre_Y_edades = {
    "pedro": 2,
    "horacio": 10,
    "maria": 5,
} 

# Agregamos la nueva entrada al diccionario anterior
nueva_entrada = ("juan", 7)  # Nombre y edad de juan

nombre_Y_edades[nueva_entrada[0]] = nueva_entrada[1]
print(nombre_Y_edades)

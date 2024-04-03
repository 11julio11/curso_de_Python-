'''
Elimina una entrada del diccionario que ya no necesites.
'''

nombre_Y_edades = {
    "pedro": 2,
    "horacio": 10,
    "maria": 5,
} 

# Agregamos la nueva entrada al diccionario anterior
nueva_entrada = ("juan", 7)  # Nombre y edad de juan

# Eliminamos una entrada del diccionario
clave_a_eliminar = "horacio"
if clave_a_eliminar in nombre_Y_edades:
    del nombre_Y_edades[clave_a_eliminar]

nombre_Y_edades[nueva_entrada[0]] = nueva_entrada[1]
print(nombre_Y_edades)


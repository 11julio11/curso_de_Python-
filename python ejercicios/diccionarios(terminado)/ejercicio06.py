'''
Desarrolla un programa que verifique si una clave específica existe en el diccionario.
'''
nombre_Y_edades = {
    "horacio": 10,
    "maria": 5,
    "juan": 7
}

consultar_clave = input("Escriba la clave a buscar: ")

# Verificar si la clave existe en el diccionario
if consultar_clave in nombre_Y_edades:
    print(f"La clave '{consultar_clave}' existe en el diccionario.")
else:
    print(f"La clave '{consultar_clave}' no existe en el diccionario.")

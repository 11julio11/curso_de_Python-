'''
Escribe una función que tome una tupla como entrada y devuelva una lista con los mismos elementos.
'''

# Función "copiar_tupla"
def copiar_tupla(t):
    # Convertir la tupla a una lista mediante el método list()
    return list(t)

# Probar la función "copiar_tupla"
t1 = (1, 2, 3, 'a', 'b')
print("Tupla original:", t1)
l1 = copiar_tupla(t1)
print("Lista generada por copiar_tupla():", l1)

# Ejemplo simple

def saluda(nombre):
    return f"Hola, {nombre}!"

# Probar la función "saluda"
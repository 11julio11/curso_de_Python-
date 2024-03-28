'''
Escribir un programa que pida al usuario que introduzca una frase en la 
consola y una vocal, y después muestre por 
pantalla la misma frase pero con la vocal introducida en mayúscula.
'''

# Solicitar una frase al usuario
frase = input("Introduce una frase: ")

# Solicitar una vocal al usuario
vocal = input("Introduce una vocal: ").lower()

# Convertir la vocal introducida en mayúscula
vocal_may = vocal.upper()

# Reemplazar la vocal introducida por la vocal en mayúscula
nueva_frase = frase.replace(vocal, vocal_may)

# Mostrar la nueva frase en pantalla
print("Nueva frase:", nueva_frase)
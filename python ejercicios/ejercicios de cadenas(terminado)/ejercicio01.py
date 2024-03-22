'''
Escribir un programa que pregunte el nombre del usuario en la consola
 y un número entero e imprima por pantalla en líneas distintas el nombre del 
 usuario tantas veces como el número introducido.
'''

# Solicita al usuario que ingrese su nombre
nombre = input("Introduce tu nombre: ") 

# Solicita al usuario que ingrese un número primo
n = int(input("ingresa un numero primo: "))

# Imprime el nombre del usuario seguido de un salto de línea (`\n`), repetido `n` veces.
# Como `n` es un número primo, esto significa que el nombre del usuario se imprimirá en la misma línea `n` veces seguido de un salto de línea en cada iteración.
print((nombre + "\n") * int(n))





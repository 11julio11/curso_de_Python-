'''
Escribe un programa que tome una tupla de números desordenados y la imprima en orden ascendente.
'''
def imprimir_tupla(numeros):
    numeros = sorted(numeros)
    for num in numeros:
        print(num, end=" ")
    print()

# Pruebas del código
numeros1 = (5, 2, 8, 3, 7)
imprimir_tupla(numeros1)

numeros2 = (-1, -4, -9, -6, -3)
imprimir_tupla(numeros2)

numeros3 = (0,  0, 0)
imprimir_tupla(numeros3)
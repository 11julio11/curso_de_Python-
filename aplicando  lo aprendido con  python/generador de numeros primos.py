
'''
Pide al usuario que ingrese un límite superior y muestra todos los números primos hasta ese límite.
'''

# Solicitar al usuario que ingrese un límite superior
limite = int(input("ingrese un numero entero como limite superior"))

# Imprimir el título de la salida
print("numeros primos hasta", limite, ":")

# Iterar a través de los números desde 2 hasta el límite de entrada (inclusive)
for num in range (2, limite+1):

    # Suponer que el número es primo, hasta que se demuestre lo contrario
    es_primo = True

    # Verificar si el número es divisible por cualquier número desde 2 hasta su mitad
    for i in range(2, num//2 +1):

        # Si el número es divisible, no es primo; interrumpir el bucle
        if num % i == 0:
            es_primo = False
            break  # break sirve para salir de la estructura iterativa tan pronto como se cumpla la condición

    # Si el número no es divisible por ningún número verificado, es primo; imprimirlo
    if es_primo:
        print(num)
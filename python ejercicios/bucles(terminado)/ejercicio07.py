'''
Escribir un programa que pida al usuario un número entero y 
muestre por pantalla si es un número primo o no.
'''

#pedimos el numero al usuario
numero = int(input("Ingrese un número entero positivo mayor que 1: "))

if numero <= 1:
    es_primo = False
else:
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break

if es_primo:
    print("Sí es primo.")
else:
    print("No es primo.")

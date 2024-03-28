'''
Escribir un programa que pida al usuario un número entero positivo
 y muestre por pantalla la cuenta atrás desde ese número 
 hasta cero separados por comas.
'''

# Solicitar un número entero positivo al usuario
numero = int(input("Introduce un número entero positivo: "))

# Validar que el número sea positivo
if numero < 0:
    print("El número debe ser positivo, por favor introduzca un número entero positivo.")
else:
    # Imprimir la cuenta regresiva en pantalla
    for i in range(numero, -1, -1):
        print(i, end=', ')
    print("¡Listo!")


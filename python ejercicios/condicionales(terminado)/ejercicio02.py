'''
Escribir un programa que pida al usuario un número entero 
y muestre por pantalla si es par o impar.
'''
#pedimos el ingreso del numero
numero=int(input("Ingrese un numero: "))
#comprobamos si el numero es par o impar y lo mostramos por pantalla
if numero%2==0:
    print("el numero ",numero,"es par")
else:
    print("el numero",numero,"es impar")
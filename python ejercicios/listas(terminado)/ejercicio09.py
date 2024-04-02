'''
Desarrolla un programa que pregunte al usuario un número y luego compruebe si está en una lista dada.
'''
#pedimos el numero a usuario
numero = int(input("Dime un numero: "))

#creamos la lista de numeros
numeros = [2,4,6,8,10]

#comprobamos si el numero esta o no esta en la lista
if numero in numeros:
    print("El numero", numero, "está en la lista")
else:
    print("El numero", numero, "no está en la lista")
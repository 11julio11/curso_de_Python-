'''
Escribe un programa que pida al usuario dos números y luego muestre cuál de los dos números es mayor.
'''
#pedimos los  numeros al usuario
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

#comparamos si el primero es mayor o menor
if numero1 > numero2 :
    print("el primer  numero", numero1, "es mayor")
else:
    print("el segindo numero", numero2, "es mayor")
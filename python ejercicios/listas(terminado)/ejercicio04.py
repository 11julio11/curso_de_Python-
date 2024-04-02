'''
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en 
una lista y los muestre por pantalla ordenados de menor a mayor.
'''
# creamos una variable de los numeros ganadores
numeros_ganadores = [ 12, 67, 45, 89 ] # Los numeros ganadores de la lotería primitiva

# Mostramos los numeros ganadores por pantalla
print("Los numeros ganadores de la lotería son:")
# Ordenamos los numeros ganadores de manera ascendente y mostramos por pantalla
# se utiliza sorted para ordenar la  secuencia de una  o más variables (en este caso numeros_ganadores)
for num in sorted(numeros_ganadores):
    print(num)
input("\nPresione Enter para continuar.")
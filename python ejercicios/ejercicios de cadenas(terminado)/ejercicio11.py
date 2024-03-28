'''
Escribir un programa que pregunte el nombre el un producto, su precio y un número de
 unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos 
 enteros y 2 decimales, el número de 
unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
'''


# Solicitar el nombre del producto, el precio y la cantidad de unidades
producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
unidades = int(input("Ingrese la cantidad de unidades: "))

# Calcular el costo total
costo_total = precio * unidades

# Mostrar el resultado por pantalla
#usamos f  para separar los valores y \n es una nueva línea
print(f"Producto: {producto} \nPrecio unitario: {precio} \nUnidades: {unidades} \nCosto total: {costo_total}")

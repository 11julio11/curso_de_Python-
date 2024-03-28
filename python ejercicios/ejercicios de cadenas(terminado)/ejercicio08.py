'''
Escribir un programa que pregunte por consola el precio de un producto
 en euros con dos decimales y muestre 
por pantalla el número de euros y el número de céntimos del precio introducido.
'''
# Solicitar el precio del producto en euros
precio_producto = float(input("Por favor, introduce el precio del producto en euros: "))

# Calcular el número de euros y el número de céntimos
euros = int(precio_producto)
centimos = int((precio_producto - euros) * 100)

# Mostrar el número de euros y el número de céntimos
print(f"El precio del producto es {euros} € con {centimos} céntimos.")
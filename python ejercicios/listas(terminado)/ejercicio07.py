'''
Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8,
 y muestre por pantalla el menor y el mayor de los precios.
'''
#lista de precios 
precios = [50, 75, 46, 22, 80, 65, 8,]

#determinar el menor y el mayor
menor_precio = min(precios)
mayor_precio = max(precios)

#imprimimos por pantalla 
print("El menor precio es: ", menor_precio)
print("El mayor precio es: ", mayor_precio)
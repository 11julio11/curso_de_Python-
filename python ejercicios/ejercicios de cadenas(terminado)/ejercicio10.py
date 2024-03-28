'''
Escribir un programa que pregunte por consola por los productos
 de una cesta de la compra, separados por comas, 
y muestre por pantalla cada uno de los productos en una línea distinta.
'''
#preguntamos por los productos en la  cesta de la compra
productos = input("Ingrese los productos de su cesta de la compra separados por comas: ")

#convertimos el string a una lista para poder manipularla fácilmente
#usamos  split() para dividir el string en substrings basado en las comas (",")
for producto in productos.split(','):
    #usamos  strip() para eliminar posibles espacios al principio y final del substring
    print(producto.strip())

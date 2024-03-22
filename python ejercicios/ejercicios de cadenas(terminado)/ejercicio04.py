'''
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension 
donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número 
de teléfono sin el prefijo y la extensión.
'''

# #extraemos  los datos del fichero telefonos.
# def extraer_numero(numero_completo):
#     '''# Dividir el número completo en prefijo, número y extensión'''
#     partes = numero_completo.split("-")
#     #el metodo splir se utiliza para  dividir un string en varias partes 
#     #La primera parte será el prefijo, la segunda el número y la tercera la extensión.
#     '''se extrae y se guarda en la variable numero'''
#     numero = partes[1]
#     #retornamos solo el número
#     return numero
# #solicitamos  al usuario que introduzca el número completo de teléfono.
# numero_telefono = input("ingrese el numero de telefono en formato +34-numero-extensión: ")
# #llamamos a la función extraer
# numero_sin_prefijo_extension = extraer_numero(numero_telefono)
# #mostramos por pantalla el resultado
# print("el numero de telefono sin prefijo y extension:", numero_sin_prefijo_extension)

def extraer_numero(numero_completo):
    partes = numero_completo.split("-")#el metodo split se utiliza para  dividir un string en varias partes 
    numero = partes[1]
    return numero

# Solicitar al usuario que ingrese el número de teléfono completo
numero_telefono = input("Ingrese el número de teléfono en formato +34-número-extension: ")

# Verificar si el número comienza con el prefijo "+34"
if numero_telefono.startswith("+34-"):#La función startswith() es un método de Python que se utiliza para verificar si una cadena comienza con un cierto prefijo
    # Llamar a la función para extraer el número
    numero_sin_prefijo_extension = extraer_numero(numero_telefono)
    
    # Mostrar el número sin el prefijo y la extensión
    print("El número de teléfono sin prefijo y extensión es:", numero_sin_prefijo_extension)
else:
    print("El número de teléfono no tiene el formato correcto.")

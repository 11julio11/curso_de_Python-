'''
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
 y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
'''

# Preguntamos al usuario la cantidad inicial a invertir
cantidad = float(input("¿Cantidad a invertir? "))

# Preguntamos al usuario el interés porcentual anual
intereses = float(input("¿Interés porcentual anual? "))

# Preguntamos al usuario el número de años que durará la inversión
years = int(input("¿Años?"))

# Calculamos el capital obtenido cada año
for i in range(years):
    # Actualizamos la cantidad con el interés anual
    cantidad *= 1 + intereses / 100 
    # Mostramos el capital obtenido al final de cada año
    # Usamos round para redondear la cantidad a dos decimales
    print("Capital tras " + str(i+1) + " años: " + str(round(cantidad, 2)))


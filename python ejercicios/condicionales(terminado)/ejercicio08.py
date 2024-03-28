'''
Escribe un programa que pida al usuario un número del 1 al 12 que represente
 un mes del año y luego muestre cuántos días tiene ese mes.
'''

# Diccionario que asocia cada mes con su cantidad de días y su nombre
meses_dias_nombres = {
    1: ("Enero", 31),
    2: ("Febrero", 28),  # 29 en año bisiesto
    3: ("Marzo", 31),
    4: ("Abril", 30),
    5: ("Mayo", 31),
    6: ("Junio", 30),
    7: ("Julio", 31),
    8: ("Agosto", 31),
    9: ("Septiembre", 30),
    10: ("Octubre", 31),
    11: ("Noviembre", 30),
    12: ("Diciembre", 31)
}

# Función para determinar si un año es bisiesto
def es_bisiesto(año):
    return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)

# Solicitar al usuario que ingrese un número de mes
numero_mes = int(input("Ingrese un número del 1 al 12 que represente un mes del año: "))

# Verificar si el mes es Febrero y si el año es bisiesto
if numero_mes == 2:
    año = int(input("Ingrese el año para verificar si es bisiesto: "))
    if es_bisiesto(año):
        print(f"El mes {meses_dias_nombres[numero_mes][0]} tiene 29 días.")
    else:
        print(f"El mes {meses_dias_nombres[numero_mes][0]} tiene {meses_dias_nombres[numero_mes][1]} días.")
else:
    # Mostrar la cantidad de días y el nombre del mes
    print(f"El mes {meses_dias_nombres[numero_mes][0]} tiene {meses_dias_nombres[numero_mes][1]} días.")

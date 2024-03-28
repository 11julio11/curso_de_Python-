'''
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y 
muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también
 funcione cuando el día o el mes se introduzcan con un solo carácter
'''

# Pedir al usuario su fecha de nacimiento en el formato `dd/mm/aaaa`
fecha_nacimiento = input("Por favor, introduzca su fecha de nacimiento en el formato `dd/mm/aaaa`: ")

# Extraer el día, el mes y el año de la entrada
dia = int(fecha_nacimiento[:2])
mes = int(fecha_nacimiento[3:5])
anio = int(fecha_nacimiento[6:])

# Mostrar el día, el mes y el año
if dia < 10:
    dia = f"0{dia}"
if mes < 10:
    mes = f"0{mes}"
if anio < 10:
    anio = f"0{anio}" 

print(f"Su fecha de nacimiento es: {dia}/{mes}/{anio}")

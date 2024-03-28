'''
Escribe un programa que pida al usuario un año y determine si es bisiesto o no.
'''

#pedimos  el año a evaluar al usuario
dia = int(input("Ingrese el año: "))

#definir las condiciones para determinar si es bisiesto o no
if (dia % 4 == 0 and dia % 100 != 0) or dia % 400 ==  0:
    print(f"%d es bisiesto" % dia)
else:
    print(f"%d no es bisiesto")
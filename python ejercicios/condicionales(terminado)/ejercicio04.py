'''
Escribe un programa que pida al usuario una calificación (entre 0 y 100)
 y muestre si pasó (calificación mayor o igual a 60) o no.
'''

#preguntamos  por la calificación del usuario
calificacion = int(input("por favor ingrese se nota: "))

#comparamos la calificación con el rango permitido, mostramos mensaje de error si es menor o superior
if calificacion < 0 or calificacion > 100:
    print ("Error! La calificación debe ser entre 0 y 100.")
else: #si la calificación está dentro del rango, comparamos para ver si pasó o no
    if calificacion >= 60:
        print ("¡PASÓ!")
    else:
        print ("No PASÓ.")
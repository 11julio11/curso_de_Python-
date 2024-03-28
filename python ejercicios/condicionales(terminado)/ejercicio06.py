'''
Escribe un programa que pida al usuario dos nombres
y luego muestre cuál de los dos nombres es más largo.
'''
#ingresamos  el primer nombre del usuario
nombre1=input("Ingrese su primer nombre: ")

#ingresamos el segundo nombre del usuario
nombre2=input("Ingrese su segundo nombre: ")

#comparamos la longitud de ambos nombres y guardamos en una variable cual es mas largo
longitud=max(len(nombre1),len(nombre2))#usamos  max para comparar las longitudes de ambas cadenas
# y len  para obtener la longitud de cada cadena

#mostramos por pantalla el nombre mas largo
if  longitud==len(nombre1):
    print ("El nombre más largo es",nombre1)
else:
    print ("El nombre más largo es",nombre2)
'''
vçEscribe un programa que pida al usuario la edad de tres miembros de una familia
 y luego determine quién es el mayor y quién es el menor.
'''

#ponemos tres miembros de la familia  en variables
miembro1 = int(input("Ingrese la edad del primer miembro: "))
miembro2 = int(input("Ingrese la edad del segundo miembro: "))
miembro3 = int(input("ingrese la edad del tercer miembro: "))


#comparamos las edades para saber quienes son los mayores y quienes son los menores
mayor = max(miembro1,miembro2,miembro3) #funcion built-in de python que devuelve el maximo entre dos o mas numeros

mayor = max(miembro1,miembro2,miembro3) #devuelve el valor mas grande entre ellos

menor = min(miembro1,miembro2,miembro3) #devuelve el valor más pequeño entre ellos

#imprimos por pantalla
print ("El mayor de la familia tiene ", mayor , " años")
print ("el menor de la familia tiene ", menor , " años")
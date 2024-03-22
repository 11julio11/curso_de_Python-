'''
Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por 
pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas
 las letras mayúsculas y otra solo con la primera letra del nombre y
 de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
'''


nombre = input("Ingrese su nombre completo: ")

print(nombre.lower()) #muestra el nombre completo pero todo en minusculas
print(nombre.upper()) #muestra el nombre completo pero todo en mayusculas
print(nombre.capitalize()) #muestra el primer caracter de cada palabra en Mayuscula y los demás en Minusculas
print(nombre.title())

#🎉✨🎉logrado
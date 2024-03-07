myStr = "Jesus David"#"Hellp World"

#concadenacion de unificacion 
print("My name is" + myStr)

#otra forma de concadenacion unificacion
print(f"My name is {myStr}")

#print(dir(myStr))
#metodos de los strings

print(myStr.upper()) #convierte el texto en mayuscula 
print(myStr.lower())#convierte el texto en miniscula
print(myStr.swapcase())#convierte las letras entre mayusculas y ninusculas
print(myStr.capitalize()) #convierte las primeras letras de un titulo en mayusculas

                                    #🔽tambien se puede anexar los metodos ya expuestos para cambiar la sintaxis 
print(myStr.replace('Hello', 'bye').upper()) #reemplaza el primer elemento por otro que se esta 
print(myStr.count('l'))# sirve para saber cuantos elementos hay en un codigo 
          #⏩print(myStr.count(''))#tambien se pueden v¿buscar caracteres vacios


           #🔽mostrara  el metodo booleans  (true/false) si caracter esta o no esta en el codigo
print(myStr.startswith('Hello'))#determina si un caracter empieza segun los que se quiera buscar

             #🔽mostrara si el caracter termina segun lo indicado / lo arrojara en booleans
print(myStr.endswith('World'))#buscara el ultimo caracter

print(myStr.split())#divide mi caracter completo en dos 
print(myStr.find(' '))#busca la ubicacion de cada letra del caracter
print(len(myStr))#muestra la longitud de los caracteres

print(myStr.index('l'))#busca el indice cada caracter 

print(myStr.isnumeric())# para saber si el caracter es numerico
print(myStr.isalpha())#para saber si es alphanumerico

print(myStr[9])#simplifica la busquedad del caracter 
print(myStr[-1])#simplificacion inversa
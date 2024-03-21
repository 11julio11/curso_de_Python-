#---------ejemplos de operaciones--------------------#
#print(type(9)) # tipo de  numero entero(integer(int))

#print(type(10.1)) # tipo sw numero decimal (float)
  
     #🔽operador de modulo(devuelve el residuo de la division)
#print(2//3)
      #se puede hacer de dos formas como:
#(2//3){
        #  ambas operaciones dan el mismo resultado     
#(2%2)}

#tablas de precedencia de operadores
#print(20-10/5*3**2)###Primero, evaluemos la potencia: (3^2 = 9).
#Luego, realicemos la división: (\frac{{10}}{{5}} = 2).
#A continuación, multiplicamos: (2 \cdot 9 = 18).
#Por último, restamos: (20 - 18 = 2).
#Por lo tanto, el resultado de la expresión es 2.###

"""
- input("insert your age"): Solicita la edad al usuario y almacena la entrada como una cadena de texto. 
- new_age = int(age) + 5: Convierte la cadena de texto a un número entero y suma 5.
- print(new_age): Muestra el resultado en la consola.
"""
age = input("insert your age")
new_age = int(age) + 5
print(new_age)
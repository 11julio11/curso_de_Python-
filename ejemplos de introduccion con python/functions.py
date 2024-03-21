'''
las funciones sirve  para realizar una tarea especifica, como por ejemplo:
- Calcular el area de un triangulo.
- Calcular la altura de un triangulo isosceles.
- Calcular el volumen de una esfera.

En python las funciones se definen con la palabra reservada "def" seguida del nombre de la función y entre paréntesis los argumentos que reciben un valor
'''

# def hello():
#     print("Hola!")

# hello() # llamada a la función hello()

# def hello(name):
#     print("Hello" + name)

# hello("John") # llamada a la función hello(), con un argumento extra "John"

# def add(numberone, numbertwo):
#     return numberone + numbertwo

# print(add(58, 67))
# print(add(5000, 565))

#la funcion lambda  se utiliza cuando queremos crear una pequeña y simple función anónima. Es similar a las funciones normales pero sin el def

add = lambda numberOne,  numbertwo: numberOne + numbertwo
print(add(1234, 9876))
demo_list = [1, "helo", 1.34, True, [1, 2, 3]]
colors = ['red', 'green', 'blue']

#consultor
numbers_list = list((1, 2, 3, 4))
#print(type(numbers_list))

#range()
"""
range se utiliza para representar una secuencia inmutable de números. Es especialmente útil junto a la sentencia for, 
ya que permite definir bucles que iteran un número determinado de veces.
 Aquí tienes los detalles sobre la clase range y cómo usarla:
Creación de objetos range:
range(fin): Crea una secuencia numérica desde 0 hasta fin - 1.
range(inicio, fin, [paso]): Crea una secuencia numérica desde inicio hasta fin - 1.
 Si se especifica el parámetro paso, la secuencia generará números con ese incremento.
Ejemplos:

list(range(10))          # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(5, 10))       # [5, 6, 7, 8, 9]
list(range(0, 10, 3))    # [0, 3, 6, 9]
list(range(0, -10, -1))  # [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
list(range(5, -5, -2))   # [5, 3, 1, -1, -3]
"""

#r = list(range(1, 100))
#print(r)


    #🔽muestra la informacion
#print(dir(colors))

     # 🔽muestra la longitud de a lista 
#print(len(colors))
  
             #🔽 se utiliza para verificar si un valor está presente en una secuencia, como una cadena, una lista, una tupla o un diccionario
print('green' in colors)

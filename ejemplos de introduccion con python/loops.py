foods = ['manzanas', 'pan', 'queso', 'leche', 'platano', 'uvas' ]

'''
se pueden llamar de esta manera
'''
# print(foods[0])
# print(foods[1])
# print(foods[2])
# print(foods[3])
# print(foods[4])

#con los bucles operadores reducimos el trabajo
# for food in foods:
#     if food == "queso":
#         #print("tienes que comprar esto")
#         #break rompe la validacion cuando llegua a la condicion 
#         continue
#     print(food)

#este metodo se utiliza para generar un listado  o recorrido completo del arreglo sin importar su longitud.
# for number in range(1, 8):
#     print(number)

#muestra la letra una por una del string
# for letter in "Hello":
#     print(letter)

#controlador de flujo
count = 4 

while count <= 10 :
    print(count)
    count = count + 1
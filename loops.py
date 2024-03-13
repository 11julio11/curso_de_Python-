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
for food in foods:
    if food == "queso":
        #print("tienes que comprar esto")
        #break rompe la validacion cuando llegua a la condicion 
        continue
    print(food)
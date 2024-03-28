'''
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y 
muestre por pantalla el número de veces que aparece la letra en la frase.
'''

#preguntamos la frase
usuario_frese = input("por favor, ingrese la  frase: ")

#preguntamos la letra 
letra_buscada = input("ingrese la letra a buscar: ")

#ponemos un contador  para saber cuántas veces sale la letra en la frase

contador = 0
for i in usuario_frese:
    if i == letra_buscada:
        contador += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra_buscada,contador,usuario_frese))
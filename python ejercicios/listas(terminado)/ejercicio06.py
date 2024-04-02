'''
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones
 múltiplos de 3, y muestre por pantalla la lista resultante.
'''
#lista del abecedario
abecedario = [ 'a', 'b', 'c', 'd', 'e','f','g','h','i','j', 'k', 'l', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]

# Se eliminan las letras que ocupen posiciones múltiplos de 3
abecedario = abecedario[::3]

print(abecedario)
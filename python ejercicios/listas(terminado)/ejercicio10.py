'''
Escribe un programa que elimine los elementos duplicados de una lista y muestre la lista resultante.
'''
#el input_list  es la lista original, en donde se buscan eliminar los elementos repetidos
def remove_duplicates(input_list):
    #returm para una nueva lista sin elementos repetidos
    return list(set(input_list))
#creamos una lista  con numeros repetidos
input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]
#remove_duplicates sirve  para eliminar los repetidos en la lista
unica_lista = remove_duplicates(input_list)
print(unica_lista)
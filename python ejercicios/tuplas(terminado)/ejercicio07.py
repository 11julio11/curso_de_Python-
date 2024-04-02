'''
Escribe un programa que cuente cuántas veces aparece un elemento en una tupla.
'''
programa = ('peliculas', 'series', 'juegos', 'musica', 'series')
elemento_buscado = input("Ingrese el elemento a buscar: ")
contador = 0
for i in programa:
    if i == elemento_buscado : 
        contador +=1
if contador == 0:
    print(f"el elemento {elemento_buscado}  no se encuentra en la tupla")
else:
    print(f"El elemento {elemento_buscado} se encuentra {contador} veces en la tupla")
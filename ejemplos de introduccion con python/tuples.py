'''
las tuplas/tuples permiten agrupar valores de diferentes tipos en una sola variable como en las 
listas pero estos valores no se pueden cambiar.
'''

#x = (1, 2, 3)
#print(type(x)) # <class 'tuple'>

#ejempls de tuplas/tuples de meses
#months = ('enero', 'febrero', 'marzo', 'abril')#es un tuple con elementos de tipo string
#print(type(months)) #<class 'tuple'>

#x = (1, 2, 3, 4, 5)

#print(x[0]) #acceder a los elemento por su indice

#del x #eliminar la tupla
'''
cuando se utiliza este metodo  lanza el error TypeError: 'tuple' object por ya la tupla fue borrada
'''

#tambien las tuplas se pueden utilizar en diccionarios
locations = {
    (132.545454, 1.454545): "Casa",
    (32.434334, 23.32323): "Oficina"
}

print(type(locations)) #<class 'dict'>
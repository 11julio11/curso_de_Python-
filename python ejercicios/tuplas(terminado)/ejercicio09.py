'''
Crea dos tuplas y compara sus longitudes. Imprime un mensaje que indique cuál es más larga.
'''

#Crear la primera tupla
tupla1 =  (5, 3, 'hola', True)
print(f"La tupla  1 tiene {len(tupla1)} elementos.")

#Crear la segunda tupla
tupla2 = ('Python', 'Ruby', 'Java', 0)
print(f"\nLa tupla 2 tiene {len(tupla2)} elementos.")

#Comparar las longitudes de ambas tuplas
if len(tupla1)>len(tupla2):
    print("\nTupla 1 es más larga")
elif len(tupla1)<len(tupla2):
    print("Tupla 2 es más larga")
else:
    print("Las dos tuplas tienen la misma longitud")
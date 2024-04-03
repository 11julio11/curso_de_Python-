'''
 Accede al valor asociado a una clave específica en el diccionario que creaste en el ejercicio anterior e imprímelo.
'''

#creamos y anexamos la informaciom
nombre_Y_edades = {
"nombre": 'horacio', "años": 2,
"nombre": 'horacio', "años": 10,
"nombre": 'maria', "años": 5,
}


#accedemos  a los valores de las claves especificadas en el diccionario.
print(nombre_Y_edades["nombre"]) # devuelve Horacio o Maria segun se pida
print(nombre_Y_edades[("años")]) #devuelve los años de cada persona


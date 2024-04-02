'''
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio 
<asignatura>,
 donde <asignatura> es cada una de las asignaturas de la lista.
'''
#creamos una varible para alacenar  las asignaturas
asignaturas_curso = ["matematicas", "fisica", "quimica", "historia", "lengua"]

#imprimimos  por pantalla 
print("Yo estudio asignaturas  como:")
               #len sirve  para obtener el tamaño del contenedor, en este caso es una lista
#agregamos  un for para recorrer el rango de nuestra variable y mostrar los elementos de esa lista
for i in range(len(asignaturas_curso)):
    # i+1 se utiliza para mostrar los numeros de asignatura (no de indice)
    print(f"{i+1}. {asignaturas_curso[i]}")
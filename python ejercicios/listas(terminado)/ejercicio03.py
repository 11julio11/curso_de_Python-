'''
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
 en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, 
 y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura>
 es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
'''

# creamos una variable para  guardar la cantidad de asignaturas
curso = ["matematicas",  "fisica","biologia", "quimica", "historia", "lengua" ]

# luego una lista vacia  para meter los valores introducidos por teclado
notas=[]
#usamos for in  range para recorrer el rango de la longitud del curso , es decir , i va a ir de 0 hasta la penultima
for i in range(len(curso)):
    #usamos %s para sustituir el valor de i en el string
    print("En %s escribe tu nota:"%(curso[i]))
    #ponemos notas.append() para meter el dato introducido a la lista notas
    notas.append(float(input()))
    
    #print("\n")  para saltos de línea
print("\n")
#Ahora vamos a mostrar las notas por pantalla como se indica en el ejercicio:
for i in range(len(curso)):
    print ("En %s has sacado %.2f"%(curso[i],notas[i]))
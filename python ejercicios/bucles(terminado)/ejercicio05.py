'''
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10
'''
# Mostrar la tabla de multiplicar del 1 al 10
for i in range(1, 11):
    # i  es el multiplicando y j es el multiplo
    print(f"Tabla de multiplicar del {i}:")
    for j in range(1, 11):
        # {j}  es lo mismo que decir "j * i" 
        print(f"{i} x {j} = {i * j}")
    print()
    #usamos 2 print  para separar las filas
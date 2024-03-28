'''
Escribir un programa que muestre el eco de todo lo que 
el usuario introduzca hasta
 que el usuario escriba “salir” que terminará.
'''



# Mostrar el eco de todo lo que el usuario ingresa
while True:
    entrada = input("> ")
    if entrada == "salir":
        break
    print("Eco:", entrada)
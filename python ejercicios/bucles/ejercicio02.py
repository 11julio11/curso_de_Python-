'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
'''
#preguntamos la edad del usuario
edad = int(input("Por favor ingrese su edad: "))
for i in range(edad):
    print ("has cumplido al rededor de  " + str(i+1) + "años.")
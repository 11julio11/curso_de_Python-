'''
 Escribe un programa que pida al usuario tres números y luego muestre cuál de los tres números es el mayor.
'''
#hacemos el ingreso de los tres numeros
numero1 = int(input("ingrese el primer numero: "))
numero2 = int(input("ingrese el segundo numero: "))
numero3 = int(input("ingrese el tercer numero: "))

if (numero1 > numero2) and (numero1 > numero3): #el primero es el mayor
    print ("El número", numero1, "es el mayor")  
elif (numero2 > numero1) and (numero2 > numero3): #el segundo es el mayor 
    print ("El número", numero2, "es el mayor")
else:                                            #el tercero es el mayor
    print ("El número", numero3, "es el mayor")
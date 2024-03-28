'''
Escribe un programa que pida al usuario dos números y una operación (suma, resta, multiplicación o división)
 y luego muestre el resultado de la operación.
'''
#pedimos al usuario los dos numeros
numero1 = int(input("ingresa el primer numero: "))

numero2 = int(input("ingresa el segundo numero: "))

#pedirle a al usuario la operacion
operacion= input ("Ingrese la operacion a realizar (+,-,*,/): ")

if operacion == "+": #si la operacion es suma
    print("la suma de", numero1,"y",numero2,"es: ",numero1+numero2)


elif operacion == "-": #si la operacion es resta
    print("la resta de", numero1,"menos",numero2,"es: ",numero1-numero2)


elif operacion == "*": #si la operacion es multiplicacion
    print("el producto de", numero1,"por",numero2,"es: ",numero1*numero2)

elif operacion ==  "/" : #si la operacion es division
    if numero2==0: #evitamos error de division por cero
        print("no se puede dividir entre cero")
    else:
        print("el cociente de", numero1,"entre",numero2,"es: ",numero1//numero2)
        print("el residuo de la division de", numero1,"entre",numero2,"es: ",numero1%numero2)
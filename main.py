#suma de dos numeros
def sumNumbers(a, b):
    sum = a + b
    return sum

#entrada del tokin 
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

#funcion de la llamada
sum = sumNumbers(num1, num2)

#mostrar resultado
print("sum of numbers is: " + str(sum))
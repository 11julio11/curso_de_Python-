# Función para sumar dos números
def sumNumbers(a, b):
  # Calcular suma de a y b
  sum = a + b  # type: ignore
  # Devolver la suma
  return sum  # type: ignore

# Solicitar primer número de entrada
num1 = int(input("ingrese el primer número: "))

# Solicitar segundo número de entrada
num2 = int(input("ingrese el segundo número: "))

# Llamar a la función
sum = sumNumbers(num1, num2)

# Mostrar resultado
print("suma de números es: " + str(sum))
'''Crea un programa que solicite al usuario su nombre, edad y género. Luego, muestra un mensaje que diga "Hola,
 [nombre]", "Tienes [edad] años" y "Eres [género]"'''

# Solicita el nombre del usuario
name = input("¿Cuál es tu nombre? ")

# Solicita la edad del usuario y la convierte en un entero
age = int(input("¿Cuántos años tienes? "))

# Solicita el género del usuario
gender = input("¿Cuál es tu género? ")

# Imprime un mensaje de saludo
print(f"Hola, {name}")

# Imprime un mensaje indicando la edad del usuario
print(f"Tienes {age} años")

# Imprime un mensaje indicando el género del usuario
print(f"Eres {gender}")

# Agrega una pausa para hacer que el resultado sea más interesante
import time
time.sleep(1)

# Imprime una sorprendida declaración sobre la edad del usuario
print("Wow, ¡tienes " + str(age) + " años?!")

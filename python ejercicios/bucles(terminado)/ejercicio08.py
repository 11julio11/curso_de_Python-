'''
Escribe un programa que calcule la suma de los dígitos de un número entero ingresado por el usuario.
'''

def sum_digits(num):
    """
    Función que recibe un número entero y devuelve la suma de sus dígitos.
    
    Parámetros:
        num (int): Número entero del cual se desea calcular la suma de sus dígitos.  
        
    Devuelve:
        # int: La suma de los dígitos del número ingresado.
    """
    # Convertir el número a cadena para poder acceder a cada uno de sus dígitos
    str_num = str(num)
    digit_sum = 0
    
    for d in str_num:
        # Sumar cada dígito convertido a entero
        digit_sum += int(d)
    
    return digit_sum

# Leer el número desde teclado
n = int(input("Ingrese un número entero: "))

# Calcular e imprimir la suma de sus dígitos
print("La suma de los dígitos de", n, "es:", sum_digits(n))
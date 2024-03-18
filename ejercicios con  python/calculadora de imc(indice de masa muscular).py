'''
Pide al usuario que ingrese su peso en 
kg y su altura en metros, luego calcula su IMC utilizando la fórmula: IMC = peso / (altura * altura).
'''

peso = float(input("ingrese su peso corporal: "))

altura = float(input("ingrese  su altura en metros: "))

IMC = peso/(altura * altura)

print("su imc es: ", IMC)
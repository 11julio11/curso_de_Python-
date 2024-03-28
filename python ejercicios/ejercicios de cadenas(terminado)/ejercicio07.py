'''
Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre 
por pantalla otro correo electrónico con el 
mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
'''
# Solicitar el correo electrónico del usuario
user_email = input("Por favor, introduce tu dirección de correo electrónico: ")

# Extraer el nombre de usuario del correo electrónico
#utlizamos  el método split para separar el nombre de usuario del dominio
user_name = user_email.split("@")[0]

# Mostrar el nuevo correo electrónico con el dominio `ceu.es`
print(f"Tu nueva dirección de correo electrónico es {user_name}@ceu.es")
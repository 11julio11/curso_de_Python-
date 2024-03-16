'''
los modulos  son como una caja fuerte que nos permite agrupar funciones y variables en un solo lugar para poder reutilizarlas.
/*!
 * Bootstrap v3.1.0 (http://getbootstrap.com)
 * Copyright 2011-2014 Twitter, Inc.
 * Licensed under the MIT license

 tambien estos los podemos escribir nosotros mismo, 
 descargadas desde internet
 y los modelos desdelas propias bibliotecas de python */
'''

# import datetime
# print(datetime.date.today())
# #muestra  la fecha actual del sistema

#tambien la podemos importar de esta manera 
# from datetime import timedelta

# print(timedelta(minutes=700))


# importamos el modulo que queremos utilizar 
#import fmath

#fmath.substract(1,2)

#tambien lo podemos importar de esta manera 

# from fmath import add, substract

# substract(1,2)
# add(1,2)

from colorama import Fore, Style, init
init(convert=True)
print(Fore.YELLOW + "hello world")
print(Fore.BLUE+ "I am learning Python")
print(Fore.RED+"This is Red Text")

#dictionaries
'''
los diccionarios/dictionaries sirven para definir objetos de la vida real y 
tambien para agrupar distintos datos como claves y valores
'''
product = {
    "name": "iPhone 12",
    "price": 999.0,
    "brand": "Apple",
    "quantity": 5,
}

person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "email": "john@doe.com",
}

#funcion para obtener las claves  de un diccionario
#print(person.keys())

#funcion para obtener los items  (clave-valor) de un diccionario
#print(person.items())

print(person.items())
person.clear()   #elimina todos los elementos del diccionario

print(person)

products = [
{"name": 'book', "price": 49.9},
{'name': 'tablet', 'price': 199.9},
]

print(products)
        

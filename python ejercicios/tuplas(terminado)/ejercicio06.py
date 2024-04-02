'''
Desarrolla un programa que verifique si un elemento específico existe en una tupla.
'''

# creamos la tupla con varios elementos 

tupla = ('ferraty', 'manzana', 1, 100, 'moto')

def buscar_elemento(elemento):
    if elemento in tupla:
        return True
    else:
        return False

def pedir_elemento():
    elemento_a_buscar = input('Introduce un elemento a buscar: ')
    encontrado = buscar_elemento(elemento_a_buscar)
    if encontrado:
        print(f'Sí, el elemento "{elemento_a_buscar}" está en la tupla.')
    else:
        print(f'No, el elemento "{elemento_a_buscar}" no está en la tupla.')

pedir_elemento()



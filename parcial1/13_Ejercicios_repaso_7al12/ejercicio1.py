"""
1.- 

Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

a.- Recorrer la lista y mostrarla
b.- hacer una funcion que recorra la lista de numeros y devuelva un string
c.- ordenarla y mostrarla
d.- mostrar su longitud
e.- buscar algun elemento que el usuario pida por teclado

"""

#b) funcion que recorra lista de numeros y devuelva un string
def recorrer_numeros():
    for iterador in lista_numeros:
        print(str(iterador))


lista_numeros = [50, 60, 70, 80, 10, 20, 30, 40]
recorrer_numeros()

#a) recorrer lista y mostrarla
for iterador in lista_numeros:
    print(iterador)

#c) ordenar y mostrar lista
lista_numeros.sort()
print(lista_numeros)

#d) mostrar su longitud
print(f"Longitud de la lista: {len(lista_numeros)}")

#e) buscar algun elemento que el usuario pida por teclado

try:
    valor_a_buscar = int(input("Ingrese el valor a buscar en la lista:\n"))
    for iterador in lista_numeros:
        if valor_a_buscar == iterador:
            print(f"{valor_a_buscar} encontrado y encontrado en posicion {lista_numeros.index(iterador)}.")
except ValueError:
    print("Ingrese un valor de tipo entero.")
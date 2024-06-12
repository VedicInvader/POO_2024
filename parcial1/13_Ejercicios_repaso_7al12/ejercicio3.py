"""
3.- 

Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
el contenido de la lista en mayusculas
"""

lista = []

print("Comprobando si la lista está vacía...")

if len(lista) == 0:
    print("La lista está vacía. Agregue elementos.")
    bandera = 1
    while bandera == 1:
        nuevoElemento = input("\nInserte nuevo elemento a la lista: ")
        lista.append(nuevoElemento)
        opcion = input("\n¿Desea agregar otra cosa? S/N: ").lower()
        if opcion == "n":
            bandera = 0
else:
    print("La lista tiene elementos.")

for i in range(0, len(lista)):
    elementoMayus = lista[i].upper()
    lista.pop(i)
    lista.insert(i, elementoMayus)
print("\n")
print(lista)
"""
2.- 
Escribir un programa  que añada valores a una lista mientras que su longitud 
sea menor a 120, y luego mostrar la lista: Usar un while y for
"""

lista1 = []

#Con ciclo while
# while len(lista) <= 120:
#     agregar_lista1 = input("Ingresa valor nuevo a la lista: ")
#     lista1.append(agregar_lista1)

# print(lista)

#Con ciclo for

lista2 = []

for iterador in range(0, 120):
    agregar_lista2 = input("Ingresa valor nuevo a la lista: ")
    lista2.append(agregar_lista2)

print(lista2)
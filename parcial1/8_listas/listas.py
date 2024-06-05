"""

List (Array)
Son colecciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un índice numérico

Nota: sus valores sí son modificados

La lista es una colección ordenada y modificable.
Permite miembros duplicados.

"""

#Ejemplo 1: crear una lista de números e imprimir su contenido

numeros = [1, 2, 3, 4, 5]

#Recorrer la lista con un ciclo for
# for i in numeros:
#     print(i)

#Recorrer la lista con un ciclo while
# i = 0
# while i <= len(numeros) - 1:
#     print(numeros[i])
#     i += 1


#Ejemplo 2: crear una lista de palabras y posteriormente buscar la coincidencia de una palabra

# continentes = ["America", "Europa", "Africa", "Asia", "Oceania", "Antartida"]

# buscarPalabra = input("Ingresa la palabra a buscar: ")

# for iterador in continentes:
#     if buscarPalabra == iterador:
#         print(f"'{buscarPalabra}' encontrado en la posicion {continentes.index(iterador)}")

# if buscarPalabra not in continentes:
#     print("Palabra no encontrada.")

#Hecho con un ciclo while

continentes = ["America", "Europa", "Africa", "Asia", "Oceania", "Antartida"]

buscarPalabra = input("Ingrese palabra a buscar: ")

iterador = 0

while iterador < len(continentes):
    if buscarPalabra == continentes[iterador]:
        print(f"'{buscarPalabra}' fue encontrado en la posicion {continentes.index(iterador)}")
    iterador += 1

if buscarPalabra not in continentes:
    print("Palabra no encontrada.")



#Ejemplo 3: agregar y eliminar elementos de una lista
#os.system("clear")

# numeros = [23, 34, 23]
# print(numeros)

# #Agregar un elemento
# numeros.append(100)
# print(numeros)

# numeros.insert(3, 200)
# print(numeros)

# #Eliminar un elemento
# numeros.remove(100) #indicar el elemento a borrar
# print(numeros)

# numeros.pop(2) #indicar la posicion del elemento a borrar
# print(numeros)
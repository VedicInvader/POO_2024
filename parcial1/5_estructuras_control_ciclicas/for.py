#   Este ciclo es una estructura de control repetitiva o ciclica que funciona con iteraciones "x" veces de acuerdo a los valores numericos enteros que contenga

#   Sintaxis:

#   for variable in elemento_iterable (list, range, etc):
#       bloque de instrucciones

#   Ejemplo 1:
#   Crear un programa que imprima cinco veces el caracter @

for contador in  range(1, 6):
    print("@")

#   Ejemplo 2:
#   Crear un programa que imprima los numeros del 1 al 5, los sume e imprima la suma al final

suma = 0
for contador in range(1, 6):
    print(contador)
    suma += contador
print(suma)

#   Ejemplo 3:
#   Crear un programa que solicite un numero y a partir de este numero, generar e imprimir la tabla de multiplicar correspondiente

numero = int(input("Ingrese un numero a mostrar su tabla de multiplicar: "))
res = 0
for contador in range(1, 11):
    res = numero * contador
    print(f"{numero} * {contador} = {res}")
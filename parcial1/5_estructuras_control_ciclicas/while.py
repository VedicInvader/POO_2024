#   Este ciclo es una estructura de control repetitiva o ciclica que funciona con iteraciones "x" veces siempre y cuando la condicions sea True

#   Sintaxis

#   while condicion:
#       bloque de instrucciones

#   Ejemplo 1:
#   Crear un programa que imprima cinco veces el caracter @

contador = 1
while contador < 6:
    print('@')
    contador += 1

#   Ejemplo 2:
#   Crear un programa que imprima los numeros del 1 al 5, los sume e imprima la suma al final

contador = 1
suma = 0

while contador < 6:
    suma += contador
    print(contador)
    contador += 1
print(suma)

#   Ejemplo 3:
#   Crear un programa que solicite un numero y a partir de este numero, generar e imprimir la tabla de multiplicar correspondiente

numero = int(input("Ingrese un numero: "))

contador = 1
res = 0

while contador < 11:
    res = numero * contador
    print(f"{numero} * {contador} = {res}")
    contador += 1


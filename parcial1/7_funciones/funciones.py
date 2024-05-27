"""
    Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular, como un programa más pequeño que cumple
    una función específica. La función se puede reutilizar con el simple hecho de invocarla, es decir, mandarla llamar.

    Sintaxis:

    def nombreFuncion (parametros):
        bloque de instrucciones

    Las funciones pueden ser de cuatro tipos:

    I. Función que no recibe parámetros y no regresa valor.
    II. Función que no recibe parámetros y regresa valor.
    III. Función que recibe parámetros y no regresa valor.
    IV. Función que recibe parámetros y regresa valor.
"""

#Ejemplo 1: crear una función para imprimir nombres de personas
#Función que no recibe parámetros y no regresa valor

def solicitarNombre():
    nombre = input("Ingrese su nombre completo: ")

solicitarNombre()

#Ejemplo 2: sumar dos números

def suma():
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    suma = num1 + num2
    print(f"La suma de {num1} y {num2} es: {suma}")

suma()

#Ejemplo 3: sumar dos números
#Función que no recibe parámetros y regresa valor

def suma():
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    suma = num1 + num2
    return suma

resultado_suma = suma()
print(f"El resultado es {resultado_suma}")

#Ejemplo 4:
#Función que recibe parámetros y no regresa valor

def suma(num1, num2):
    suma = num1 + num2
    return suma

num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
suma(num1, num2)
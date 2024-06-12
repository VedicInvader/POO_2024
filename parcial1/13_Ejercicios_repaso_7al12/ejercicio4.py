"""
 4.- 

Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones
"""

lista = ["Serbia"]
cadena = "Bosnia y Herzegovina"
entero = 20
logico = True


def tipo_dato(variable):
    print(type(variable))

tipo_dato(lista)
tipo_dato(cadena)
tipo_dato(entero)
tipo_dato(logico)



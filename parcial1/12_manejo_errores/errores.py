#Los errores de ejecucion en un lenguaje de programacion se presentan cuando existe una anomalia o error dentro de la ejecucion
#del codigo, lo cual provoca que se detenga la ejecucion del mismo. Con el control y manejo de excepciones, sera posible
#minimizar o evitar la interrupcion del programa debido a una exepcion.

#Ejemplo 1: cuando una variable no se genera
# nombre = input("Introduce el nombre completo de una persona: ")

# try:
#     if len(nombre) > 0:
#         nombre_usuario = "El nombre completo del usuario es: " + nombre

#     print(nombre_usuario)
# except: #Si no se pone esto, se detendrá todo el programa cuando se genere un error. De este modo, si ocurre un error, lo notifica, pero sigue con el flujo del programa m
#     print("Es necesario introducir un nombre de usuario... verifique por favor.")


#Ejemplo 2: cuando se solicita un numero y se ingresa otra cosa
# try:
#     numero = int(input("Ingrese un numero entero: "))

#     if numero > 0:
#         print("Soy un numero entero positivo.")
#     elif numero == 0:
#         print("Soy un numero entero neutro.")
#     else:
#         print("Soy un numero entero negativo.")
# except ValueError:
#     print("Ingresa un numero entero.")

#Ejemplo 3: cuando se generan multiples excepciones

try:
    numero = int(input("Introduce un numero: "))
    print(f"El cuadrado del numero es {numero ** 2}")
except ValueError:
    print("Introduce un valor numerico entero.")
except TypeError:
    print("Se debe convertir el numero a entero")
else:
    print("No se presentaron errores de ejecucion")
finally:
    print("Termine la ejecucion")

#   Esta estructura de control evalua una condicion. Si la condicion se cumple, se ejecita la o las instrucciones contenidas dentro de ella

#   Tiene 4 variantes:
#   I. if simple
#   II. if compuesto
#   III. if anidado
#   IV. if con elif

#   Ejemplo de if simple

color = "verde"

if color == "verde":
    print("Soy color verde.")

#   Ejemplo de if compuesto

color = "blanco"

if color == "verde":
    print("Soy color verde.")
else:
    print("No soy color verde.")

#   Ejemplo de if anidado

color = "blanco"

if color == "verde":
    print("Soy color verde.")
else:
    if color == "blanco":
        print("No soy color verde, pero soy color blanco.")
        if color != "verde" and color != "blanco":
            print("No soy color verde.")    

#   Ejemplo de if con elif

color = input("Ingrese color: ")

if color == "rojo":
    print("Soy color rojo.")
elif color == "blanco":
    print("Soy color blanco.")
elif color == "negro":
    print("Soy color negro.")
else:
    print("No soy ninguno de los colores anteriores.")
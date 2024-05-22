#   Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario

print("Mostrar todos los numeros entre dos numeros que decida el usuario")
rango1 = int(input("Ingrese el valor del rango inferior: "))
rango2 = int(input("Ingrese el valor del rango superior: "))

for contador in range(rango1, rango2):
    print(contador)
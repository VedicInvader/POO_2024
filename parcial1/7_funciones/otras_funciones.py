import math

def solicitarNumeros():
    # global n1, n2 #Para hacer globales a las variables locales
    n1 = int(input("Ingrese numero 1: "))
    n2 = int(input("Ingrese numero 2: "))
    return n1, n2
def solicitarUnSoloNumero():
    n3 = int(input("Ingresa el numero: "))
    return n3

def operacion(num1, num2, opc):
    match (opc):
        case (1):
            suma = num1 + num2
            return f"El resultado es {suma}"
        case (2):
            resta = num1 - num2
            return f"El resultado es {resta}"          
        case (3):
            mult = num1 * num2
            return f"El resultado es {mult}"    
        case (4):
            division = num1 / num2
            return f"El resultado es {division}"
        case (5):
            potencia = num1 ** num2
            return f"El resultado es {potencia}"
        case (6):
            raiz = math.sqrt(num1)
            return f"El resultado es {raiz}"
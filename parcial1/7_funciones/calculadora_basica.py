import os 
from otras_funciones import * #Se pone asterisco para importar todas las funciones del archivo

# bandera = 1

# while bandera == 1:
#     print(""".::      MENU PRINCIPAL      ::. \n
#     1.    SUMA
#     2.    RESTA
#     3.    MULTIPLICACION
#     4.    DIVISION
#     5.    SALIR
#           """)
#     opc = int(input("Elige una opcion: "))

#     match (opc):
#         case (1):
#             num1 = int(input("Ingrese el primer numero: "))
#             num2 = int(input("Ingrese el segundo numero: "))
#             suma = num1 + num2
#             print(f"El resultado es {suma}")
#         case (2):
#             num1 = int(input("Ingrese el primer numero: "))
#             num2 = int(input("Ingrese el segundo numero: "))
#             resta = num1 - num2
#             print(f"El resultado es {resta}")          
#         case (3):
#             num1 = int(input("Ingrese el primer numero: "))
#             num2 = int(input("Ingrese el segundo numero: "))
#             mult = num1 * num2
#             print(f"El resultado es {mult}")         
#         case (4):
#             num1 = float(input("Ingrese el primer numero: "))
#             num2 = float(input("Ingrese el segundo numero: "))
#             division = num1 / num2
#             print(f"El resultado es {division}")            
#         case (5):
#             print("Ha terminado.")
#             bandera = 0
#         case _:
#             print("Opcion incorrecta, intente de nuevo.")


# def solicitarNumeros():
#     global n1, n2 #Para hacer globales a las variables locales
#     n1 = int(input("Ingrese numero 1: "))
#     n2 = int(input("Ingrese numero 2: "))

# def operacion(num1, num2, opc):
#     match (opc):
#         case (1):
#             suma = num1 + num2
#             return f"El resultado es {suma}"
#         case (2):
#             resta = num1 - num2
#             return f"El resultado es {resta}"          
#         case (3):
#             mult = num1 * num2
#             return f"El resultado es {mult}"    
#         case (4):
#             division = num1 / num2
#             return f"El resultado es {division}"  
                 
bandera = True
while bandera == True:
    print(""".::      MENU PRINCIPAL      ::. \n
    1.    SUMA
    2.    RESTA
    3.    MULTIPLICACION
    4.    DIVISION
    5.    POTENCIA
    6.    RAIZ
    7.    SALIR
            """)
    oper = int(input("Elige una opcion: "))
    if oper == 7:
        bandera = False
        print("Ha terminado.")
    elif oper == 6:
       n3 = solicitarUnSoloNumero()
       print(operacion(n3, 0, oper))
       input("Ingrese una tecla para continuar...")
       os.system("clear")
    else:
        n1, n2 = solicitarNumeros()
        print(operacion(n1, n2, oper))  
        input("Ingrese una tecla para continuar...")
        os.system("clear")

    #
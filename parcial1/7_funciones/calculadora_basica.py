bandera = 1

while bandera == 1:
    print(""".::      MENU PRINCIPAL      ::. \n
    1.    SUMA
    2.    RESTA
    3.    MULTIPLICACION
    4.    DIVISION
    5.    SALIR
          """)
    opc = int(input("Elige una opcion: "))

    match (opc):
        case (1):
            num1 = int(input("Ingrese el primer numero: "))
            num2 = int(input("Ingrese el segundo numero: "))
            suma = num1 + num2
            print(f"El resultado es {suma}")
        case (2):
            num1 = int(input("Ingrese el primer numero: "))
            num2 = int(input("Ingrese el segundo numero: "))
            resta = num1 - num2
            print(f"El resultado es {resta}")          
        case (3):
            num1 = int(input("Ingrese el primer numero: "))
            num2 = int(input("Ingrese el segundo numero: "))
            mult = num1 * num2
            print(f"El resultado es {mult}")         
        case (4):
            num1 = int(input("Ingrese el primer numero: "))
            num2 = int(input("Ingrese el segundo numero: "))
            division = num1 / num2
            print(f"El resultado es {division}")            
        case (5):
            bandera = 0
        case _:
            print("Opcion incorrecta, intente de nuevo.")
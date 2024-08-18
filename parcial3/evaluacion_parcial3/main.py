from autos import autos
from clientes import clientes
from revisiones import revisiones
from usuario import usuario
from funciones import *
import getpass

def menu_login():
    while True:
        print("""
.:::   MENU DE REGISTRO/INICIO DE SESION   :::.
        
    1. REGISTRO
    2. INICIO DE SESION
    3. SALIR
""")
        opcion_login = int(input("Ingresa el numero de opcion elegida: "))
        match opcion_login:
            case 1:
                borrarPantalla()
                print("\n \t .:::       REGISTRO DE USUARIO   :::.")
                
                nombre = input("\tIngresa tu nombre: ")
                apellidos = input("\tIngresa tus apellidos: ")
                email = input("\tIngresa tu correo electronico: ")
                password = getpass.getpass ("\tIngresa la contrasenia que vas a usar: ")

                obj_usuario = usuario.Usuarios(nombre, apellidos, email, password)
                resultado = obj_usuario.registrar()

                if resultado:
                    borrarPantalla()
                    print(f"\nUsuario {nombre} {apellidos} se ha registrado con exito.")
                    input("Pulsa ENTER para continuar...")
                    
                else:
                    print("Fallo al crear usuario, intenta de nuevo.")
                    input("Pulsa ENTER para continuar...")
                    borrarPantalla()
            case 2:
                print("\n \t .:::   INICIO DE SESION   :::.")
                email = input("\tIngresa tu correo electronico: ")
                password = getpass.getpass("\tIngresa tu contrasenia: ")

                login = usuario.Usuarios.iniciar_sesion(email, password)

                if login:
                    menu_principal(login[1], login[2])
                else:
                    print("Correo y/o contrasenia incorrectos. Intenta de nuevo.")
                    input("Pulsa ENTER para continuar...")
                    borrarPantalla()
            case 3:
                borrarPantalla()
                print("Gracias por utilizar este programa.")
                break
            case _:
                print("Opcion incorrecta elige de nuevo.")
        



def menu_principal(nombre, apellidos):
    while True:
        borrarPantalla()
        print("\n \t .:::   AGENCIA DE AUTOS   :::.")
        print(f"\n\tBIENVENIDO {nombre} {apellidos}")
        print("""
        .:::   MENU PRINCIPAL   :::.
            
                1. CLIENTES
                2. AUTOS
                3. REVISIONES
                4. SALIR
        """)
        opc = int(input("Elige una opcion: "))
        match opc:
            case 1:
                    while True:
                        borrarPantalla()
                        print("\n \t .:::   MENU PRINCIPAL   :::.")
                        print("""
                    BIENVENIDO AL SISTEMA GESTOR DE CLIENTES

                    1. ANIADIR CLIENTE
                    2. MOSTRAR CLIENTES
                    3. ACTUALIZAR CLIENTE
                    4. ELIMINAR CLIENTE
                    5. SALIR
                            """)
                        opc = int(input("Elige el numero de la operacion a realizar: "))
                        match opc:
                            case 1:
                                borrarPantalla()
                                print("\n \t .:::   ANIADIR CLIENTE   :::.")
                                print("INGRESA LOS DATOS DEL CLIENTE\n")
                                nif = int(input("\tINGRESA EL N.I.F. DEL CLIENTE: "))
                                nombre = input("\tINGRESA EL NOMBRE DEL CLIENTE: ").upper()
                                direccion = input("\tINGRESA LA DIRECCION DEL CLIENTE: ").upper()
                                ciudad = input("\tINGRESA LA CIUDAD DEL CLIENTE: ").upper()
                                tel = int(input("\tINGRESA EL NUMERO TELEFONICO DEL CLIENTE: "))

                                objeto_cliente = clientes.Clientes(nif, nombre, direccion, ciudad, tel)

                                resultado = objeto_cliente.insertar()

                                if resultado:
                                    print("Cliente agregado exitosamente.")
                                    input("Pulsa una tecla para continuar...")
                                    borrarPantalla()
                                else:
                                    print("Error al agregar el cliente.")
                            case 2:
                                borrarPantalla()
                                print("\n \t .:::   CLIENTES EN LA BASE DE DATOS   :::.")
                                clientes.Clientes.consultar()
                                input("Pulsa una tecla para continuar...")
                                borrarPantalla()
                                
                            case 3:
                                borrarPantalla()
                                print("\n \t .:::   ACTUALIZAR CLIENTE   :::.\n")

                                nif_id = input("INGRESA EL N.I.F. DEL CLIENTE AL QUE SE ACTUALIZARAN LOS DATOS: ")

                                print("\nINGRESA LOS NUEVOS DATOS DEL CLIENTE\n")
                                nombre = input("\tINGRESA EL NOMBRE DEL CLIENTE: ").upper()
                                direccion = input("\tINGRESA LA DIRECCION DEL CLIENTE: ").upper()
                                ciudad = input("\tINGRESA LA CIUDAD DEL CLIENTE: ").upper()
                                tel = int(input("\tINGRESA EL NUMERO TELEFONICO DEL CLIENTE: "))

                                objeto_cliente = clientes.Clientes(None, nombre, direccion, ciudad, tel)

                                resultado = objeto_cliente.actualizar(nif_id)

                                if resultado:
                                    print("Cliente actualizado correctamente.")
                                    input("Pulsa una tecla para continuar...")
                                    borrarPantalla()
                                else:
                                    print("Ha ocurrido un error al actualizar el cliente.")
                                    input("Pulsa una tecla para continuar...")
                                    borrarPantalla()
                            case 4:
                                borrarPantalla()
                                print("\n \t .:::   ELIMINAR CLIENTE   :::.\n")

                                nif_id = input("INGRESA EL N.I.F. DEL CLIENTE A ELIMINAR: ")

                                obj_cliente = clientes.Clientes(0, "", "", "", 0)

                                resultado = obj_cliente.eliminar(nif_id)

                                if resultado:
                                    print("Cliente eliminado correctamente.")
                                    input("Pulsa una tecla para continuar...")
                                    borrarPantalla()
                                else:
                                    print("Ha ocurrido un error al eliminar el Cliente.")
                                    input("Pulsa una tecla para continuar...")
                                    borrarPantalla()

                            case 5:
                                borrarPantalla()
                                break
                            case _:
                                print("Has escogido una opcion invalida, intenta de nuevo...")
            case 2:
                    while True:
                        borrarPantalla()
                        print("\n \t .:::   MENU PRINCIPAL   :::.")
                        print("""
                    BIENVENIDO AL SISTEMA GESTOR DE AUTOS

                    1. ANIADIR AUTO
                    2. MOSTRAR AUTOS
                    3. ACTUALIZAR AUTO
                    4. ELIMINAR AUTO
                    5. SALIR
                            """)
                        opc = int(input("Elige el numero de la operacion a realizar: "))
                        match opc:
                            case 1:
                                borrarPantalla()
                                print("\n \t .:::   ANIADIR AUTO   :::.")
                                print("INGRESA LOS DATOS DEL AUTO\n")
                                matricula = input("\tINGRESA LA MATRICULA DEL VEHICULO (7 CARACTERES): ")
                                marca = input("\tINGRESA LA MARCA DEL AUTO: ")
                                modelo = int(input("\tINGRESA EL MODELO (ANIO) DEL AUTO: "))
                                color = input("\tINGRESA EL COLOR DEL AUTO: ")
                                nif = int(input("\tINGRESA EL N.I.F. DEL AUTO (5 NUMEROS): "))

                                objeto_auto = autos.Autos(matricula, marca, modelo, color, nif)

                                resultado = objeto_auto.insertar()

                                if resultado:
                                    print("Auto agregado exitosamente.")
                                    input("Pulsa una tecla para continuar...")
                                    borrarPantalla()
                                else:
                                    print("Error al agregar el auto.")
                            case 2:
                                borrarPantalla()
                                print("\n \t .:::   AUTOS EN LA BASE DE DATOS   :::.")
                                autos.Autos.consultar()
                                input("Pulsa una tecla para continuar...")
                                borrarPantalla()
                                
                            case 3:
                                borrarPantalla()
                                print("\n \t .:::   ACTUALIZAR AUTO   :::.\n")

                                matricula_id = input("INGRESA LA MATRICULA DEL AUTO AL QUE SE ACTUALIZARAN LOS DATOS: ")

                                print("\nINGRESA LOS NUEVOS DATOS DEL AUTO\n")
                                marca = input("\tINGRESA LA MARCA DEL AUTO: ")
                                modelo = int(input("\tINGRESA EL MODELO (ANIO) DEL AUTO: "))
                                color = input("\tINGRESA EL COLOR DEL AUTO: ")
                                nif = int(input("\tINGRESA EL N.I.F. DEL AUTO (5 NUMEROS): "))

                                objeto_auto = autos.Autos(None, marca, modelo, color, nif)

                                resultado = objeto_auto.actualizar(matricula_id)

                                if resultado:
                                    print("Auto actualizado correctamente.")
                                    input("Pulsa una tecla para continuar...")
                                    borrarPantalla()
                                else:
                                    print("Ha ocurrido un error al actualizar el coche.")
                                    input("Pulsa una tecla para continuar...")
                                    borrarPantalla()
                            case 4:
                                borrarPantalla()
                                print("\n \t .:::   ELIMINAR AUTO   :::.\n")

                                matricula_id = input("INGRESA LA MATRICULA DEL AUTO A ELIMINAR: ")

                                obj_auto = autos.Autos("", "", 0, "", 0)

                                resultado = obj_auto.eliminar(matricula_id)

                                if resultado:
                                    print("Auto eliminado correctamente.")
                                    input("Pulsa una tecla para continuar...")
                                    borrarPantalla()
                                else:
                                    print("Ha ocurrido un error al eliminar el coche.")
                                    input("Pulsa una tecla para continuar...")
                                    borrarPantalla()

                            case 5:
                                borrarPantalla()
                                break
                            case _:
                                print("Has escogido una opcion invalida, intenta de nuevo...")
            case 3:
                    while True:
                        borrarPantalla()
                        print("\n \t .:::   MENU PRINCIPAL   :::.")
                        print(f"""
                    BIENVENIDO AL SISTEMA GESTOR DE REVISIONES

                    1. ANIADIR REVISION
                    2. MOSTRAR REVISIONES
                    3. ACTUALIZAR REVISION
                    4. ELIMINAR REVISION
                    5. SALIR
                            """)
                        opc = int(input("Elige el numero de la operacion a realizar: "))
                        match opc:
                            case 1:
                                borrarPantalla()
                                print("\n \t .:::   ANIADIR REVISION   :::.")
                                print("INGRESA LOS DATOS DE LA REVISION\n")

                                no_revision = int(input("\tINGRESA EL NUMERO DE REVISION (5 CARACTERES): "))
                                cambiofiltro = input("\t¿CAMBIO DE FILTRO? (S/N): ").upper()
                                cambioaceite = input("\t¿CAMBIO DE ACEITE? (S/N): ").upper()
                                cambiofrenos = input("\t¿CAMBIO DE FRENOS? (S/N): ").upper()
                                otros = input("\t¿ALGUNA OTRA REVISION? ESCRIBELA:  ").upper()
                                matricula = input("\tINGRESA LA MATRICULA DEL AUTO: ").upper()


                                objeto_revision = revisiones.Revisiones(no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula)

                                resultado = objeto_revision.insertar()

                                if resultado:
                                    print("Revision agregado exitosamente.")
                                    input("Pulsa una tecla para continuar...")
                                    borrarPantalla()
                                else:
                                    print("Error al agregar el cliente.")
                            case 2:
                                borrarPantalla()
                                print("\n \t .:::   REVISIONES EN LA BASE DE DATOS   :::.")
                                revisiones.Revisiones.consultar()
                                input("Pulsa una tecla para continuar...")
                                borrarPantalla()
                                
                            case 3:
                                borrarPantalla()
                                print("\n \t .:::   ACTUALIZAR REVISION   :::.\n")

                                revision_id = input("INGRESA EL NUMERO DE LA REVISION A LA QUE SE ACTUALIZARAN LOS DATOS: ")

                                cambiofiltro = input("\t¿CAMBIO DE FILTRO? (S/N): ").upper()
                                cambioaceite = input("\t¿CAMBIO DE ACEITE? (S/N): ").upper()
                                cambiofrenos = input("\t¿CAMBIO DE FRENOS? (S/N): ").upper()
                                otros = input("\t¿ALGUNA OTRA REVISION? ESCRIBELA:  ").upper()

                                objeto_revision = revisiones.Revisiones(None, cambiofiltro, cambioaceite, cambiofrenos, otros, None)

                                resultado = objeto_revision.actualizar(revision_id)

                                if resultado:
                                    print("Revision actualizada correctamente.")
                                    input("Pulsa una tecla para continuar...")
                                    borrarPantalla()
                                else:
                                    print("Ha ocurrido un error al actualizar la revision.")
                                    input("Pulsa una tecla para continuar...")
                                    borrarPantalla()
                            case 4:
                                borrarPantalla()
                                print("\n \t .:::   ELIMINAR REVISION   :::.\n")

                                revision_id = input("INGRESA EL NUMERO DE LA REVISION A ELIMINAR: ")

                                obj_revision = revisiones.Revisiones(0, "", "", "", "", "")

                                resultado = obj_revision.eliminar(revision_id)

                                if resultado:
                                    print("Revision eliminada correctamente.")
                                    input("Pulsa una tecla para continuar...")
                                    borrarPantalla()
                                else:
                                    print("Ha ocurrido un error al eliminar la revision.")
                                    input("Pulsa una tecla para continuar...")
                                    borrarPantalla()

                            case 5:
                                borrarPantalla()
                                break
                            case _:
                                print("Has escogido una opcion invalida, intenta de nuevo...")
            case 4:
                borrarPantalla()
                break
            case _:
                borrarPantalla()
                print("Opcion incorrecta, intenta de nuevo.")
                input("Pulsa cualquier tecla para continuar...")
if __name__ == "__main__":
    menu_login()

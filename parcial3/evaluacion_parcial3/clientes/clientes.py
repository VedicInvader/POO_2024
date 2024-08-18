from conexionDB import *

class Clientes():
    def __init__(self, nif, nombre, direccion, ciudad, tel):
        self.nif = nif
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.tel = tel

    def insertar(self):
        try:
            cursor.execute(
                "INSERT INTO clientes(nif, nombre, direccion, ciudad, tel) VALUES(%s, %s, %s, %s, %s)",
                (self.nif, self.nombre, self.direccion, self.ciudad, self.tel)
            )

            conexion.commit()
            return True
        
        except Exception as exp:
            print("Ha ocurrido un error al crear el auto. ", exp)
            return False
        
    @classmethod
    def consultar(self):
        try:
            cursor.execute(
                "SELECT * FROM clientes"
            )

            registros = cursor.fetchall()

            if not registros:
                print("\nNO EXISTEN REGISTROS.")

            for registro in registros:
                if len(registros) == 1:
                    print(f"\nN.I.F.: {registro[0]}, \nNombre: {registro[1]}, \nDireccion: {registro[2]}, \nCiudad: {registro[3]}, \nTelefono: {registro[4]}\n")
                else:
                    print(f"N.I.F.: {registro[0]}, \nNombre: {registro[1]}, \nDireccion: {registro[2]}, \nCiudad: {registro[3]}, \nTelefono: {registro[4]}\n") 
            
            conexion.commit()

            return True
        except Exception as exp:
            print("Ha ocurrido un error al mostrar los autos. ", exp)
            return False
        
    def actualizar(self, nif_id):
        try:
            cursor.execute(
                "UPDATE clientes SET nombre = %s, direccion = %s, ciudad = %s, tel = %s WHERE nif = %s",
                (self.nombre, self.direccion, self.ciudad, self.tel, nif_id)
            )
        
            conexion.commit()
            return True
        except Exception as exp:
            print("Ha ocurrido un error al actualizar el auto. ", exp)
            return False
        
    def eliminar(self, nif_id):
        try:
            cursor.execute(
                "DELETE FROM clientes WHERE nif = %s",
                (nif_id,)
            )

            conexion.commit()
            return True
        except Exception as exp:
            print("Ha ocurrido un error al eliminar el auto. ", exp)
            return False
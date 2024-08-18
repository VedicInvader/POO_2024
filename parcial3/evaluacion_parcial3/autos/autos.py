from conexionDB import *


class Autos():
    def __init__(self, matricula, marca, modelo, color, nif):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.nif = nif
    
    def insertar(self):
        try:
            cursor.execute(
                "INSERT INTO autos(matricula, marca, modelo, color, nif) VALUES(%s, %s, %s, %s, %s)",
                (self.matricula, self.marca, self.modelo, self.color, self.nif)
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
                "SELECT * FROM autos"
            )

            registros = cursor.fetchall()

            if not registros:
                print("\nNO EXISTEN REGISTROS.")

            for registro in registros:
                if len(registros) == 1:
                    print(f"\nMatricula: {registro[0]}, \nMarca: {registro[1]}, \nModelo: {registro[2]}, \nColor: {registro[3]}, \nN.I.F.: {registro[4]}\n")
                else:
                    print(f"Matricula: {registro[0]}, \nMarca: {registro[1]}, \nModelo: {registro[2]}, \nColor: {registro[3]}, \nN.I.F.: {registro[4]}\n") 
            
            conexion.commit()

            return True
        except Exception as exp:
            print("Ha ocurrido un error al mostrar los autos. ", exp)
            return False
        
    def actualizar(self, matricula_id):
        try:
            cursor.execute(
                "UPDATE autos SET marca = %s, modelo = %s, color = %s, nif = %s WHERE matricula = %s",
                (self.marca, self.modelo, self.color, self.nif, matricula_id)
            )
        
            conexion.commit()
            return True
        except Exception as exp:
            print("Ha ocurrido un error al actualizar el auto. ", exp)
            return False
        
    def eliminar(self, matricula_id):
        try:
            cursor.execute(
                "DELETE FROM autos WHERE matricula = %s",
                (matricula_id,)
            )

            conexion.commit()
            return True
        except Exception as exp:
            print("Ha ocurrido un error al eliminar el auto. ", exp)
            return False
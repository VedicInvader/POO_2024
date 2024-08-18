from conexionDB import *

class Revisiones():
    def __init__(self, no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula):
        self.no_revision = no_revision
        self.cambiofiltro = cambiofiltro
        self.cambioaceite = cambioaceite
        self.cambiofrenos = cambiofrenos
        self.otros = otros
        self.matricula = matricula
    
    def insertar(self):
        try:
            cursor.execute(
                "INSERT INTO revisiones(no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula) VALUES(%s, %s, %s, %s, %s, %s)",
                (self.no_revision, self.cambiofiltro, self.cambioaceite, self.cambiofrenos, self.otros, self.matricula)
            )

            conexion.commit()
            return True
        
        except Exception as exp:
            print("Ha ocurrido un error al crear la revision. ", exp)
            return False
        
    @classmethod
    def consultar(self):
        try:
            cursor.execute(
                "SELECT * FROM revisiones"
            )

            registros = cursor.fetchall()

            if not registros:
                print("\nNO EXISTEN REGISTROS.")

            for registro in registros:
                if len(registros) == 1:
                    print(f"\nNumero de revision: {registro[0]}, \nCambio de filtro: {registro[1]}, \nCambio de aceite: {registro[2]}, \nCambio de frenos: {registro[3]}, \nOtros: {registro[4]}\nMatricula: {registro[5]}\n")
                else:
                    print(f"\nNumero de revision: {registro[0]}, \nCambio de filtro: {registro[1]}, \nCambio de aceite: {registro[2]}, \nCambio de frenos: {registro[3]}, \nOtros: {registro[4]}\nMatricula: {registro[5]}\n")
            
            conexion.commit()

            return True
        except Exception as exp:
            print("Ha ocurrido un error al mostrar las revisiones. ", exp)
            return False
        
    def actualizar(self, revision_id):
        try:
            cursor.execute(
                "UPDATE revisiones SET cambiofiltro = %s, cambioaceite = %s, cambiofrenos = %s, otros = %s WHERE no_revision = %s",
                (self.cambiofiltro, self.cambioaceite, self.cambiofrenos, self.otros, revision_id)
            )
        
            conexion.commit()
            return True
        except Exception as exp:
            print("Ha ocurrido un error al actualizar la revision. ", exp)
            return False
        
    def eliminar(self, revision_id):
        try:
            cursor.execute(
                "DELETE FROM revisiones WHERE no_revision = %s",
                (revision_id,)
            )

            conexion.commit()
            return True
        except Exception as exp:
            print("Ha ocurrido un error al eliminar el auto. ", exp)
            return False
#Codificar la clase Usuarios
from conexionBD import *
import hashlib
import datetime

class Usuarios():
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = self.hash_password(password)


    def hash_password (self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def registrar(self):
        try:
            fecha = datetime.datetime.now()
            cursor.execute("INSERT INTO usuarios VALUES ( null, %s, %s, %s, %s, %s)"
                        (self.nombre, self.apellidos, self.email, self.password, fecha)
                        )
            conexion.commit()
        except:
            return False

    def iniciar_sesion (email, password):
        pass   
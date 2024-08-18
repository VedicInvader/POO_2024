from conexionDB import *
import hashlib
import datetime

class Usuarios():
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.contrasena = self.hash_password(password)
    
    def hash_password(self, contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()
    
    def registrar(self):
        try:
            fecha = datetime.datetime.now()
            cursor.execute(
                "INSERT INTO usuarios(nombre, apellidos, email, contrasena, fecha) VALUES (%s, %s, %s, %s, %s)",
                (self.nombre, self.apellidos, self.email, self.contrasena, fecha)
            )

            conexion.commit()
            return True
        
        except Exception as exp:
            print("Ocurrio un error al registrar el usuario. ", exp)
            return False
    
    @staticmethod
    def iniciar_sesion(email, contrasena):
        try:
            contrasena = hashlib.sha256(contrasena.encode()).hexdigest()
            cursor.execute(
                "SELECT * FROM usuarios WHERE email = %s AND contrasena = %s",
                (email, contrasena)
            )

            usuario = cursor.fetchone()

            if usuario:
                return usuario
            else:
                return None
        except Exception as exp:
            print("Ha ocurrido un error al iniciar sesion. ", exp)
            return None
import mysql.connector as mysql
from root import contrasena

try:
    conexion = mysql.connect(
        host = "localhost",
        user = "root",
        password = contrasena,
        database = "bd_notas"
    )
    
except Exception as excepcion:
    print(f"Error: {excepcion}")
    print(f"Tipo de error: {type(excepcion).__name__}")
    print("Ha ocurrido un problema... intente despues.")
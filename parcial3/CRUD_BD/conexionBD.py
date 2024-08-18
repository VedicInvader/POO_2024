import mysql.connector as mysql

#Conectar con la base de datos MySQL

try:
    conexion = mysql.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "bd_python"
    )
except Exception as excepcion:
    print(f"Error: {excepcion}")
    print(f"Tipo de error: {type(excepcion).__name__}")
    print("Ocurrio un problema. Intente despues.")
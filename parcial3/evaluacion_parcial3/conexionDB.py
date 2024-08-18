import mysql.connector

try:
    conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "agencia_autos_datos",
    )

    cursor = conexion.cursor(buffered = True)

except Exception as excepcion:
    print(f"Error: {excepcion}")
    print(f"Tipo de error: {type(excepcion).__name__}")
    print("Ha ocurrido un problema, intenta despues.")
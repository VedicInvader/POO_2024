import mysql.connector as mysql

try:
    conexion = mysql.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "bd_python"
    )
except:
    print("Ha ocurrido un error. Intente despues.")
else:
    #Crear tabla
    sql = "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTO_INCREMENT, nombre VARCHAR(60), direccion VARCHAR(120), tel VARCHAR(15))"

    cursor_bd = conexion.cursor()

    cursor_bd.execute(sql)


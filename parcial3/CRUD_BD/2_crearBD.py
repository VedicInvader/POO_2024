import mysql.connector as mysql

try:
    #Crear la conexion con la BD

    conexion = mysql.connect(
        host = "localhost",
        user = "root",
        password = ""
    )

except Exception as excepcion:
    print(f"Error: {excepcion}")
    print(f"Tipo de error: {type(excepcion).__name__}")
    print("Ocurrio un error, intente mas tarde.")
else:
        #Verificar la conexion
    if conexion.is_connected():
        print("Conexion exitosa.")

    else:
        print("La conexion ha fallado. Intente de nuevo...")


    #Crear otro objeto para ejecutar las conexiones
    mi_cursor = conexion.cursor()

    #Crear BD desde Python
    sql = "CREATE DATABASE bd_python"
    mi_cursor.execute(sql)

    #Verificar que se haya creada la base de datos

    if mi_cursor:
        print("Base de datos creada con exito.")
    else:
        print("Hubo un fallo al crear la base de datos")

    #Mostrar las bases de datos que existen en mi servidor de MySQL

    mi_cursor.execute("SHOW DATABASES")

    for iterador in mi_cursor:
        print(iterador)
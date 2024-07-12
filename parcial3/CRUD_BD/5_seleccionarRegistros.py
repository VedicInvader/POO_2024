from conexionBD import *

micursor=conexion.cursor()
try:
  sql="SELECT nombre,direccion,tel FROM clientes"
  micursor.execute(sql)
  resultado=micursor.fetchall()

  if len(resultado)>0:
    print(f"Registros de la tabla: {len(resultado)}")
    for x in resultado:
      print(x)

except:
   print("Ha ocurrido un error... Intente despues.")
else:
  print("Registros consultados correctamente.")



from conexionBD import *

micursor=conexion.cursor()

try:
   sql="update clientes set tel='6181112233' where id='4'"
   micursor.execute(sql)
   conexion.commit()
except:
   print("Ha ocurrido un error... Intente mas tarde.")
else:
   print(f"Registro Actualizado Correctamente")
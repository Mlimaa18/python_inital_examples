#Conexión a base de datos

import mysql.connector

conexion = mysql.connector.connect(
    user = "root",
    password = "",
    host = "localhost",
    database = "curso_python"
)

print(conexion)

cursor = conexion.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS curso_python")
cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS user(
        user_id int(11) auto_increment NOT NULL,
        user_name varchar(50) null,
        user_password varchar(120) null,
        user_email varchar(100) null,
        user_status char(1) null,
        CONSTRAINT pk_user PRIMARY KEY (user_id)
    )
""")

conexion.close()


#hacer busqueda de amplitud de juego de:
# 1 2 3,
# 4 5 6,
# 7 8 _ 
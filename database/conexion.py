import mysql.connector


CONFIG_BD = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "sga_universidad"
}


def obtener_conexion():

    return mysql.connector.connect(
        **CONFIG_BD
    )
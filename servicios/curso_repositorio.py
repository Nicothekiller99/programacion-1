from database.conexion import (
    obtener_conexion
)


class CursoRepositorio:

    def guardar(
        self,
        curso
    ):

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        sql = """
        insert into cursos
        values(
        %s,%s,%s,%s
        )
        """

        cursor.execute(
            sql,
            (
                curso.get_codigo(),
                curso.get_nombre(),
                3,
                30
            )
        )

        conexion.commit()

        conexion.close()
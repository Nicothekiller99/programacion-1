from database.conexion import (
    obtener_conexion
)


class MatriculaRepositorio:

    def guardar(
        self,
        estudiante_id,
        curso_codigo
    ):

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        sql = """
        insert into matriculas(
        estudiante_id,
        curso_codigo
        )
        values(
        %s,
        %s
        )
        """

        cursor.execute(
            sql,
            (
                estudiante_id,
                curso_codigo
            )
        )

        conexion.commit()

        conexion.close()
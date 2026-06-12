from database.conexion import (
    obtener_conexion
)


class EstudianteRepositorio:

    def guardar(
        self,
        estudiante
    ):

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        sql = """
        insert into estudiantes
        values(
        %s,%s,%s,%s,%s
        )
        """

        cursor.execute(
            sql,
            (
                estudiante.get_identificacion(),
                estudiante.get_nombre(),
                estudiante.get_email(),
                estudiante.get_codigo(),
                estudiante.get_programa()
            )
        )

        conexion.commit()
        conexion.close()

    def listar_todos(self):

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute(
            "select * from estudiantes"
        )

        return cursor.fetchall()

    def eliminar(
        self,
        identificacion
    ):

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute(
            """
            delete from estudiantes
            where identificacion=%s
            """,
            (identificacion,)
        )

        conexion.commit()

        conexion.close()
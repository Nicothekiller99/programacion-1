from modelos.calificacion import (
    Calificacion
)


class Matricula:

    def __init__(
        self,
        estudiante,
        curso
    ):

        self.__estudiante = estudiante
        self.__curso = curso
        self.__calificaciones = []

    def agregar_calificacion(
        self,
        actividad,
        nota
    ):

        self.__calificaciones.append(
            Calificacion(
                actividad,
                nota
            )
        )

    def promedio(self):

        if len(
            self.__calificaciones
        ) == 0:
            return 0

        suma = sum(
            nota.get_nota()
            for nota in self.__calificaciones
        )

        return round(
            suma /
            len(
                self.__calificaciones
            ),
            2
        )
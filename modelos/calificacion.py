class Calificacion:

    def __init__(
        self,
        actividad,
        nota
    ):

        self.__actividad = actividad

        if not 0 <= nota <= 5:
            raise ValueError(
                "nota invalida"
            )

        self.__nota = nota

    def get_nota(self):
        return self.__nota
class GestorCursos:

    def __init__(self):

        self.__cursos = []
        self.__matriculas = []

    def agregar_curso(
        self,
        curso
    ):
        self.__cursos.append(
            curso
        )

    def matricular(
        self,
        matricula
    ):
        self.__matriculas.append(
            matricula
        )
class GestorEstudiantes:

    def __init__(self):
        self.__estudiantes = []

    def registrar(
        self,
        estudiante
    ):
        self.__estudiantes.append(
            estudiante
        )

    def listar(self):
        return self.__estudiantes
class Curso:

    def __init__(
        self,
        codigo,
        nombre,
        creditos,
        cupo_maximo
    ):

        self.__codigo = codigo
        self.__nombre = nombre
        self.__creditos = creditos
        self.__cupo_maximo = cupo_maximo

        self.__docente = None
        self.__estudiantes = []

    def asignar_docente(
        self,
        docente
    ):
        self.__docente = docente

    def agregar_estudiante(
        self,
        estudiante
    ):
        self.__estudiantes.append(
            estudiante
        )

    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre
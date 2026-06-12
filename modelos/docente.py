from modelos.persona import Persona


class Docente(Persona):

    def __init__(
        self,
        identificacion,
        nombre,
        email,
        especialidad,
        titulo
    ):
        super().__init__(
            identificacion,
            nombre,
            email
        )

        self.__especialidad = especialidad
        self.__titulo = titulo
        self.__cursos = []

    def agregar_curso(self, curso):
        self.__cursos.append(curso)

    def mostrar_info(self):
        return (
            f"docente: "
            f"{self.get_nombre()} "
            f"- {self.__especialidad}"
        )
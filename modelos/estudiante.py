from modelos.persona import Persona


class Estudiante(Persona):

    def __init__(
        self,
        identificacion,
        nombre,
        email,
        codigo,
        programa,
        promedio=0.0
    ):
        super().__init__(
            identificacion,
            nombre,
            email
        )

        self.set_codigo(codigo)
        self.set_programa(programa)
        self.__promedio = promedio

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        if not codigo.strip():
            raise ValueError(
                "codigo invalido"
            )
        self.__codigo = codigo

    def get_programa(self):
        return self.__programa

    def set_programa(self, programa):
        if not programa.strip():
            raise ValueError(
                "programa invalido"
            )
        self.__programa = programa

    def get_promedio(self):
        return self.__promedio

    def mostrar_info(self):
        return (
            f"estudiante: "
            f"{self.get_nombre()} "
            f"- {self.__programa}"
        )
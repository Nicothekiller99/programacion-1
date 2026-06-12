from abc import ABC, abstractmethod


class Persona(ABC):

    def __init__(self, identificacion, nombre, email):
        self.set_identificacion(identificacion)
        self.set_nombre(nombre)
        self.set_email(email)

    def get_identificacion(self):
        return self.__identificacion

    def set_identificacion(self, identificacion):
        if not identificacion.strip():
            raise ValueError(
                "identificacion invalida"
            )
        self.__identificacion = identificacion

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        if not nombre.strip():
            raise ValueError(
                "nombre invalido"
            )
        self.__nombre = nombre

    def get_email(self):
        return self.__email

    def set_email(self, email):
        if "@" not in email:
            raise ValueError(
                "correo invalido"
            )
        self.__email = email

    @abstractmethod
    def mostrar_info(self):
        pass
import pytest

from modelos.estudiante import (
    Estudiante
)

from modelos.docente import (
    Docente
)

from modelos.calificacion import (
    Calificacion
)

from modelos.matricula import (
    Matricula
)

from modelos.curso import (
    Curso
)


def test_estudiante_valido():

    estudiante = Estudiante(
        "1",
        "juan",
        "juan@gmail.com",
        "est01",
        "ingenieria"
    )

    assert (
        estudiante.get_nombre()
        ==
        "juan"
    )


def test_calificacion_valida():

    nota = Calificacion(
        "parcial",
        4.5
    )

    assert (
        nota.get_nota()
        ==
        4.5
    )


def test_calificacion_invalida():

    with pytest.raises(
        ValueError
    ):

        Calificacion(
            "parcial",
            6.0
        )


def test_promedio_correcto():

    estudiante = Estudiante(
        "1",
        "juan",
        "juan@gmail.com",
        "est01",
        "ingenieria"
    )

    curso = Curso(
        "poo",
        "programacion",
        3,
        30
    )

    matricula = Matricula(
        estudiante,
        curso
    )

    matricula.agregar_calificacion(
        "parcial",
        4.0
    )

    matricula.agregar_calificacion(
        "final",
        5.0
    )

    assert (
        matricula.promedio()
        ==
        4.5
    )


def test_polimorfismo():

    estudiante = Estudiante(
        "1",
        "juan",
        "a@a.com",
        "est01",
        "sistemas"
    )

    docente = Docente(
        "2",
        "carlos",
        "b@b.com",
        "poo",
        "msc"
    )

    assert (
        estudiante.mostrar_info()
        !=
        docente.mostrar_info()
    )
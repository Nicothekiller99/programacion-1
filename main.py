from modelos.estudiante import (
    Estudiante
)

from modelos.curso import (
    Curso
)

from modelos.matricula import (
    Matricula
)


while True:

    print("\n")
    print("=== star ===")
    print("1. estudiantes")
    print("2. cursos")
    print("3. matriculas")
    print("4. reportes")
    print("5. salir")

    opcion = input(
        "seleccione: "
    )

    try:

        if opcion == "1":

            nombre = input(
                "nombre: "
            )

            estudiante = Estudiante(
                "100",
                nombre,
                "correo@gmail.com",
                "est001",
                "ingenieria de sistemas"
            )

            print(
                estudiante.mostrar_info()
            )

        elif opcion == "2":

            curso = Curso(
                "poo01",
                "programacion orientada a objetos",
                3,
                30
            )

            print(
                curso.get_nombre()
            )

        elif opcion == "3":

            estudiante = Estudiante(
                "100",
                "juan",
                "juan@gmail.com",
                "est01",
                "ingenieria"
            )

            curso = Curso(
                "poo01",
                "poo",
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

            print(
                matricula.promedio()
            )

        elif opcion == "4":

            print(
                "modulo reportes"
            )

        elif opcion == "5":

            break

        else:

            print(
                "opcion invalida"
            )
            

    except ValueError as error:

        print(
            f"error: {error}"
        )
        
# fin del programa
create database if not exists sga_universidad;

use sga_universidad;

create table estudiantes(

    identificacion varchar(20)
    primary key,

    nombre varchar(100)
    not null,

    email varchar(100)
    not null,

    codigo varchar(20)
    not null,

    programa varchar(100)
    not null
);

create table docentes(

    identificacion varchar(20)
    primary key,

    nombre varchar(100)
    not null,

    email varchar(100)
    not null,

    especialidad varchar(100),

    titulo varchar(100)
);

create table cursos(

    codigo varchar(20)
    primary key,

    nombre varchar(100)
    not null,

    creditos int,

    cupo_maximo int
);

create table matriculas(

    id int
    auto_increment
    primary key,

    estudiante_id varchar(20),

    curso_codigo varchar(20),

    foreign key(estudiante_id)
    references estudiantes(
        identificacion
    ),

    foreign key(curso_codigo)
    references cursos(
        codigo
    )
);
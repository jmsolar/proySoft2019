from enum import IntEnum


def get_day(num):
    day = DiaSemana(num)
    return day.name


class DiaSemana(IntEnum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

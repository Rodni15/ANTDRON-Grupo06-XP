"""Modelo de una fila de Grupo06.csv (UML: pkAntCiberDronContract.CoordenadaUK)."""


class CoordenadaUK:
    def __init__(self, geoposicion: str, lunes: str = "", martes: str = "",
                 miercoles: str = "", jueves: str = "", viernes: str = "",
                 tipoArsenal: str = ""):
        self.__geoposicion = geoposicion
        self.__lunes = lunes
        self.__martes = martes
        self.__miercoles = miercoles
        self.__jueves = jueves
        self.__viernes = viernes
        self.__tipoArsenal = tipoArsenal

    def getGeoposicion(self) -> str:
        return self.__geoposicion

    def getTipoArsenal(self) -> str:
        return self.__tipoArsenal

    def getHorarios(self) -> list[str]:
        return [self.__lunes, self.__martes, self.__miercoles, self.__jueves, self.__viernes]

    def __str__(self) -> str:
        return f"CoordenadaUK({self.__geoposicion}, {self.__tipoArsenal})"

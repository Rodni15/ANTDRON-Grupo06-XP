"""Registro de entrenamiento de inglés y español en la simulación."""

from dataclasses import dataclass
from enum import Enum

from ant.db.sqlite_connection import SqliteConnection


class Idioma(str, Enum):
    EN = "EN"
    ES = "ES"


class Area(str, Enum):
    LEXICO = "léxico"
    GRAMATICA = "gramática"
    FONETICA = "fonética"


@dataclass(frozen=True)
class ExpertoParlante:
    nombre: str
    idioma: Idioma
    certificado: bool = False


@dataclass(frozen=True)
class Entrenamiento:
    area: Area
    contenido: str
    experto: ExpertoParlante


class ModuloIdioma:
    def __init__(self, almacenamiento: SqliteConnection | None = None) -> None:
        self._entrenamientos: list[Entrenamiento] = []
        self._almacenamiento = almacenamiento

    def entrenar(self, idioma: Idioma, area: Area, dato: str, experto: ExpertoParlante) -> bool:
        if not isinstance(experto, ExpertoParlante) or not experto.certificado:
            return False
        idioma = Idioma(idioma)
        if experto.idioma != idioma or not dato.strip():
            return False
        registro = Entrenamiento(Area(area), dato.strip(), experto)
        if self._almacenamiento is None:
            self._entrenamientos.append(registro)
        else:
            with self._almacenamiento.abrir() as db:
                db.execute(
                    "INSERT INTO entrenamiento_idioma(experto, idioma, area, contenido) VALUES (?, ?, ?, ?)",
                    (experto.nombre, idioma.value, registro.area.value, registro.contenido),
                )
        return True

    def consultar(self, idioma: Idioma) -> tuple[Entrenamiento, ...]:
        idioma = Idioma(idioma)
        if self._almacenamiento is not None:
            with self._almacenamiento.abrir() as db:
                filas = db.execute(
                    "SELECT experto, area, contenido FROM entrenamiento_idioma WHERE idioma = ? ORDER BY id",
                    (idioma.value,),
                )
                return tuple(Entrenamiento(Area(area), contenido, ExpertoParlante(nombre, idioma, True))
                             for nombre, area, contenido in filas)
        return tuple(registro for registro in self._entrenamientos if registro.experto.idioma == idioma)

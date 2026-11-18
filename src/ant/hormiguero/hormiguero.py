"""Gestiona la identidad de cada hormiga durante su transformación."""

from ant.alimento.alimento import AHervivoro, Alimento
from ant.db.sqlite_connection import SqliteConnection
from ant.hormiguero.hormiga import HLarva, Hormiga, HRastreadora


TIPOS = {"HLarva": HLarva, "HRastreadora": HRastreadora}


class Hormiguero:
    def __init__(self, almacenamiento: SqliteConnection | None = None) -> None:
        self._hormigas: dict[int, Hormiga] = {}
        self._almacenamiento = almacenamiento

    def crearLarva(self, sexo: str) -> HLarva:
        if self._almacenamiento is not None:
            with self._almacenamiento.abrir() as db:
                cursor = db.execute("INSERT INTO hormiga(tipo, sexo, estado) VALUES ('HLarva', ?, 'VIVA')", (sexo,))
                return HLarva(cursor.lastrowid, sexo)
        larva = HLarva(len(self._hormigas) + 1, sexo)
        self._hormigas[larva.Id] = larva
        return larva

    def alimentar(self, id_hormiga: int, alimento: Alimento) -> bool:
        if self._almacenamiento is not None:
            with self._almacenamiento.abrir() as db:
                db.execute("BEGIN IMMEDIATE")
                fila = db.execute("SELECT tipo, sexo, estado FROM hormiga WHERE id = ?", (id_hormiga,)).fetchone()
                if fila is None:
                    raise KeyError(id_hormiga)
                tipo, sexo, estado = fila
                hormiga = self._alimentar(TIPOS[tipo](id_hormiga, sexo, estado), alimento)
                db.execute("UPDATE hormiga SET tipo = ?, estado = ? WHERE id = ?",
                           (type(hormiga).__name__, hormiga.estado, id_hormiga))
                db.execute("INSERT INTO alimentacion(hormiga_id, alimento, resultado) VALUES (?, ?, ?)",
                           (id_hormiga, str(alimento), f"{type(hormiga).__name__}:{hormiga.estado}"))
                return hormiga.estado == "VIVA"
        hormiga = self._alimentar(self._hormigas[id_hormiga], alimento)
        self._hormigas[id_hormiga] = hormiga
        return hormiga.estado == "VIVA"

    @staticmethod
    def _alimentar(hormiga: Hormiga, alimento: Alimento) -> Hormiga:
        vive = hormiga.comer(alimento)
        if vive and isinstance(hormiga, HLarva) and isinstance(alimento, AHervivoro):
            return HRastreadora(hormiga.Id, hormiga.sexo)
        return hormiga

    def listarHormigas(self) -> list[Hormiga]:
        if self._almacenamiento is not None:
            with self._almacenamiento.abrir() as db:
                filas = db.execute("SELECT id, tipo, sexo, estado FROM hormiga ORDER BY id")
                return [TIPOS[tipo](id_, sexo, estado) for id_, tipo, sexo, estado in filas]
        return list(self._hormigas.values())

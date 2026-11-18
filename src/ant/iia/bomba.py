"""Bomba inteligente e impresión de la tabla de coordenadas ucranianas a destruir."""
from typing import Any, Iterable

from ant.iia.bomba_automata import BombaAutomata
from pkAntCiberDronContract.coordenada_uk import CoordenadaUK

ENCABEZADO_DESTRUIR = f"{'Geoposición':<11} | {'Tipo Arsenal':<12} | Acción"


class Bomba:
    """Evalúa si la bomba debe explotar según el autómata del Grupo 06."""

    def __init__(self, automata: BombaAutomata | None = None) -> None:
        self.automata: BombaAutomata = automata or BombaAutomata()

    def explotar(self, palabra: str) -> bool:
        """True si el tipo de arsenal corresponde a un objetivo autorizado."""
        return self.automata.evaluar(palabra)

    def buscar(self, tipoArsenal: str) -> bool:
        """Alias compatible con el contrato IIA.buscar(tipoArsenal) -> bool."""
        return self.explotar(tipoArsenal)


def _resolver_funcion_evaluadora(evaluador: Any = None):
    """Permite evaluar con Bomba, BombaAutomata, AntCiberDron (IIA) o función."""
    if evaluador is None:
        bomba = Bomba()
        return bomba.explotar
    if callable(evaluador):
        return evaluador
    for nombre_metodo in ("buscar", "explotar", "evaluar", "aceptar"):
        metodo = getattr(evaluador, nombre_metodo, None)
        if callable(metodo):
            return metodo
    raise TypeError("El evaluador debe exponer buscar, explotar, evaluar o aceptar.")


def mostrar_destruir(
    coordenadas: Iterable[CoordenadaUK],
    evaluador: Any = None,
) -> list[CoordenadaUK]:
    """Imprime la tabla COORDENADAS UCRANIANAS A DESTRUIR y retorna las detonadas."""
    evaluar = _resolver_funcion_evaluadora(evaluador)
    destruidas: list[CoordenadaUK] = []

    print("\nCOORDENADAS UCRANIANAS A DESTRUIR:")
    print(ENCABEZADO_DESTRUIR)
    for coord in coordenadas:
        arsenal = coord.getTipoArsenal()
        if evaluar(arsenal):
            destruidas.append(coord)
            print(f"{coord.getGeoposicion():<11} | {arsenal:<12} | true")
    return destruidas

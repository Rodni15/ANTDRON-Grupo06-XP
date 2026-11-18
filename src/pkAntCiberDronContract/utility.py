"""Utilidades de consola (UML: pkAntCiberDronContract.Utility)."""
import sys
import time

from pkAntCiberDronContract.coordenada_uk import CoordenadaUK

SPINNER = "\\|/-"
ENCABEZADO = (f"{'Loading':<8}| {'Geoposición':^11}| {'Lunes':^7}| {'Martes':^7}| "
              f"{'Miércoles':^9}| {'Jueves':^7}| {'Viernes':^7}| Tipo Arsenal")


class Utility:
    @staticmethod
    def mostrarLoading(delayMs: int = 20) -> None:
        """Gira el spinner \\ | / - mientras sube el porcentaje hasta 100%."""
        for paso, porcentaje in enumerate(range(0, 101, 5)):
            sys.stdout.write(f"\r{SPINNER[paso % 4]} {porcentaje}%   ")
            sys.stdout.flush()
            if delayMs > 0:
                time.sleep(delayMs / 1000)

    @staticmethod
    def formatearFila(c: CoordenadaUK) -> str:
        lu, ma, mi, ju, vi = c.getHorarios()
        return (f"{c.getGeoposicion():^11}| {lu:^7}| {ma:^7}| {mi:^9}| "
                f"{ju:^7}| {vi:^7}| {c.getTipoArsenal()}")

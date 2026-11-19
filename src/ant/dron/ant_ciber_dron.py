"""Modelo del exoesqueleto para la simulación académica."""

from dataclasses import dataclass

from ant.dron.modulo_idioma import ModuloIdioma
from ant.iia.iia import Evaluador, IIA


class FuenteDePoder:
    def __init__(self, capacidad: int = 100) -> None:
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser positiva")
        self._capacidad = capacidad
        self.recargar()

    def recargar(self) -> None:
        self._energia = self._capacidad

    def getEnergia(self) -> int:
        return self._energia

    def consumir(self, cantidad: int) -> bool:
        if cantidad <= 0:
            raise ValueError("El consumo debe ser positivo")
        if cantidad > self._energia:
            return False
        self._energia -= cantidad
        return True


class Laser:
    def calcularPotencia(self, fuente: FuenteDePoder) -> int:
        return fuente.getEnergia()


class Metralleta:
    def calcularPotencia(self, fuente: FuenteDePoder) -> int:
        return fuente.getEnergia()


@dataclass(frozen=True)
class Pata:
    posicion: str
    equipo: Laser | Metralleta | None = None


class TurboReactor:
    def activarVuelo(self, fuente: FuenteDePoder) -> bool:
        return fuente.consumir(1)


class AntCiberDron(IIA):
    def __init__(
        self,
        bomba: Evaluador,
        fuente: FuenteDePoder | None = None,
        modulo_idioma: ModuloIdioma | None = None,
    ) -> None:
        self.bomba = bomba
        self.fuente = fuente if fuente is not None else FuenteDePoder()
        self.laserDelanteroIzq = Laser()
        self.metralletaDelanteraDer = Metralleta()
        self.turboEspalda = TurboReactor()
        self.moduloIdioma = modulo_idioma if modulo_idioma is not None else ModuloIdioma()
        self.cabeza = "cabeza con antenas"
        self.torax = "tórax"
        self.abdomen = "abdomen"
        self.patas = (
            Pata("delantera izquierda", self.laserDelanteroIzq),
            Pata("delantera derecha", self.metralletaDelanteraDer),
            Pata("media izquierda"),
            Pata("media derecha"),
            Pata("trasera izquierda"),
            Pata("trasera derecha"),
        )

    def buscar(self, tipoArsenal: str) -> bool:
        for nombre in ("buscar", "explotar", "evaluar", "aceptar"):
            metodo = getattr(self.bomba, nombre, None)
            if callable(metodo):
                return bool(metodo(tipoArsenal))
        raise TypeError("La bomba debe exponer un método de evaluación.")

    def volar(self) -> bool:
        return self.turboEspalda.activarVuelo(self.fuente)

    def dispararLaser(self) -> int:
        return self.laserDelanteroIzq.calcularPotencia(self.fuente)

    def asistirRecargaFuente(self) -> None:
        self.fuente.recargar()

    def asistirReemplazoFuente(self, nueva: FuenteDePoder) -> None:
        self.fuente = nueva

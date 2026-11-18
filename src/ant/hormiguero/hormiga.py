"""Ciclo de alimentación del grupo 06."""

from abc import ABC, abstractmethod
from dataclasses import dataclass

from ant.alimento.alimento import AHervivoro, Alimento, Nectar


class IHormiga(ABC):
    @abstractmethod
    def comer(self, alimento: Alimento) -> bool: ...


@dataclass
class Hormiga(IHormiga):
    Id: int = 0
    sexo: str = ""
    estado: str = "VIVA"

    def morir(self) -> None:
        self.estado = "MUERTA"

    def __str__(self) -> str:
        return f"{type(self).__name__} #{self.Id} ({self.sexo}, {self.estado})"


class HRastreadora(Hormiga):
    def comer(self, alimento: Alimento) -> bool:
        if not isinstance(alimento, AHervivoro):
            self.morir()
        return self.estado == "VIVA"


class HLarva(Hormiga):
    def comer(self, alimento: Alimento) -> bool:
        if not isinstance(alimento, (Nectar, AHervivoro)):
            self.morir()
        return self.estado == "VIVA"

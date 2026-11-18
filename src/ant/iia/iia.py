"""Contrato de evaluación de palabras del CSV académico."""

from abc import ABC, abstractmethod
from typing import Protocol


class Evaluador(Protocol):
    def explotar(self, palabra: str) -> bool: ...


class IIA(ABC):
    @abstractmethod
    def buscar(self, tipoArsenal: str) -> bool: ...

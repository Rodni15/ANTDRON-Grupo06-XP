"""Alimentos del hormiguero virtual del grupo 06."""

from abc import ABC, abstractmethod


class Alimento(ABC):
    @abstractmethod
    def __str__(self) -> str: ...


class Nectar(Alimento):
    def __str__(self) -> str:
        return "néctar"


class AHervivoro(Alimento):
    def __str__(self) -> str:
        return "herbívoro"

"""Sistema de la KGD (UML: pkAntCiberDronContract.SistemaRuso)."""
import csv
import sys

from pkAntCiberDronContract.coordenada_uk import CoordenadaUK
from pkAntCiberDronContract.utility import ENCABEZADO, Utility

PROFESOR = ("patmic", "123")


class SistemaRuso:
    def __init__(self, integrantes: list | None = None, delayMs: int = 20):
        self.integrantes = integrantes or []
        self.delayMs = delayMs
        self.__credenciales = {i.usuario: i.clave for i in self.integrantes if i.usuario}
        self.__credenciales[PROFESOR[0]] = PROFESOR[1]

    def login(self, usuario: str, clave: str) -> bool:
        """True si el usuario es un integrante del grupo o el profesor."""
        return self.__credenciales.get((usuario or "").strip()) == (clave or "").strip()

    def mostrarEquipo(self, equipo: str, integrantes: list, numero: int = 6) -> None:
        print(f"\n[+] TEAM [{numero}]: {equipo}")
        for n, i in enumerate(integrantes, start=1):
            print(f"      • Alumno {n}: {i.cedula} | {i.nombre}")

    def readCoord(self, filename: str, mostrar: bool = True) -> list[CoordenadaUK]:
        """Lee el CSV (separado por ;) mostrando la animación antes de cada línea."""
        coordenadas: list[CoordenadaUK] = []
        try:
            with open(filename, encoding="utf-8-sig", newline="") as f:
                filas = list(csv.reader(f, delimiter=";"))
        except FileNotFoundError:
            print(f"[!] No se encontró el archivo {filename}")
            return coordenadas

        if mostrar:
            print("\n[+] COORDENADAS UCRANIANAS:")
            print(ENCABEZADO)
        for num, campos in enumerate(filas[1:], start=2):
            campos = [c.strip() for c in campos]
            if not any(campos) or campos[0].startswith("#"):
                continue
            if len(campos) != 7:
                print(f"[!] Línea {num} ignorada: se esperaban 7 columnas")
                continue
            c = CoordenadaUK(*campos)
            coordenadas.append(c)
            if mostrar:
                Utility.mostrarLoading(self.delayMs)
                sys.stdout.write(f"\r{'100%':<8}| {Utility.formatearFila(c)}\n")
        return coordenadas

    def evaluarDestruccion(self, dron, coords: list[CoordenadaUK]) -> None:
        """Pendiente: lo implementa quien tenga el AntCiberDron (dron.buscar por coordenada)."""
        raise NotImplementedError("Se implementa junto con AntCiberDron / IIA")

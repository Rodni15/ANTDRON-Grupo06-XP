"""Punto de entrada de ANTDRON / AntCiberDron (Grupo 06).

Flujo del PDF:
  1. Login (máx. 3 intentos, 4 integrantes + patmic/123)        -> listo
  2. Presentación [+] TEAM [6]                                    -> listo
  3. SistemaRuso.readCoord("data/Grupo06.csv") con loading         -> listo
  4. AntCiberDron.buscar(tipoArsenal) -> coordenadas a destruir   -> pendiente
  5. Menú de consola del Hormiguero Virtual (src/ant/ui)          -> pendiente
"""
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ / "src"))

from ant.ruso.auth_service import AuthService  # noqa: E402
from ant.ruso.integrante import Integrante  # noqa: E402
from pkAntCiberDronContract.sistema_ruso import SistemaRuso  # noqa: E402


def main():
    equipo, grupo, integrantes = Integrante.cargarEquipo(RAIZ / "data" / "integrantes.json")
    sistema = SistemaRuso(integrantes)

    if not AuthService(sistema).autenticar():
        sys.exit(1)

    sistema.mostrarEquipo(equipo, integrantes, grupo)
    coordenadas = sistema.readCoord(RAIZ / "data" / f"Grupo{grupo:02d}.csv")

    # Pendiente (AntCiberDron / IIA): sistema.evaluarDestruccion(dron, coordenadas)
    # Pendiente (ant.ui): menú del Hormiguero Virtual


if __name__ == "__main__":
    main()

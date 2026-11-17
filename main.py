"""Punto de entrada de ANTDRON / AntCiberDron (Grupo 06).

Flujo del PDF:
  1. SistemaRuso: login (máx. 3 intentos, 4 integrantes + patmic/123)
  2. SistemaRuso: presentación [+] TEAM [6]
  3. SistemaRuso.readCoord("data/Grupo06.csv") con Utility (loading \\ | / -)
  4. AntCiberDron.buscar(tipoArsenal) por cada coordenada -> tabla de coordenadas a destruir
  5. Menú de consola del Hormiguero Virtual (src/ant/ui)

Código pendiente hasta contar con las 4 cédulas del equipo.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))


def main():
    print("ANTDRON Grupo 06 — implementación pendiente (ver PROMPT_IMPLEMENTACION.md)")


if __name__ == "__main__":
    main()
